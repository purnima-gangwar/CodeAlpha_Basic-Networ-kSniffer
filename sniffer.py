from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

packet_count = 0

def analyze_packet(packet):
    global packet_count

    if IP not in packet:
        return

    packet_count += 1

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    protocol = "Other"
    source_port = "N/A"
    destination_port = "N/A"

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport
    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport
    elif ICMP in packet:
        protocol = "ICMP"

    print("\n" + "=" * 45)
    print(f"Packet Number : {packet_count}")
    print(f"Time          : {datetime.now().strftime('%H:%M:%S')}")
    print(f"Source IP     : {source_ip}")
    print(f"Destination IP: {destination_ip}")
    print(f"Protocol      : {protocol}")
    print(f"Source Port   : {source_port}")
    print(f"Destination Port: {destination_port}")
    print(f"Packet Size   : {len(packet)} bytes")

    if Raw in packet:
        payload_preview = bytes(packet[Raw].load)[:20]
        print(f"Payload Preview (hex): {payload_preview.hex(' ')}")
    else:
        print("Payload Preview: No raw payload layer")

def start_sniffer():
    print("===================================")
    print("     BASIC NETWORK SNIFFER")
    print("===================================")
    print("Capturing IP packets...")
    print("Press Ctrl+C to stop.\n")

    try:
        sniff(
            filter="ip",
            prn=analyze_packet,
            store=False
        )
    except KeyboardInterrupt:
        print("\nSniffer stopped.")
        print(f"Total packets analyzed: {packet_count}")

if __name__ == "__main__":
    start_sniffer()
