from SimpleGUICS2Pygame import simpleguics2pygame, simplegui_lib_keys, simplegui_lib_fps
from Vector import Vector
USER_PATH = 'C:/Users/octav/Desktop/Programming/Games/cs1830/'
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
#polygons
ParticleSize=2500
#Sprites:
SpriteSize=200
#CAMERA
CamMinDist=200
CAM_SENSITIVITY=5
class Sprite:
    def __init__(self, image):
        self.image = simpleguics2pygame.load_image(image)

        self.dim = Vector(self.image.get_width()*SpriteSize,self.image.get_height()*SpriteSize)


    def draw(self, canvas, cam, pos):
        # get Distance
        dist = pos.copy()
        dist.subtract(cam.origin)
        # get ratio
        ratio = dist.divideVector(cam.dim.copy().divide(2))
        # multiply ration on real screen
        pos = ratio.multiplyVector(cam.dimCanv.copy().divide(2))
        pos.add(cam.dimCanv.copy().divide(2))
     
        imgDim=(self.dim.copy().divide(cam.dim.x).getP())
        imgCenter = tuple(ti/2 for ti in imgDim)
        canLoc=pos.getP()
        canvas.draw_image(self.image,[self.image.get_width()//2,self.image.get_height()//2],[self.image.get_width(),self.image.get_width()], canLoc,imgDim)

