#    mmm   mmmm  mmm     mmmm   mmmm   mmmm 
#  m"   " #"   "   #    #    # "   "# m"  "m
#  #      "#mmm    #    "mmmm"   mmm" #  m #
#  #          "#   #    #   "#     "# #    #
#   "mmm" "mmm#" mm#mm  "#mmm" "mmm#"  #mm# 
# Networking class
                                          

import queue, threading, time, pycurl, json, io

from Classes.Settings import CONFIG_TYPE,CLIENT_IP, LOGGING, LOGGING_LEVEL, DEVELOPER_OPTIONS
from flask import Flask, request, Response
from Transfer.JsonToObject import getObject
import time, sys

class FlaskAppWrapper(object):
    app = None

    def __init__(self, name, inqueue):
        self.app = Flask(name)
        print("Passing inqueue to Flask")
        self.iq = inqueue

    def run(self):
        print("Flask starting...")
        self.app.run("", 5027)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=["POST"])

    def action():
        server = com
        #get the dictionary of the message
        jsonData = request.get_json(force=True)
        #if(LOGGING and LOGGING_LEVEL == "high"): print(jsonData)
        #seperate into the queue
        for value in jsonData:
            server.recieved.put(json.dumps(value))
        #set the body to empty
        body = json.dumps([])

        if(LOGGING and LOGGING_LEVEL == "high"): print("Amalgmating response at " + str(time.time()))
        while server.send.empty():
            data = json.loads(body)
            data.append(server.send.get())
            body = json.dumps(data)
        if(LOGGING and LOGGING_LEVEL == "high"): print("Sending response " + str(time.time()))
        return Response(body, status=200, headers={})

class server:

    def __init__(self):

        print("Starting server...")
        #init queues
        self.recieved = queue.Queue()
        self.send = queue.Queue()
        self.a = FlaskAppWrapper('wrap', self.recieved)
        self.a.add_endpoint(endpoint='/', endpoint_name='root', handler=FlaskAppWrapper.action)

        #start flask in a thread we can control
        self.t = threading.Thread(target=self.a.run)
        self.t.start()

class client:
    def __init__(self, peer, port):
        print("Starting client...")
        self.peer = peer 
        self.port = port
        #init queues
        self.recieved = queue.Queue()
        self.send = queue.Queue()
        if(LOGGING): print("Threading cURL at " + str(time.time()))
        #start the curl stuff in a thread we can control
        self.t = threading.Thread(target=self.makeRequest)
        self.t.start()

    def makeRequest(self):
        while(1 == 1):
            #only start a curl if we actually have something to send
            if(not self.send.empty()):
                if(LOGGING and LOGGING_LEVEL == "high"): print("Starting cURL at " + str(time.time()))
                
                c = pycurl.Curl()
                storage = io.BytesIO()

                c.setopt(c.URL, self.peer)
                c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
                c.setopt(pycurl.POST, 1)
                c.setopt(pycurl.PORT, self.port)
                c.setopt(c.WRITEFUNCTION, storage.write)

                #set the body to empty
                body = json.dumps([])
                if(LOGGING and LOGGING_LEVEL == "high"): print("Amalgmating cURL at " + str(time.time()))
                while(not self.send.empty()):
                    data = json.loads(body)
                    data.append(self.send.get())
                    body = json.dumps(data)

                c.setopt(pycurl.POSTFIELDS, body)
                if(LOGGING and LOGGING_LEVEL == "high"): print("Making cURL at " + str(time.time()))
                c.perform()
                if(LOGGING and LOGGING_LEVEL == "high"): print(c.getinfo(pycurl.RESPONSE_CODE))
                c.close()

                #get the json
                content = json.loads(storage.getvalue().decode('UTF-8'))
                
                if(LOGGING and LOGGING_LEVEL == "high"): print("Pushing to queue at " + str(time.time()))
                for value in content:
                    value = json.dumps(value)
                    #if(LOGGING and LOGGING_LEVEL == "high"): print(value)
                    self.recieved.put(value)

#Override settings when testing (to make it easier to run multiple instances)
#if(DEVELOPER_OPTIONS and sys.argv[1]): CONFIG_TYPE = sys.argv[1]

if (CONFIG_TYPE == "server"):
    com = server()
elif (CONFIG_TYPE == "client"):
    com = client(CLIENT_IP, 5027)

currentTime=time.time()
oldTime=time.time()

def ping():
    com.send.put({'idClass': 0})
def communicate(object):
    com.send.put(object.encode())

def recieve():
    print("the sise of the qeue is:"+str(com.recieved.qsize()))

    while not com.recieved.empty():

        print("waiting")
        obj=com.recieved.get()
        print(obj)
        if(LOGGING): print("Pulling from queue at " + str(time.time()))

        getObject(obj)



