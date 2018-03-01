import socket
import time
import threading
import queue
import random

class coms_client:

    def __init__(self, ip):
        self.address = ip
        self.go = 1

    def connect(self):
        try: 
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.address, 7720))
        except ConnectionRefusedError: 
            return False
        return True

    def msg_send(self, msg):
        self.s.sendall(msg.encode('utf-8'))

    def msg_recv(self, buffer=1024):
        return self.s.recv(buffer)

    def start(self):
        self.send_queue = queue.Queue()
        self.recieved_queue = queue.Queue()
        self.send_thread = threading.Thread(None, self.run_send)
        self.rec_thread = threading.Thread(None, self.run_rec)
        self.send_thread.start()
        self.rec_thread.start()

    def run_send(self):
        while self.go == 1:
            if(not self.send_queue.empty()):      
                web.msg_send(self.send_queue.get())

    def run_rec(self):
        while self.go == 1:
            self.recieved_queue.put(web.msg_recv(1024))
            print('> Data from ' + str(web.s.getpeername()))
                

web = coms_client("localhost")
if(web.connect()): 

    web.start()

    while(1==1):
        time.sleep(1)
        web.send_queue.put('{"id": 0,"pos": {"x": 200,"y": 0}}')

else:
    print("Connection to peer failed")