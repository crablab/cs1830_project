
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



        # #get Distance
        # dist=self.copy()
        # print("distance: " + str(dist))
        # #get ratio
        # ratio=camDim.divideVector(canvDim)
        # print("ratio: "+str(ratio))
        # #ratio*coords
        # self.multiplyVector(ratio)
        # print("mult ratio: " + str(self.getP()))
        #
        # #take away origin to adjust
        # self.add(cam.origin)
        # print("subtract : " + str(self.getP()))
        #
        #
        # #get Distance
        # dist=self.pos.copy()
        # dist.subtract(cam.origin)
        # #get ratio
        # ratio=dist.divideVector(cam.dim.copy().divide(2))
        # #multiply ration on real screen
        # self.pos=ratio.multiplyVector(cam.dimCanv.copy().divide(2))
        # self.pos.add(cam.dimCanv.copy().divide(2))



        self.pos.subtract(cam.origin)
        ratio=cam.dimCanv.copy().divideVector(cam.dim)
        self.pos.multiplyVector(ratio)
        self.pos.add(cam.dimCanv.copy().divide(2))




    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys =True, indent=4)