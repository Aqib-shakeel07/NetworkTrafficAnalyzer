# traffic_analysis/analyze.py
from scapy.all import rdpcap

def analyze_traffic(file_path="captured_traffic.pcap"):
    """
    Analyzes captured traffic from a pcap file.
    Args:
        file_path (str): Path to the pcap file.
    """
    packets = rdpcap(file_path)
    for packet in packets:
        if packet.haslayer('IP'):
            print(f"Source: {packet['IP'].src}, Destination: {packet['IP'].dst}")
