from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/sensor/last', methods=['GET'])
def get_last_value():
    if os.path.exists("sensor_data.txt"):
        with open("sensor_data.txt", "r") as file:
            line = file.readline().strip()
            print(line)
            if line:
                timestamp, temperature, alarm_triggered = line.split(',')
                return jsonify({
                    "timestamp": timestamp,
                    "last_value": float(temperature),
                    "alarm": alarm_triggered == 'True'
                }), 200
    return jsonify({"error": "No data available"}), 404

if __name__ == "__main__":
    app.run(port=5000)
