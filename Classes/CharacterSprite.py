import os
import json
from Classes.Sprite import Sprite

USER_PATH = 'C:/Users/octav/Desktop/Programming/Games/cs1830/'


class Character:
    cwd = os.getcwd()
    image1 = Sprite(cwd + '/img/character/elf/demo.jpg')

    def __init__(self, pos, idP):
        self.idP = idP
        self.pos = pos

        self.column = 1
        self.row = 1
        self.numRows = 1
        self.numColumns = 1
        self.numPictures = 1

    def draw(self, canvas, cam,pos):
        self.pos=pos
        image = self.image1
        # if self.idP==1:
        #     image=self.image1
        # elif self.idP==2:
        #     image=self.image2
        # elif self.idP==3:
        #     image=self.image3
        # else:
        #     image=self.image4

        image.draw(canvas, cam,self.pos, self.numColumns, self.numRows, self.row, self.column)

    def setRow(self, row, columnStart, numPictures, numColumns,numRows):
        self.column = columnStart
        self.row = row
        self.numPictures = numPictures
        self.numColumns = numColumns
        self.numRows=numRows

    def update(self):
        self.column += 1
        self.column = self.column % self.numPictures
        if self.column == 0:
            self.column += 1

    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
