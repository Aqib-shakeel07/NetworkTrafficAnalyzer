# traffic_analysis/alert.py
def alert(ip, message):
    """
    Sends an alert for suspicious traffic.
    Args:
        ip (str): IP address involved.
        message (str): Description of the suspicious activity.
    """
    print(f"ALERT: Suspicious activity detected from {ip}. {message}")
