# traffic_analysis/capture.py
from scapy.all import sniff, wrpcap

def start_capture(packet_count=50, output_file="captured_traffic.pcap"):
    """
    Captures network traffic and saves to a file.
    Args:
        packet_count (int): Number of packets to capture.
        output_file (str): Name of the output file to save packets.
    """
    print(f"Capturing {packet_count} packets...")
    packets = sniff(count=packet_count)
    wrpcap(output_file, packets)
    print(f"Captured packets saved to {output_file}")
