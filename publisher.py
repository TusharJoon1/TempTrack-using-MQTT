import paho.mqtt.client as mqtt
from random import uniform
import time

# Define the MQTT broker address and port
mqttBroker = "mqtt.eclipseprojects.io"
mqttPort = 1883

# Callback function for successful connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print(f"Connect failed with code {rc}")

# Create an MQTT client instance 
client = mqtt.Client()
client.on_connect = on_connect

# Connect to the broker
client.connect(mqttBroker, mqttPort, 60)

# Start the MQTT client loop
client.loop_start()

try:
    while True:
        # Generate a random temperature value
        randNumber = uniform(20.0, 21.0)
        # Publish the value to the TEMPERATURE topic
        client.publish("TEMPERATURE", randNumber)
        print(f"Just published {randNumber} to Topic TEMPERATURE")
        time.sleep(1)
except KeyboardInterrupt:
    print("Disconnected from broker")
finally:
    client.loop_stop()
    client.disconnect()
