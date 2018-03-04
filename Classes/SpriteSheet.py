import os
import json
from Classes.SpriteAnimator import SpriteAnimator




class SpriteSheet:

    def __init__(self, pos, PictureKey):
        self.key = PictureKey
        self.pos = pos

        self.column = 1
        self.row = 1
        self.numRows = 1
        self.numColumns = 1
        self.numPictures = 1

        self.hasLooped=False

    def draw(self, canvas, cam,pos,angle,spriteDictionary):
        self.pos=pos
        image = spriteDictionary.get(self.key,'elf_demo')

        image.draw(canvas, cam,self.pos, self.numColumns, self.numRows, self.row, self.column,angle)

    def setRow(self, row, columnStart, numPictures, numColumns,numRows):
        self.column = columnStart
        self.row = row
        self.numPictures = numPictures
        self.numColumns = numColumns
        self.numRows=numRows
    def resetLoop(self):
        self.hasLooped=False
    def update(self):
        self.column += 1

        self.column = self.column % self.numPictures
        if self.column == 0:
            self.hasLooped=True
            self.column += 1

    def encode(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
