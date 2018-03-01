import socket, socketserver

class Sock:
    def __init__(self, queue_recv):
        self.recv_list = []
        
        ##Queue.queue object
        self.queue_recv = queue_recv

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind( (host, port) )

    def addRecv(self, host, port):
        self.queue_recv.append()

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

class RecvServer(socketserver.ThreadingTCPServer):

    def __init__(self, server_address, RequestHandlerClass, queue):
        SocketServer.ThreadingTCPServer.__init__(self, server_address, RequestHandlerClass)
        self.queue = queue

class RecvServerHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        self.server.queue.put(data)
