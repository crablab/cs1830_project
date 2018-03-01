import socket

class SendSock:
    def __init__(self, host, port, queue):
        self.host = host
        self.port = port

        ##Queue.queue object
        self.queue = queue

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind( (host, port) )

    def startLoop(self):
        while True:
            self.sock.sendall(self.queue.get())
