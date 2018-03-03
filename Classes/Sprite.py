from SimpleGUICS2Pygame import simpleguics2pygame
from Classes.Vector import Vector

import math
import json
class Sprite:
    def __init__(self, image):
        self.image = simpleguics2pygame.load_image(image)
        self.dim = Vector(self.image.get_width(),self.image.get_height())
        self.id=5

    def draw(self, canvas, cam, pos):

        ratio=cam.dimCanv.copy().divideVector(cam.dim)

        imgDim=self.dim.copy().multiplyVector(ratio)

        canLoc=pos.getP()

        canvas.draw_image(self.image,[self.image.get_width()//2,self.image.get_height()//2],[self.image.get_width(),self.image.get_width()], canLoc,imgDim.getP())


    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)
