import WinTmp
import threading
import time
import logging
from flask import Flask, jsonify
import subprocess
import sys
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('temperature_server.log', mode='w'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Global variables to store temperatures
current_temperatures = {
    'cpu': None,
    'gpu': None
}

def update_temperatures():
    """Background thread to continuously update temperatures"""
    global current_temperatures
    while True:
        try:
            # Retrieve CPU temperature
            cpu_temps = WinTmp.CPU_Temps()
            current_temperatures['cpu'] = cpu_temps[1] if len(cpu_temps) > 1 else None
            
            # Retrieve GPU temperature
            gpu_temps = WinTmp.GPU_Temps()
            current_temperatures['gpu'] = gpu_temps[0] if gpu_temps else None
            
            logging.info(f"Updated temperatures: {current_temperatures}")
            
            # Wait for 2 seconds before next update
            time.sleep(2)
        except Exception as e:
            logging.error(f"Error updating temperatures: {e}")
            time.sleep(2)  # Wait 2 seconds on error to prevent rapid error logging

# Flask application
app = Flask(__name__)

@app.route('/temperatures')
def get_temperatures():
    """Endpoint to retrieve current temperatures"""
    return jsonify(current_temperatures)

def run_flask_app():
    """Run Flask app"""
    app.run(host='0.0.0.0', port=5000, debug=False)

def main():
    # Start temperature update thread
    temp_thread = threading.Thread(target=update_temperatures, daemon=True)
    temp_thread.start()
    
    # Start Flask web server
    run_flask_app()

if __name__ == "__main__":
    main()
