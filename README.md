# TempTrack-using-MQTT

TempTrack is a simple Flask-based web application designed to monitor sensor data, provide real-time updates, and trigger alarms based on the data received.

Import necessary libraries for MQTT communication, generating random numbers, and handling time delays.
import paho.mqtt.client as mqtt
from random import uniform
import time

# In suscriber
Define the temperature threshold and duration for triggering an alarm.
THRESHOLD = 21.0
DURATION = 5    -> 5 minutes, assuming one data point per minute

Also define a callback function to handle incoming MQTT messages, process the data, and update the state and add a TimeStamp for Each entry.

# In the image left side show Publisher Data and Right side show Suscriber data 
![WhatsApp Image 2024-05-19 at 10 34 51_e264c652](https://github.com/TusharJoon1/TempTrack-using-MQTT/assets/131438804/893721c2-7a62-48db-8685-657478e3be37)

# For Server
pip install Flask

Define a route to serve the index.html file from the current directory.
Define an API endpoint /sensor/last that reads the last line of the sensor_data.txt file and returns the timestamp, temperature, and alarm status as a JSON response. If the file or data is not available, it returns an error message.

The page that our Hotel Manager see is dhown below
![WhatsApp Image 2024-05-19 at 11 00 25_e93b5cd1](https://github.com/TusharJoon1/TempTrack-using-MQTT/assets/131438804/29de311b-fa14-4eae-9835-d1141af98cf9)
