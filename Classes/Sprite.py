from SimpleGUICS2Pygame import simpleguics2pygame
from Classes.Vector import Vector
from Classes.Settings import SPRITE_SIZE
import json
class Sprite:
    def __init__(self, image):
        self.image = simpleguics2pygame.load_image(image)
        self.dim = Vector(self.image.get_width()*SPRITE_SIZE,self.image.get_height()*SPRITE_SIZE)
        self.id=5

    def draw(self, canvas, cam, pos):
        # multiply ration on real screen
        imgDim=(self.dim.copy().divide(cam.dim.x).getP())
        imgCenter = tuple(ti/2 for ti in imgDim)
        canLoc=pos.getP()
        canvas.draw_image(self.image,[self.image.get_width()//2,self.image.get_height()//2],[self.image.get_width(),self.image.get_width()], canLoc,imgDim)


    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)
