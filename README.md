# Basic Network Sniffer
Basic Network Sniffer is a Python-based cybersecurity project that captures and analyzes IP network packets using Scapy.

## Features
- Capture IP packets in real time
- Display source and destination IP addresses
- Identify TCP, UDP, and ICMP protocols
- Display source and destination ports for TCP and UDP
- Show packet size and capture timestamp
- Display a limited hexadecimal preview of available raw payload data
- Stop packet capture using Ctrl+C

## Technologies Used
- Python
- Scapy
- Npcap (Windows packet capture)

## Requirements
- Python 3
- Scapy
- Npcap on Windows

## Installation
1. Install Python 3.
2. Install Npcap from https://npcap.com/
3. Open a terminal in the project folder.
4. Install dependencies:
 - pip install -r requirements.txt

## Run the Project
Run the terminal with appropriate permissions and execute:
 - python sniffer.py

Press Ctrl+C to stop packet capture.

## Security and Privacy
Use this tool only on networks and devices you own or are authorized to analyze. Packet metadata and payload previews may contain sensitive information. This project displays only a limited hexadecimal payload preview.

## Learning Objectives
- Understand network packets and IP addressing
- Learn basic TCP, UDP, and ICMP identification
- Practice packet capture and network traffic analysis
- Understand basic cybersecurity monitoring

## Author: Purnima Gangwar.
## Thank you!

