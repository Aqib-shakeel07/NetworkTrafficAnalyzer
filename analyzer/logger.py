def log_packet_details(packet, file_path):
    """
    Logs details of a packet to a file.
    :param packet: Packet to log.
    :param file_path: File to write logs to.
    """
    with open(file_path, "a") as log_file:
        log_file.write(str(packet) + "\n")
