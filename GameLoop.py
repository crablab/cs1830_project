from SimpleGUICS2Pygame import simpleguics2pygame
from Classes.Camera import Camera
from Classes.Grass import Grass
from Classes.Particle import Particle
from Classes.Vector import Vector
from Classes.Player import Player
from collections import namedtuple
from Classes.Settings import CANVAS_WIDTH, CANVAS_HEIGHT
from Transfer import JsonToObject
import json
import random
import copy
import time
from Classes.Settings import PARTICLE_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT


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
cam = Camera(Vector(250, 250), Vector(CANVAS_WIDTH, CANVAS_HEIGHT))
player = Player(Vector(250, 250), Vector(0, 0), 0, 1)
player_list.append(player)


#interactions (if required later):
class Interaction:
    def __init__(self, particle, line):
        self.particle = particle
        self.line = line

# User input
def mouseClick(pos):
    #get position transform and then apply to current player and send.
    if pos != pos[-1]:
        for player in player_list:
            point=Vector(pos[0],pos[1])
            point.transform(cam)
            player.move(point)
    print(cam.dimCanv)
    print(cam.dim)

def keyup(key):
    if key == simpleguics2pygame.KEY_MAP['r']:
        cam.zoomOut = False
    elif key == simpleguics2pygame.KEY_MAP['e']:
        cam.zoomIn = False
    elif key == simpleguics2pygame.KEY_MAP['right']:
        cam.moveRight = False
    elif key == simpleguics2pygame.KEY_MAP['left']:
        cam.moveLeft = False
    elif key == simpleguics2pygame.KEY_MAP['up']:
        cam.moveUp = False
    elif key == simpleguics2pygame.KEY_MAP['down']:
        cam.moveDown = False


def keydown(key):
    if key == simpleguics2pygame.KEY_MAP['r']:
        cam.zoomOut = True
    elif key == simpleguics2pygame.KEY_MAP['e']:
        if cam.dim.x > 100 and cam.dim.y > 100:
            cam.zoomIn = True
        else:
            cam.zoomIn = False
    elif key == simpleguics2pygame.KEY_MAP['right']:
        cam.moveRight = True
    elif key == simpleguics2pygame.KEY_MAP['left']:
        cam.moveLeft = True
    elif key == simpleguics2pygame.KEY_MAP['up']:
        cam.moveUp = True
    elif key == simpleguics2pygame.KEY_MAP['down']:
        cam.moveDown = True

#Game loop
def draw(canvas):
    # adjust camera
    cam.zoom()
    cam.move()

    # updates

    for player in player_list:
        player.update()
        cam.origin=player.pos.copy()

    # copy and draw Background Sprites/objects
    for grass in grass_list:
        g1 = copy.deepcopy(grass)
        g1.transform(cam)
        g1.draw(canvas,cam)

    # copy and draw Forground Sprites/objects
    for player in player_list:
        p = copy.deepcopy(player)
        p.transform(cam)
        p.draw(canvas)



    # if (g1.pos.getY()<CANVAS_HEIGHT+100000/cam.dim.getX() and g1.pos.getY()>-100000/cam.dim.getX()) and (g1.pos.getX()>-100000/cam.dim.getX() and g1.pos.getX()<CANVAS_WIDTH+100000/cam.dim.getX()):
    #     print(cam.dim.getX())
    #     g2=(g1.encode())
    #     g3=JsonToObject.GetObject(g2)
    #     g3.draw(canvas,cam)


frame = simpleguics2pygame.create_frame('A convex polygon domain', CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(mouseClick)

frame.start()
