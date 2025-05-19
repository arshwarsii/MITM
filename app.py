from flask import Flask, render_template, request, jsonify, session
import os
import json
import time
import random
import string
import secrets
import socket
from datetime import datetime

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Function to find available port
def find_available_port(start_port=5000):
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                return port
            except OSError:
                port += 1

# Simulated network traffic data
network_data = []
intercepted_data = []

# Generate random hex for packet IDs
def random_hex(length=8):
    return ''.join(random.choice(string.hexdigits) for _ in range(length))

# Simulated encryption/decryption
def encrypt_message(message):
    encrypted = ""
    for char in message:
        # Simple substitution cipher for demonstration
        encrypted += chr((ord(char) + 5) % 0x10FFFF)
    return encrypted

def decrypt_message(encrypted):
    decrypted = ""
    for char in encrypted:
        decrypted += chr((ord(char) - 5) % 0x10FFFF)
    return decrypted

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender = data.get('sender')
    receiver = data.get('receiver')
    message = data.get('message')
    use_encryption = data.get('encryption', False)
    
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    packet_id = random_hex()
    
    # Original message
    original_message = message
    
    # If encryption is enabled
    if use_encryption:
        message = encrypt_message(message)
    
    # Create packet details
    packet = {
        "id": packet_id,
        "timestamp": timestamp,
        "sender": sender,
        "receiver": receiver,
        "data": message,
        "encrypted": use_encryption,
        "protocol": "HTTPS" if use_encryption else "HTTP"
    }
    
    # Simulate network delay
    time.sleep(0.3)
    
    # Add to network data
    network_data.append(packet)
    
    # Simulate MITM attack (only intercepts unencrypted)
    if not use_encryption:
        intercepted = packet.copy()
        intercepted["intercepted"] = True
        intercepted_data.append(intercepted)
    
    return jsonify({
        "success": True, 
        "message": "Message sent", 
        "packet": packet,
        "original": original_message
    })

@app.route('/get_network_data')
def get_network_data():
    return jsonify(network_data[-10:] if network_data else [])

@app.route('/get_intercepted_data')
def get_intercepted_data():
    return jsonify(intercepted_data[-10:] if intercepted_data else [])

@app.route('/reset_simulation', methods=['POST'])
def reset_simulation():
    global network_data, intercepted_data
    network_data = []
    intercepted_data = []
    return jsonify({"success": True})

if __name__ == '__main__':
    # Find available port starting from 5500
    port = find_available_port(5500)
    print(f"Running on http://127.0.0.1:{port}")
    app.run(host='127.0.0.1', port=port, debug=True)