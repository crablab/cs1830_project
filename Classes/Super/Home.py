from Classes.Base.Vector import Vector
from Classes.Middle.Particle import Particle
from Classes.Functions.Collisions.Collisions import doCirclesIntersect,isPointInRect
import time
class Home:
    def __init__(self,pos,p1Pos,p2Pos,spriteDictionary):
        self.house=Particle(False,pos,Vector(0,0),Vector(0,0),pos,0,0,0,0,'house',spriteDictionary,1,False,False,'house',1,2,1,2,1,2)
        self.portalH=Particle(True,p1Pos,Vector(0,0),Vector(0,0),p1Pos,0,0,0,0,'portal',spriteDictionary,10,False,False,'portalH',1,9,1,1,1,9)
        self.portalM = Particle(True, p2Pos, Vector(0, 0), Vector(0, 0), p2Pos, 0, 0, 0, 0, 'portal', spriteDictionary,
                                10, False, False, 'poratlM', 1, 9, 1, 1, 1, 9)
        self.teleportCountDown=120
        self.prevTime=time.time()

    def update(self,player):
        if player.particle.pos.getX()<-1000:
            self.house.update()
            self.block(player)
            self.portalM.update()

        self.teleport(player)
        self.teleportCountDown+=time.time()-self.prevTime
        self.prevTime=time.time()
        self.portalH.update()

    def teleport(self,player):
        if self.teleportCountDown>120:
            if player.particle.pos.getX()>-1000:
                if doCirclesIntersect(player.particle.pos,player.particle.radius,self.portalM.pos,self.portalM.radius):
                    self.teleportCountDown=0
                    player.particle.pos=self.portalH.pos.copy()
                    player.particle.nextPosTime=time.time()
                    player.particle.nextPos=self.portalH.pos.copy()
                    print(player.particle.pos,self.portalH.pos)
                    return
            if player.particle.pos.getX() < -1000:
                if doCirclesIntersect(player.particle.pos,player.particle.radius,self.portalH.pos,self.portalH.radius):
                    self.teleportCountDown=0
                    player.particle.pos=self.portalM.pos.copy()
                    player.particle.nextPosTime=time.time()
                    player.particle.nextPos=self.portalM.pos.copy()
                    return

    def block(self,player):
        if player.particle.pos.getX()<-1000:
            player.life=player.totalLife #while in the house life is at max.
            if not isPointInRect(player.particle.pos,self.house.pos,self.house.dim.copy()) and player.particle.vel.copy().dot(player.particle.pos.copy().subtract(self.house.pos))>0:
                player.particle.vel.multiply(0)

                player.particle.nextPos=player.particle.pos
                player.particle.nextPosTime=time.time()

    def draw(self,canvas,cam):
        self.house.draw(canvas,cam)
        self.portalH.draw(canvas,cam)
        self.portalM.draw(canvas,cam)