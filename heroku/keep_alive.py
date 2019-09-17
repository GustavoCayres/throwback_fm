import socket
from time import sleep

from multiping import MultiPing


def keep_alive(url, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", int(port)))
    s.listen(5)

    mp = MultiPing([url])
    while True:
        sleep(30000)
        mp.send()
        responses, no_responses = mp.receive(10)
        print(responses)
