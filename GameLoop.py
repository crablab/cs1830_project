#    mmm   mmmm  mmm     mmmm   mmmm   mmmm
#  m"   " #"   "   #    #    # "   "# m"  "m
#  #      "#mmm    #    "mmmm"   mmm" #  m #
#  #          "#   #    #   "#     "# #    #
#   "mmm" "mmm#" mm#mm  "#mmm" "mmm#"  #mm#
# Networking class


import queue, threading, time, pycurl, json, io
from flask import Flask, request, Response

from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_fps
import pygame
import random
import copy
import time
from collections import namedtuple

import json

from Classes.Camera import Camera
from Classes.Vector import Vector
from Classes.Player import Player

from Classes.KeyHandler import keydown, keyup
from Classes.ClickHandler import checkClick

from Classes.Settings import *
from Classes.Objects import cam, player_list, particle_set_middle,particle_set_top,particle_set_bottom, spriteDictionary

#NETWORKING

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
        #get the dictionary of the message
        jsonData = request.get_json(force=True)
        #seperate into the queue
        for value in jsonData:
            server.recieved.put(value)
        #set the body to empty
        body = json.dumps([])

        while(not server.send.empty()):
            data = json.loads(body)
            data.append(server.send.get())
            body = json.dumps(data)
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

        #start the curl stuff in a thread we can control
        self.t = threading.Thread(target=self.makeRequest)
        self.t.start()

    def makeRequest(self):
        while(1 == 1):
            #only start a curl if we actually have something to send
            if(not self.send.empty()):
                c = pycurl.Curl()
                storage = io.BytesIO()

                c.setopt(c.URL, self.peer)
                c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
                c.setopt(pycurl.POST, 1)
                c.setopt(pycurl.PORT, self.port)
                c.setopt(c.WRITEFUNCTION, storage.write)

                #set the body to empty
                body = json.dumps([])

                while(not self.send.empty()):
                    data = json.loads(body)
                    data.append(self.send.get())
                    body = json.dumps(data)

                c.setopt(pycurl.POSTFIELDS, body)

                c.perform()
                print(c.getinfo(pycurl.RESPONSE_CODE))
                c.close()

                #get the json
                content = json.loads(storage.getvalue().decode('UTF-8'))
                print(content)
                for value in content:
                    self.recieved.put(value)

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

#-----START----GAME----CLOCK
fps = simplegui_lib_fps.FPS()
fps.start()
startTime = time.time()


# # -----INTERACTIONS?
# class Interaction:
#     def __init__(self, particle, line):
#         self.particle = particle
#         self.line = line
#

##-----NETWORKING
if(CONFIG_TYPE == "server"):
    com = server()
elif(CONFIG_TYPE == "client"):
    com = client(CLIENT_IP, 5027)

#--------------GAME-----LOOP
def draw(canvas):
    com.send.put(cam.encode())


#-----CAM---UPDATE---
    cam.zoom()
    cam.move()
#----CLICK---HANDLER---
    checkClick()

#-----OBJECT---UPDATES-----
    for player in player_list:
        player.update()
    for p in particle_set_top:
        p.update()
        p.spriteSheet.update()
    for p in particle_set_middle:
        p.update()
        p.spriteSheet.update()
    for p in particle_set_bottom:
        p.update()
        p.spriteSheet.update()


#  --------DRAW---OBJECTS---BY---LAYER---PRIORITY

    for pbot in particle_set_bottom:
        pbot.update()
        pbot.draw(canvas,cam,spriteDictionary)

    for pmid in particle_set_middle:
        pmid.update()
        pmid.draw(canvas, cam, spriteDictionary)

    for ptop in particle_set_top:
        ptop.update()
        ptop.draw(canvas, cam, spriteDictionary)



    for player in player_list:

        player.draw(canvas, cam, spriteDictionary)


    fps.draw_fct(canvas)
#--------COLLECT----MARKED---OBJECTS------------
    removal_set=set()

    for particle in particle_set_top:
        if particle.pos==particle.nextPos and particle.removeOnVelocity0:
            removal_set.add(particle)
        if particle.spriteSheet.hasLooped and particle.removeOnAnimationLoop:
            removal_set.add(particle)
    particle_set_top.difference_update(removal_set)
    removal_set.clear()

    for particle in particle_set_middle:
        if particle.pos==particle.nextPos and particle.removeOnVelocity0:
            removal_set.add(particle)
        if particle.spriteSheet.hasLooped and particle.removeOnAnimationLoop:
            removal_set.add(particle)
    particle_set_middle.difference_update(removal_set)
    removal_set.clear()

    for particle in particle_set_bottom:
        if particle.pos==particle.nextPos and particle.removeOnVelocity0:
            removal_set.add(particle)
        if particle.spriteSheet.hasLooped and particle.removeOnAnimationLoop:
            removal_set.add(particle)
    particle_set_bottom.difference_update(removal_set)
    removal_set.clear()



frame = simpleguics2pygame.create_frame('Game', CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()