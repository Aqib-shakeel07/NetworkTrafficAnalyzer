from scapy.all import sniff

def capture_packets(count):
    """
    Captures network packets.
    :param count: Number of packets to capture.
    :return: List of captured packets.
    """
    packets = sniff(count=count)
    return packets
