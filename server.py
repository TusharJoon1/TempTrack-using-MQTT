from flask import Flask, jsonify, send_from_directory
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/sensor/last', methods=['GET'])
def get_last_value():
    logging.info("Received request for latest sensor value")
    file_path = "sensor_data.txt"
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()  # Get the last line
                    logging.info(f"Read last line from file: {last_line}")
                    if last_line:
                        timestamp, temperature, alarm_triggered = last_line.split(',')
                        return jsonify({
                            "timestamp": timestamp,
                            "last_value": float(temperature),
                            "alarm": alarm_triggered == 'True'
                        }), 200
        except Exception as e:
            logging.error(f"Error reading file: {e}")
            return jsonify({"error": "Error reading data"}), 500
    else:
        logging.warning(f"File {file_path} does not exist")
    return jsonify({"error": "No data available"}), 404

if __name__ == "__main__":
    app.run(port=5000)
