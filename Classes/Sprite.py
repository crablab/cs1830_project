from SimpleGUICS2Pygame import simpleguics2pygame
from Classes.Vector import Vector
from Classes.Settings import SPRITE_SIZE
class Sprite:
    def __init__(self, image):
        self.image = simpleguics2pygame.load_image(image)

        self.dim = Vector(self.image.get_width()*SPRITE_SIZE,self.image.get_height()*SPRITE_SIZE)


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

