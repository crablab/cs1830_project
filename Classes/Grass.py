
import os

from Classes.Sprite import Sprite

USER_PATH = 'C:/Users/octav/Desktop/Programming/Games/cs1830/'

class Grass:
    cwd = os.getcwd()
    image1= Sprite(cwd +'/img/grass/grass18.jpg')
    image2 = Sprite(cwd +'/img/grass/grass17.jpg')
    image3= Sprite(cwd +'/img/grass/grass16.jpg')
    image4 = Sprite(cwd +'/img/grass/grass19.jpg')

    def __init__(self, pos,id):
        self.id=id
        self.pos=pos

    def draw(self,canvas,cam):
        print (self.id)
        if self.id==1:
            image=self.image1
        elif self.id==2:
            image=self.image2
        elif self.id==3:
            image=self.image3
        else:
            image=self.image4

        image.draw(canvas, cam,self.pos)

