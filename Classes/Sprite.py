from SimpleGUICS2Pygame import simpleguics2pygame
from Classes.Vector import Vector

import math
import json
class Sprite:
    def __init__(self, image):
        self.image = simpleguics2pygame.load_image(image)
        self.dim = Vector(self.image.get_width(),self.image.get_height())


    def draw(self, canvas, cam,pos,numberColumns,numberRows,row,column,):


        ratio=cam.dimCanv.copy().divideVector(cam.dim)
        imgDimTrans=self.dim.copy().divideVector(Vector(numberColumns,numberRows)).multiplyVector(ratio)
        canLoc=pos.getP()


        imageCenter=Vector((self.image.get_width()/numberColumns)*column-(self.image.get_width()/numberRows)/2,(self.image.get_height()/numberRows)*row-(self.image.get_height()/numberRows)/2)
        imageDimention=Vector(self.image.get_height()/numberRows,self.image.get_width()/numberColumns)

        canvas.draw_image(self.image,imageCenter.getP(),imageDimention.getP(), canLoc,imgDimTrans.getP())

