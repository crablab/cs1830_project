from SimpleGUICS2Pygame import simpleguics2pygame
from Classes.Camera import Camera
from Classes.Grass import Grass
from Classes.Particle import Particle
from Classes.Vector import Vector
import random
import copy

from Classes.Settings import PARTICLE_SIZE,CANVAS_WIDTH,CANVAS_HEIGHT
class Interaction:
    def __init__(self, particle, line):
        self.particle = particle
        self.line = line


def keyup(key):
    if key == simpleguics2pygame.KEY_MAP['r']:
        cam.zoomOut=False
    elif key == simpleguics2pygame.KEY_MAP['e']:
        cam.zoomIn=False
    elif key == simpleguics2pygame.KEY_MAP['right']:
        cam.moveRight=False
    elif key == simpleguics2pygame.KEY_MAP['left']:
        cam.moveLeft=False
    elif key == simpleguics2pygame.KEY_MAP['up']:
        cam.moveUp=False
    elif key == simpleguics2pygame.KEY_MAP['down']:
        cam.moveDown=False

def keydown(key):
    if key == simpleguics2pygame.KEY_MAP['r']:
        cam.zoomOut=True
    elif key == simpleguics2pygame.KEY_MAP['e']:
        if cam.dim.x>100 and cam.dim.y>100:
            cam.zoomIn=True
        else:
            cam.zoomIn=False
    elif key == simpleguics2pygame.KEY_MAP['right']:
        cam.moveRight = True
    elif key == simpleguics2pygame.KEY_MAP['left']:
        cam.moveLeft = True
    elif key == simpleguics2pygame.KEY_MAP['up']:
        cam.moveUp = True
    elif key == simpleguics2pygame.KEY_MAP['down']:
        cam.moveDown = True

grass_list=[]
x=0
for i in range(0,400):
    if i%20==0:
        x+=1
    g=Grass(Vector(x*200,(i%20)*200),random.randrange(0,4))
    grass_list.append(g)
    print(str(i%20)+", "+ str(x))


p = Particle(Vector(250, 250), Vector(random.randint(-3, 3), random.randint(-3, 3)), 0,PARTICLE_SIZE)
p1 = Particle(Vector(250, 100), Vector(random.randint(-3, 3), random.randint(-3, 3)), 0,PARTICLE_SIZE)
cam=Camera(Vector(250,250),Vector(1000,1000))

def draw(canvas):
    cam.zoom()
    cam.move()
    p1.update()
    p.update()
    pd1=copy.deepcopy(p1)
    pd=copy.deepcopy(p)
    pd1.transform(cam)
    pd.transform(cam)
    pd1.draw(canvas,cam.dim.x)
    pd.draw(canvas,cam.dim.x)
    for grass in grass_list:
        g1=copy.deepcopy(grass)
        g1.draw(canvas,cam)


frame = simpleguics2pygame.create_frame('A convex polygon domain', CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)

frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()
