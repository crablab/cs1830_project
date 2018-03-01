import socket

class RecvSock:
    def __init__(self, host, port, queue):
        self.host = host
        self.port = port

        ##Queue.queue object
        self.queue = queue

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind( (host, port) )

    def startLoop(self):
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
