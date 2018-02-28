import socket
import sys

"""
Simple example to work on
"""

class MySock:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.sock.connect((host, port))

    def close(self):
        self.sock.close()

    def sendStr(self, msgStr):
        self.send(bytes(msgStr + "\n","utf-8"))

    def send(self, toSend):
        self.sock.sendall(toSend)

    def recieve(self):
        recieved = str(self.sock.recv(1024), "utf-8")
        return recieved

s = MySock()
s.connect('localhost',9999)
s.sendStr('ABC')
print(s.recieve())


        
 

