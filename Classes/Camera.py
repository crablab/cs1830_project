from Classes.Vector import Vector
from Classes.Settings import CAM_MAX_MOVE_DIST

import configparser
config = configparser.ConfigParser()
config.read_file(open('Classes/config'))
import json
import uuid
import time
class Camera:
    def __init__(self, origin, dim):
        self.idClass = 1
        self.idObject = uuid.uuid4()

        self.origin = origin
        self.dim = dim
        self.dimCanv=Vector(int(config['CANVAS']['CANVAS_WIDTH']),int(config['CANVAS']['CANVAS_HEIGHT']))
        self.zoomIn=False
        self.zoomOut=False
        self.moveLeft=False
        self.moveRight=False
        self.moveUp=False
        self.moveDown=False
        self.maxMoveDist=CAM_MAX_MOVE_DIST
        self.maxZoomDist=int(config['CAMERA']['CAM_MAX_ZOOM_DIST'])
        self.minZoomDist = int(config['CAMERA']['CAM_MIN_ZOOM_DIST'])
        self.moveSensitivity=int(config['CAMERA']['CAM_MOVE_SENSITIVITY'])
        self.zoomSensitivity=float(config['CAMERA']['CAM_ZOOM_SENSITIVITY'])
        self.currentTime=time.time()


    def move(self,playerId,player_list):
        for player in player_list:
            if playerId == player.idObject:
                pos = player.particle.pos.copy()
        self.currentTime=time.time()

        if self.moveUp==True and pos.getY()-self.origin.getY()<self.maxMoveDist:
            self.origin.add(Vector(0,-self.moveSensitivity))
        if self.moveDown==True and self.origin.getY()-pos.getY()<pos.getY()+self.maxMoveDist:
            self.origin.add(Vector(0,self.moveSensitivity))

        if self.moveLeft == True:
            self.origin.add(Vector(-self.moveSensitivity,0))
        if self.moveRight == True:
            self.origin.add(Vector(self.moveSensitivity,0))


    def zoom(self):
        if self.zoomOut == True and self.dim.x<self.maxZoomDist and self.dim.y<self.maxZoomDist:
            self.dim.add(self.dim.copy().multiply(self.zoomSensitivity))

        if self.zoomIn == True and self.dim.x>self.minZoomDist and self.dim.y>self.minZoomDist:

                self.dim.add(self.dim.copy().multiply(-self.zoomSensitivity))

    def ratioToCam(self):
        return(self.dimCanv.copy().divideVector(self.dim).getX())

    def ratioToCanv(self):
        return (self.dim.copy().divideVector(self.dimCanv).getX())

    def get(self):
        return(self.origin, self.dim.x)

    def recieve(self,other):
        self.currentTime=other.currentTime
        self.origin=other.origin
        self.dim=other.dim
