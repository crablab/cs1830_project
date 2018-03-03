
import os
import json
from Classes.Sprite import Sprite
USER_PATH = 'C:/Users/octav/Desktop/Programming/Games/cs1830/'

class Grass:
    cwd = os.getcwd()
    image1= Sprite(cwd +'/img/grass/grass18.jpg')
    image2 = Sprite(cwd +'/img/grass/grass17.jpg')
    image3= Sprite(cwd +'/img/grass/grass16.jpg')
    image4 = Sprite(cwd +'/img/grass/grass19.jpg')

    def __init__(self, pos,idP):
        self.idP=idP
        self.pos=pos
        self.id=2
        self.width=0

    def draw(self,canvas,cam):
        if self.idP==1:
            image=self.image1
        elif self.idP==2:
            image=self.image2
        elif self.idP==3:
            image=self.image3
        else:
            image=self.image4

        image.draw(canvas,cam,self.pos)

    def transform(self,cam):
        self.width=cam.dim.getX()


        self.pos.subtract(cam.origin)
        ratio=cam.dimCanv.copy().divideVector(cam.dim)
        self.pos.multiplyVector(ratio)
        self.pos.add(cam.dimCanv.copy().divide(2))




    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)