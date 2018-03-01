import socket

class Sock:
    def __init__(self, host, port, queue_send, queue_recv):
        self.host = host
        self.port = port

        ##Queue.queue object
        self.queue_send = queue_send
        self.queue_recv = queue_recv

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind( (host, port) )

    def loopSend(self):
        while True:
            self.sock.sendall(self.queue_send.get())

    def loopRecv(self):
        self.sock.listen(1)

        while True:
            connection, client_address = self.sock.accept()
            try:
                while True:
                    data = connection.recv(1024)
                    if data:
                        self.queue.put(data)

                        ##Some kind of confirmation request
                    else:
                        break
            finally:
                connection.close()
