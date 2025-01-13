# run.py
import json
from Traffic_analysis.capture import start_capture
from Traffic_analysis.analyze import analyze_traffic
from Traffic_analysis.alert import alert

# Load configuration
with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)

# Capture traffic
start_capture(packet_count=config['packet_capture_count'])

# Analyze captured traffic
analyze_traffic(file_path="captured_traffic.pcap")

# Check for malicious IPs (alert functionality)
malicious_ips = config['malicious_ips']
# Check if any malicious IP is in the traffic
# For simplicity, let's pretend we check all packets for malicious IPs (use real analysis logic)
for ip in malicious_ips:
    alert(ip, "Known malicious IP detected!")

