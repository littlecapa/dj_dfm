import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This doesn't need to be a reachable address, just something outside your local network
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception as e:
        print.error(e)
        local_ip = "127.0.0.1"
    finally:
        s.close()
    return local_ip