import os
import socket


def keep_alive(url, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", int(port)))
    s.listen(5)

    os.system(f"ping -i 30 {url}")
