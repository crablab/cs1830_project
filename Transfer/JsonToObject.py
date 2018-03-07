#to read data into dictionary: data = json.loads(<json File>, object_hook=lambda d: namedtuple('<Object Name For Reference>', d.keys())(*d.values()))
from Classes.Camera import Camera
from Classes.Vector import Vector
from Classes.Objects import spriteDictionary
from Classes.Particle import Particle
from Classes.Player import Player
from Classes.Objects import moving_set, player_list
from Classes.Objects import cam
from collections import namedtuple
import json
import time
recieved_player_list=[]
recieved_particle_set=set()
### If exists local: update   if does not exist local: add      if boolean: remove  and on local then set boolean to False

def updateAllObjects():
    add_set=set()
    for remote in recieved_particle_set:
        existsLocal=False
        for local in moving_set:
            if local.idObject == remote.idObject:
                local.receive(remote)
                existsLocal = True
        if not existsLocal:
            add_set.add(remote)
    for a in add_set:
        moving_set.add(a)


    for local in moving_set:
        for remote in recieved_particle_set:
            if remote.remove==True and local.remove==False:
                local.remove=True

    for remote in recieved_player_list:
        existsLocal=False
        for local in player_list:
            if local.idObject == remote.idObject:
                local.receive(remote)
                existsLocal = True
        if not existsLocal:
            player_list.append(remote)

    for local in player_list:
        for remote in recieved_player_list:
            if remote.remove==True and local.remove==False:
                print("player removed")
                local.remove=True

    for remote in recieved_player_list:
        playerLoaded = False
        for local in recieved_player_list:
            if remote.idObject== local:
                playerLoaded=True
                local.receive(remote)
        if not playerLoaded:
            recieved_player_list.append(remote)
def getCam(arr):
    obj=Camera(Vector(arr.origin.x,arr.origin.y),Vector(arr.dim.x,arr.dim.y))
    cam.recieve(obj)

def particle(arr):
    obj = Particle(arr.updateSprite,Vector(arr.pos.x, arr.pos.y), Vector(arr.vel.x, arr.vel.y), arr.maxVel, arr.maxRange, arr.angle,
                   arr.radius, arr.spriteKey, spriteDictionary, arr.fps, arr.removeOnVelocity0,
                   arr.removeOnAnimationLoop)
    recieved_particle_set.add(obj)



def getPlayer(arr):
    obj = Player(Vector(arr.pos.x,arr.pos.y),Vector(arr.vel.x,arr.vel.y),arr.maxVel,arr.angle,arr.radius,arr.spriteKey,spriteDictionary,arr.spriteFps,arr.idPlayer)
    recieved_player_list.append(obj)


def getVector(arr):
    obj = Vector(arr.x,arr.y)
    return obj

def getObject(j):
    arr = json.loads(j, object_hook=lambda d: namedtuple('arr', d.keys())(*d.values()))
    if arr.idClass==1:
        return getCam(arr)
    elif arr.idClass==2:
        return particle(arr)
    elif arr.idClass==3:
        return getPlayer(arr)
    elif arr.idClass==4:
        return getVector(arr)
    else:
        return "error"

