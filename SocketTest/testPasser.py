import queue, threading
from sock import *

##Problem - only one socket can be open at any one time

class Passer:
    def __init__(self, host, port):
        self.q_recv = queue.Queue()
        self.q_send = queue.Queue()
        
        self.sock = Sock(host, port, self.q_send, self.q_recv)

    def start(self):
        self.threads = []
        
        self.threads.append( threading.Thread(name='send', target=self.sock.loopSend) )
        self.threads[-1].setDaemon(True)

        self.threads.append( threading.Thread(name='recv', target=self.sock.loopRecv) )
        self.threads[-1].setDaemon(True)

        self.threads.append( threading.Thread(name='middle', target=self.handle_message) )
        self.threads[-1].setDaemon(True)

        for thread in self.threads:
            thread.start()

    def handle_message(self):
        while True:
            date = self.q_recv.get()
            print(data)
            self.q_send.put(date)
