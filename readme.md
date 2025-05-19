# Man-in-the-Middle (MITM) Attack Simulation

A Flask-based educational application that demonstrates how MITM attacks work and how HTTPS encryption prevents them.

## Overview

This application creates a simulated environment where users can:

- Send messages between two parties (Alice and Bob)
- Choose between unencrypted (HTTP) or encrypted (HTTPS) communication
- Observe how unencrypted traffic can be intercepted by an attacker
- Learn about MITM attacks and protection methods

## Features

- **Message Transmission**: Send messages between users with visual packet animation
- **Protocol Selection**: Toggle between HTTP and HTTPS to see the difference in security
- **Real-time Interception**: See which packets are intercepted in real-time
- **Visual Statistics**: Track message counts and interception rates by protocol
- **Educational Information**: Learn about MITM attacks and protection methods

## Requirements

- Python 3.6+
- Flask

## Installation

1. Clone this repository or download the files
2. Install dependencies:
   ```
   pip install flask
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000/`

## How It Works

This simulation demonstrates the following concepts:

### 1. HTTP vs HTTPS

- **HTTP**: Messages are sent in plaintext and can be intercepted by attackers
- **HTTPS**: Messages are encrypted and cannot be read even if intercepted

### 2. MITM Attack Mechanics

- The attacker positions themselves between the sender and receiver
- Unencrypted traffic is captured and read by the attacker
- Encrypted traffic remains secure even when intercepted

### 3. Security Statistics

- Real-time tracking of message counts by protocol
- Visualization of interception rates
- Security recommendations

## Educational Purpose

This simulation is provided for educational purposes only to demonstrate cybersecurity concepts. Performing actual MITM attacks without authorization is illegal and unethical.

## Extending the Simulation

This basic simulation could be extended to include:

- Certificate verification simulation for HTTPS
- More complex MITM attack techniques (DNS spoofing, ARP poisoning)
- Packet modification demonstrations
- More detailed network analysis