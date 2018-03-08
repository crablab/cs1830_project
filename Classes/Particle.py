import json
import time
import os
import json
import uuid
from Classes.SpriteSheet import SpriteSheet
from Classes.Vector import Vector
from SimpleGUICS2Pygame import simplegui_lib_draw
from Classes.Settings import * 


class Particle:

    def __init__(self, updateSprite,pos, vel,nextPosTime,nextPos, maxVel, maxRange, angle, radius, spriteKey, spriteDictionary,fps, removeOnVelocity0,
                 removeOnAnimationLoop,idObject,numRows,numColumns,startRow,startColumn,endRow,endColumn):

        self.idClass = 2
        self.idObject= idObject

        self.pos = pos
        self.vel = vel
        self.nextPos = nextPos
        self.nextPosTime = nextPosTime
        self.maxVel = maxVel

        self.maxRange = maxRange
        self.angle = angle

        self.updateSprite=updateSprite
        self.spriteKey = spriteKey

        self.spriteSheet = SpriteSheet( spriteDictionary.get(self.spriteKey, 'elf_demo'),fps)
        self.spriteSheet.setRow(numRows, numColumns, startRow, startColumn, endRow, endColumn)
        self.removeOnAnimationLoop = removeOnAnimationLoop
        self.removeOnVelocity0 = removeOnVelocity0

        self.dim = self.spriteSheet.animator.dimOriginal.copy()
        self.radius = radius
        if radius==0:
            self.radius=self.dim.size()/4



        self.currentTime = time.time()

    def recieve(self, nextPos,nextPosTime,maxVel,maxRange,angle,updateSprite,spriteKey,fps,numRows,numColumns,startRow,startColumn,endRow,endColumn,radius,spriteDictionary):
        self.nextPos=nextPos
        self.nextPosTime= nextPosTime
        self.maxVel=maxVel
        self.maxRange=maxRange
        self.angle=angle
        self.updateSprite=updateSprite
        self.radius=radius
        if self.spriteKey!=spriteKey:
            self.spriteSheet = SpriteSheet( spriteDictionary.get(self.spriteKey, 'elf_demo'),fps)
        if self.spriteSheet.numRows!=numRows or self.spriteSheet.numColumns!= numColumns or self.spriteSheet.startRow!=startRow or self.spriteSheet.startColumn!=startColumn or self.spriteSheet.endRow!=endRow or self.spriteSheet.endColumn!=endColumn:
            self.spriteSheet.setRow(numRows,numColumns,startRow,startColumn,endRow,endColumn)
            print(numRows,numColumns,startRow,startColumn,endRow,endColumn)

    def draw(self, canvas, cam):
            # ---------TESTING PURPOSES-----DO NOT REMOVE------
            # ratio = cam.dimCanv.copy().divideVector(cam.dim)
            # self.radius*=ratio.getX()
            # canvas.draw_circle(self.pos.getP(), self.radius, 1, 'White')
            # -------------------------------------------------

            pos = self.pos.copy()
            pictureSize = self.spriteSheet.animator.dimCamera.copy()
            origin = cam.origin.copy()
            distance = origin.copy().subtract(pos)
            if distance.getX() < 0:
                distance.x *= -1
            if distance.getY() < 0:
                distance.y *= -1
            distance.subtract(pictureSize.multiply(2))
            if distance.getX() < cam.dim.getX() / 2 and distance.getY() < cam.dim.getY() / 2:
                # --------TESTING PURPOSES----DO NOT REMOVE-------------
                #cam.dim = Vector(2600*2, 1400*2)
                objectPos = self.pos.copy().transformToCam(cam)
                self.spriteSheet.draw(canvas, cam, objectPos, self.angle)
                #cam.dim=Vector(1300,700)

            # DEVELOPER OPTION:
            if(DEVELOPER_OPTIONS):
                ratio = cam.dimCanv.copy().divideVector(cam.dim).divideVector(Vector(self.spriteSheet.numColumns,self.spriteSheet.numRows))
                a=self.radius*ratio.getX()
                canvas.draw_circle(self.pos.copy().transformToCam(cam).getP(), a, 1, 'White')
                simplegui_lib_draw.draw_rect(canvas, self.pos.copy().transformToCam(cam).subtract(self.dim.copy().divide(2).multiplyVector(ratio)).getP(),
                                             self.dim.copy().multiplyVector(ratio).getP(), 1, 'White', fill_color=None)
            # ----------------
    def bounce(self, normal):
        self.vel.reflect(normal)

    def moveRange(self, pos):
        dist = self.pos.copy().subtract(pos)
        dist.negate()
        if dist.length() != 0:
            dist.normalize().multiply(self.maxRange)

        self.nextPos = self.pos.copy().add(dist)

        self.timeTo(self.maxVel)
        self.vel.negate()

    def move(self, pos):
        self.nextPos = pos
        self.timeTo(self.maxVel)
        self.vel.negate()

    def update(self):
        if self.updateSprite:
            self.spriteSheet.update()
        if self.pos.copy().subtract(self.nextPos).dot(self.vel) > 0:
            self.vel.multiply(0)

        if self.pos != self.nextPos:
            x, y = self.pos.copy().distanceToVector(self.nextPos)
            dist = Vector(x, y)
            dist.negate()

            if self.nextPosTime - time.time() <= 0:
                self.pos = self.nextPos
            else:
                self.vel = dist.divide(self.nextPosTime - time.time())
                self.vel.multiply(time.time() - self.currentTime)
                self.pos.add(self.vel)

            self.currentTime = time.time()
            self.pos.add(self.vel.copy().multiply(time.time() - self.currentTime))
        self.currentTime = time.time()

    def turn(self, angle):
        self.vel.rotate(self.angle + angle)

    def copy(self,spriteDictionary):
        p = Particle(self.updateSprite,self.pos, self.vel,self.maxVel,self.maxRange,self.angle,self.radius,self.spriteKey,spriteDictionary,self.fps,self.removeOnVelocity0,self.removeOnAnimationLoop )
        return (p)

    def timeTo(self, maxVel):
        self.nextPosTime = time.time() + self.pos.copy().distanceTo(self.nextPos) / maxVel

    def encode(self):
        data = {'updateSprite':self.updateSprite,
                'idObject': self.idObject,
                'idClass': self.idClass,
                'pos': {'x': self.pos.x, 'y': self.pos.y},
                'vel': {'x': self.vel.x, 'y': self.vel.y},
                'maxVel': self.maxVel,
                'maxRange':self.maxRange,
                'currentTime':self.currentTime,
                'angle': self.angle,
                'radius': self.radius,
                'spriteKey': self.spriteKey,
                'nextPosTime':self.nextPosTime,
                'nextPos':{'x':self.nextPos.x,'y':self.nextPos.y},
                'fps': self.spriteSheet.fps,
                'removeOnVelocity0':self.removeOnVelocity0,
                'removeOnAnimationLoop':self.removeOnAnimationLoop,
                'numColumns':self.spriteSheet.numColumns,
                'numRows':self.spriteSheet.numRows,
                'startColumn':self.spriteSheet.startColumn,
                'startRow':self.spriteSheet.startRow,
                'endRow':self.spriteSheet.endRow,
                'endColumn':self.spriteSheet.endColumn}
        a=json.dumps(data)
        print(a)
        return a
