import socket
import time
import threading

class coms_client:

    def __init__(self, ip):
        self.address = ip
        self.go = 1

    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.address, 7720))

    def msg_send(self, msg):
        self.s.sendall(msg.encode('utf-8'))

    def msg_recv(self, buffer):
        return self.s.recv(buffer)

    def run(self):
        while self.go == 1:
            web.msg_send("Test123")

            time.sleep(1)

            data = web.msg_recv(1024)

            print('Received', repr(data))



web = coms_client("localhost")
web.connect()

thr = threading.Thread(None, web.run)
thr.start()