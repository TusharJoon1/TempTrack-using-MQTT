import paho.mqtt.client as mqtt
from datetime import datetime
import threading

# Constants
THRESHOLD = 21.0
DURATION = 5  # 5 minutes, assuming one data point per minute

# Variables to store state
exceed_count = 0
data_points = []
last_value = None
alarm_triggered = False

# MQTT on_message callback function
def on_message(client, userdata, message):
    global exceed_count, data_points, last_value, alarm_triggered
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperature = float(message.payload.decode("utf-8"))
    
    # Save the last value received
    last_value = temperature

    # Save the data point with timestamp
    data_points.append((timestamp, temperature))
    print(f"Received message: {temperature} at {timestamp}")
    
    # Check if temperature exceeds the threshold
    if temperature > THRESHOLD:
        exceed_count += 1
    else:
        exceed_count = 0

    # Raise alarm if threshold is exceeded for the specified duration
    if exceed_count >= DURATION:
        print("Alarm! Temperature threshold exceeded continuously for 5 minutes.")
        alarm_triggered = True
        exceed_count = 0  # reset count after alarm
    else:
        alarm_triggered = False

    # Write the latest data to a file
    with open("sensor_data.txt", "a") as file:  # Changed to "a" to append data
        file.write(f"{timestamp},{temperature},{alarm_triggered}\n")

# MQTT setup
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client()
client.connect(mqttBroker)

client.on_message = on_message
client.subscribe("TEMPERATURE")

# Function to start MQTT client loop
def start_mqtt_loop():
    client.loop_forever()

# Run the MQTT client in a background thread
mqtt_thread = threading.Thread(target=start_mqtt_loop)
mqtt_thread.start()

# Run indefinitely until interrupted
try:
    while True:
        pass
except KeyboardInterrupt:
    client.loop_stop()
    print("Subscriber stopped.")
