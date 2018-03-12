# REMEMBER: SIMULATE YOUR SHOT AGAINST MONSTER TO CHECK IF KILLED, IF SO, ADD STATS TO PLAYER, THE MONSTER WILL BE REMOVED ON THE OTHER SIDE

import time
import random
from Classes.Vector import Vector
from Classes.RandomGen import getRandomMagicWeapon, getRandomMagicCast, getRandomMonster
from Classes.Weapon import Weapon
from Classes.Particle import Particle
from Classes.Monster import Monster
from Classes.Objects import weapon_set, visual_set, spriteDictionary, getUid, playerId
from Classes.Settings import MAP_WIDTH, MAP_HEIGHT
# monsters spawned based on how far away from the map they are.
# respawn by tier time

from Classes.Objects import monster_set, player_list
from Collisions.Collisions import doCirclesIntersect


class MonsterAi:
    def __init__(self, numMonsters):
        self.tier1Total = int(numMonsters * 0.6)
        self.tier2Total = int(numMonsters * 0.3)
        self.tier3Total = int(numMonsters * 0.1)
        self.tier1Current = 0
        self.tier2Current = 0
        self.tier3Current = 0
        self.tier1SpawnRate = 100
        self.tier2SpawnRate = 600
        self.tier3SpawnRate = 1800
        self.tier3Respawn = 0
        self.tier2Respawn = 0
        self.tier1Respawn = 0
        self.timeElapsed = 0
        self.currentTime = time.time()
        self.updateStatsTime = 0
        self.moveMonstersTime = 20

    def update(self):
        self.updateCountdowns()
        self.moveMonsters()
        self.attack()
        self.respawn()
        self.updateSpriteState()
        if self.updateStatsTime > 100:
            self.updateNum()
            self.updateStatsTime = 0
        self.currentTime = time.time()
    def respawn(self):
        if self.tier1Respawn>self.tier1SpawnRate and self.tier1Current<self.tier1Total:
            self.tier1Respawn=0
            self.spawnT1()
        if self.tier2Respawn>self.tier2SpawnRate and self.tier2Current<self.tier2Total:
            self.tier2Respawn=0
            self.spawnT2()
        if self.tier3Respawn>self.tier3SpawnRate and self.tier3Current<self.tier3Total:
            self.tier3Respawn=0
            self.spawnT3()

    def spawnMonsters(self):
        t1 = self.tier1Total
        t2 = self.tier2Total
        t3 = self.tier3Total
        for a in range(0,t1):
            self.spawnT1()
        for a in range(0,t2):
            self.spawnT2()
        for a in range(0,t3):
            self.spawnT3()

    def updateSpriteState(self):
        for monster in monster_set:
           # print(monster.spriteState)
            if monster.particle.pos.getX()-monster.particle.nextPos.getX()<0 and not monster.spriteState==2:
                monster.setSpriteState(2)
            elif monster.particle.pos.getX()-monster.particle.nextPos.getX()>0 and not monster.spriteState==1:
                monster.setSpriteState(1)
          #  print(monster.spriteState)
    def updateCountdowns(self):
        difference = self.currentTime - time.time()
        self.updateStatsTime += difference
        self.moveMonstersTime += difference
        self.tier1Respawn += difference
        self.tier2Respawn += difference
        self.tier3Respawn += difference

    def moveMonsters(self):
        # CHOOSE A RANDOM POINT WITHIN OPERATING RANGE OF MONSTER AND MOVE THE MONSTER TO THAT LOCATION IF THE VELOCITY IS 0 and not fierin
        for monster in monster_set:
            if monster.particle.vel.getX() == 0 and monster.particle.vel.getY() == 0 and not monster.hasFired:
                px = random.randrange(int(monster.operationOrigin.getX() - monster.operationRange.getX()),
                                    int(monster.operationOrigin.getX() + monster.operationRange.getX()))
                py = random.randrange(int(monster.operationOrigin.getY() - monster.operationRange.getY()),
                                      int( monster.operationOrigin.getY() + monster.operationRange.getY()))
                if px>MAP_WIDTH:
                    px=MAP_WIDTH
                if px<0:
                    px=0
                if py>MAP_HEIGHT:
                    py=MAP_HEIGHT
                if py<0:
                    py=0
                monster.particle.move(Vector(px, py))

    def updateNum(self):
        self.tier1Current = 0
        self.tier2Current = 0
        self.tier3Current = 0
        for monster in monster_set:

            if monster.tier == 1:
                self.tier1Current += 1
            elif monster.tier == 2:
                self.tier2Current += 1
            elif monster.tier == 3:
                self.tier3Current += 1

    def attack(self):
        # VERY SIMPLE AI, IF MONSTER WITHIN OPERATION RANGE AND WITHIN ATTACK RANGE ATTACK AND KEEP RANGE IF MONSTER OUT OF OPERATION RANGE ==> IGNORE
        # ONLY TAKE CARE OF LOCAL MONSTER SET, NOT EXTERNAL, BUT ATTACK BOTH PLAYERS

        for monster in monster_set:
            if not monster.hasFired:
            # SLIGHTLY LONG, JUST CHECKING IF WITHIN BOUNDARY OF OPERATION RECT
                if monster.particle.pos.getX() < monster.operationOrigin.getX() + monster.operationRange.getX() or monster.particle.pos.getX() > monster.operationOrigin.getX() - monster.operationRange.getX() or monster.particle.pos.getY() < monster.operationOrigin.getY() + monster.operationRange.getY() or monster.particle.pos.getY() > monster.operationOrigin.getY() - monster.operationRange.getY():
                    # CHECK IF PLAYER WITHIN ATTACK RANGE:
                    for player in player_list:
                        # CHECK IF PLAYER ATTACK RANGE (RADIUS) FROM SELF POSITION USE CIRCLE CIRCLE DETECTION.
                        if doCirclesIntersect(monster.particle, player.particle):
                            monster.particle.keepRange(player.particle.pos,monster.followDistance)  # artbitrary distance at which to keep range by monster tier
                            self.fire(player, monster)


                # IF HEALTH IS LOWER THAN PREVIOUS GENERATION I.E. ATTACKED, THEN RETALIATE ON CLOSEST OPPONENT
                d1 = 0
                d2 = 0
                if monster.lifePrev < monster.life:
                    for player in player_list:
                        if player.idObject == playerId:

                            d1 = monster.particle.pos.copy().distanceTo(player.particle.pos)
                        else:

                            d2 = monster.particle.pos.copy().distanceTo(player.particle.pos)
                    for player in player_list:
                        if player.idObject == playerId and d1 < d2:

                            monster.particle.keepRange(player.particle.pos, monster.followDistance)
                            self.fire(player, monster)
                        elif player.idObject != playerId and d2 < d1:
                            self.fire(player, monster)
                            monster.particle.keepRange(player.particle.pos, monster.followDistance)

    def fire(self, player, monster):
        # THIS IS ESSENTIALLY COPPIED FROM CLICK HANDLER AND IMPLEMENTED FOR MONSTER ONCE IT CHOOSES A TARGET :d, NO TIME TO MAKE IT NICER ON BOTH ENDS AND OPTIMIZE UNFORTUNATELY
        # SET MAGIC SPRITE ATTACK ANIMATION
        numRows, numCol, startRow, startCol, endRow, endCol, key = getRandomMagicWeapon(monster.magic)
        # SET MAGIC SPRITE WEAPON WITH The above
        print(numRows, numCol, key)
        weapon = Weapon(player.particle.pos.copy(), Vector(0, 0), 0,
                        player.particle.pos.copy(), 0, 0, 0, key, spriteDictionary,
                        20, getUid(), numRows, numCol, startRow, startCol, endRow, endCol, False, True, monster.magic)
        # BIND SPRITE TO MONSTER and MONSTER TO SPRITE to remember who kills who
        weapon.idPlayer = monster.idObject
        monster.magicId = weapon.idObject

        weapon_set.add(weapon)

        # SET MAGIC SPRITE CASTING ANIMATION USE PARTICLE CLASS ADD TO VISUAL SET
        # SHIFT ALL MAGIC SPRITES UP FOR MONSTER IF SMALL
        pos = monster.particle.pos.copy()
        if monster.particle.dim.getY()<120:
            pos.y -= 30
        numRows, numCol, startRow, startCol, endRow, endCol, key = getRandomMagicCast(monster.magic)
        particle = Particle(True, pos, Vector(0, 0), 0, pos, 0, 0, 0, 0, key, spriteDictionary, 15, False, True,
                            getUid(), numRows, numCol, startRow, startCol, endRow, endCol)
        visual_set.add(particle)

        monster.particle.vel.multiply(0)
        monster.particle.nextPosTime = time.time()
        monster.particle.nextPos = monster.particle.pos
        monster.hasFired=True

    def spawnT1(
            self):  # WITHIN 25% OF MAP CENTER, OPERATION RANGE OF 1000, ATTACK RANGE OF 500 t1, 1500,t2, 2500 t3? for lols
        # the following locations on the map X axis and y axis randomly:   \_________XXXXXX___________\
        pos = Vector(random.randint(int(MAP_WIDTH / 2 - MAP_WIDTH / 4),int( MAP_WIDTH / 2 + MAP_WIDTH / 4)),
                     random.randint(int(MAP_HEIGHT / 2 - MAP_HEIGHT / 4),int( MAP_HEIGHT / 2 + MAP_HEIGHT / 4)))
        vel = Vector(0, 0)
        maxVel = 100  # why not
        aBack,numRows, numCol, startRow, startCol, endRow, endCol, key = getRandomMonster(1)
        monster = Monster(pos, vel, 0, pos, maxVel, 0, 0, key, spriteDictionary, 15, getUid(), False, Vector(0, 0), 1,
                          numRows, numCol, startRow, startCol, endRow, endCol, 1,aBack)

        monster.setSpriteState(2)
        monster.life = random.randrange(6000, 10000)
        monster.magic = random.randrange(200, 1000)
        monster.attackRange = 150
        monster.followDistance = 50
        monster.operationRange = Vector(2000,2000)
        monster.operationOrigin = pos
        monster_set.add(monster)

    def spawnT2(
            self):  # WITHIN 25-75% OF MAP CENTER, OPERATION RANGE OF 3000, ATTACK RANGE OF 500 t1, 1500,t2, 2500 t3? for lols
        num = random.randrange(1, 3)
        adjustX = 0
        adjustY = 0
        if num == 2:
            adjustX = int(MAP_WIDTH / 2)
            adjustY =int( MAP_HEIGHT / 2)
        # the following locations on the map X axis and y axis randomly:   \______XXXXX__________XXXXX_______\
        pos = Vector(random.randint(int((MAP_WIDTH / 3)) + adjustX,int(((MAP_WIDTH / 3) * 2)) + adjustX),
                     random.randint(int((MAP_HEIGHT / 3)) + adjustY, int(((MAP_HEIGHT / 3) * 2)) + adjustY))

        vel = Vector(0, 0)
        maxVel = 120  # why not

        aBack,numRows, numCol, startRow, startCol, endRow, endCol, key = getRandomMonster(2)
        monster = Monster(pos, vel, 0, pos, maxVel, 0, 0, key, spriteDictionary, 15, getUid(), False, Vector(0, 0), 1,
                          numRows, numCol, startRow, startCol, endRow, endCol, 2,aBack)
        monster.setSpriteState(2)
        monster.life = random.randrange(50000, 300000)
        monster.magic = random.randrange(10000, 30000)
        monster.attackRange = 250
        monster.followDistance = 100
        monster.operationRange = Vector(2000,2000)
        monster.operationOrigin = pos
        monster_set.add(monster)

    def spawnT3(
            self):  # WITHIN 25% OF MAP CENTER, OPERATION RANGE OF 1000, ATTACK RANGE OF 500 t1, 1500,t2, 2500 t3? for lols

        num = random.randrange(1, 3)
        adjustX = 0
        adjustY = 0
        if num == 2:
            adjustX = int(MAP_WIDTH * 0.75)
            adjustY = int(MAP_HEIGHT * 0.75)
        # the following locations on the map X axis and y axis randomly:   \XXXXX______________________XXXXX\


        pos = Vector(random.randint(0+ adjustX,int( MAP_WIDTH / 4)+adjustX),
                     random.randint(0+adjustY, int(MAP_HEIGHT / 4) +adjustY))
        vel = Vector(0, 0)
        maxVel = 200  # why not
        aBack,numRows, numCol, startRow, startCol, endRow, endCol, key = getRandomMonster(3)
        monster = Monster(pos, vel, 0, pos, maxVel, 0, 0, key, spriteDictionary, 15, getUid(), False, Vector(0, 0), 1,
                          numRows, numCol, startRow, startCol, endRow, endCol, 3,aBack)
        monster.setSpriteState(2)

        monster.life=random.randrange(500000,1000000)
        monster.magic=random.randrange(50000,100000)
        monster.attackRange=750
        monster.followDistance=200
        monster.operationRange=Vector(2000,2000)
        monster.operationOrigin=pos


        monster_set.add(monster)
