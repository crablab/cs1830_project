from Classes.Grass import Grass
from Classes.Vector import Vector
from Classes.Particle import Particle
from Classes.Player import Player
from Classes.Camera import Camera
from Classes.Settings import CANVAS_HEIGHT,CANVAS_WIDTH
from Classes.Mouse import Mouse
import random

#simple gui to Pygame click adjustment Vector:
adjustment=Vector(250,25)
#declare sets/lists
grass_list = []
particle_set = set()
player_list = []

#initiate statics
x = 0
for i in range(0, 400):
    if i % 20 == 0:
        x += 1
    g = Grass(Vector(x * 500, (i % 20) * 500), random.randrange(0, 4))
    grass_list.append(g)

#initiate non-statics
cam  = Camera(Vector(250, 250), Vector(CANVAS_WIDTH, CANVAS_HEIGHT))
player = Player(Vector(250, 250), Vector(0, 0), 0, 1)
player_list.append(player)
mouse=Mouse()
