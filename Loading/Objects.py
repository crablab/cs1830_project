import configparser
from Classes.Middle.Particle import Particle
from Classes.Base.Vector import Vector
from Classes.Super.Camera import Camera
config = configparser.ConfigParser()

# Open file as writeable
config.read_file(open('Classes/config'))


import os
import uuid

# ---------------------ANY SETS/LISTS-----------------------
block=Particle(False,Vector(0,0),Vector(0,0),0,Vector(0,0),1000,10000,0,10,'',{},0,True,True,'',0,0,0,0,0,0)
cam = Camera(Vector(0,0),Vector(100,100))
# -----------------------SOUNDS------------------



