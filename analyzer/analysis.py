def analyze_packets(packets, malicious_ips=None, output_file=None):
    """
    Analyzes packets and detects malicious IPs.
    :param packets: List of captured packets.
    :param malicious_ips: List of malicious IPs to check against.
    :param output_file: File to save analysis logs.
    """
    if not malicious_ips:
        malicious_ips = []
    
    if output_file:
        log = open(output_file, "w")
    else:
        log = None

    for packet in packets:
        src_ip = packet[1].src if hasattr(packet[1], "src") else "Unknown"
        print(f"Packet from {src_ip}")
        
        if log:
            log.write(f"Packet from {src_ip}\n")
        
        if src_ip in malicious_ips:
            alert = f"ALERT: Malicious IP detected: {src_ip}"
            print(alert)
            if log:
                log.write(alert + "\n")

    if log:
        log.close()
