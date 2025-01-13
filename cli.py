import argparse
from analyzer.capture import capture_packets
from analyzer.analysis import analyze_packets

def main():
    parser = argparse.ArgumentParser(description="Network Traffic Analyzer")
    parser.add_argument(
        "-c", "--count", type=int, default=50,
        help="Number of packets to capture (default: 50)"
    )
    parser.add_argument(
        "-m", "--malicious", type=str, nargs="*",
        help="List of malicious IPs to monitor"
    )
    parser.add_argument(
        "-o", "--output", type=str, default="traffic_log.txt",
        help="File to save analysis logs"
    )
    args = parser.parse_args()

    print("[*] Capturing packets...")
    packets = capture_packets(args.count)
    print("[*] Analyzing packets...")
    analyze_packets(packets, args.malicious, args.output)

if __name__ == "__main__":
    main()
