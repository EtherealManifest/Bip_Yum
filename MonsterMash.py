import pygame
from StatusBlock import *
from SlimesDelight import *
import SlimesDelight
import logging
from pathlib import Path
import os

logging.basicConfig(filename='MainLog.txt', level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s -  %(message)s  - MONSTER')

MonsterMoveSpeed = 1
# the amount of time the monster is knocked back after being hit
HITTIME = 10
# this part will import (for now) all the enemy sprites and adds them to an array
GraveYardSmash = []

monsterList = os.listdir('./EnemySprites/')

for sprite in monsterList:
    temp = Path('./EnemySprites/' + sprite)
    GraveYardSmash.append(pygame.image.load(temp))

# not the acidity of the enemy, but the PlaceHolder for the sprite
EnemyPH = GraveYardSmash[0]


class Monster(pygame.sprite.Sprite):
    statBlock = StatBlock()
    monsterX = 0
    monsterY = 0
    Name = ""
    Description = ""
    position = (monsterX, monsterY)
    statBlock.pos = position
    # this is the amount to change his position by when he takes damage, ordered (x,y)
    isHit = False
    hitMove = (0, 0)
    hitMoveRate = 0
    hitTick = 0
    direction = ""

    def __init__(self):
        # this initializes it as a sprite object by calling the Parent COnstructor
        pygame.sprite.Sprite.__init__(self)
        self.Name = ""
        self.Description = ""
        self.statBlock = StatBlock()
        self.setMonsterStats(20, 10, 10, 10, 10, 10, 10)
        self.monsterX = self.statBlock.pos[0]
        self.monsterY = self.statBlock.pos[1]
        self.position = (self.monsterX, self.monsterY)
        self.isHit = False
        self.hitTick = 0
        self.hitMove = (0, 0)
        # This is the knockback rate, how far this enemy moves when slime hits it
        self.hitMoveRate = 1
        # giving it an image so that it shows up helps to establish position
        # the placeholder I use for this is a skull.
        self.image = EnemyPH
        # because it extends Sprite, it has to have a rectangle and a position
        self.rect = self.image.get_rect()

    # These are a variety of set and mod options for the stats and attributes.
    def setName(self, name):
        self.Name = name

    def setDescription(self, desc):
        self.Description = desc

    def setNameAndDescription(self, name, desc):
        self.Name = name
        self.Description = desc

    def setMonsterStats(self, HP, ATK, DEF, ARC, ARD, SPD, LCK):
        self.statBlock.setStats(HP, ATK, DEF, ARC, ARD, SPD, LCK)

    def setAll(self, name, desc, HP, ATK, DEF, ARC, ARD, SPD, LCK):
        statBlock = StatBlock(HP, ATK, DEF, ARC, ARD, SPD, LCK)
        self.Name = name
        self.Description = desc

    def setKnockback(self, num):
        self.hitMoveRate = num

    # These methods deal with setting the look of the beastie
    def setImage(self, Img):
        self.image = Img

    def takeDamage(self, player):
        print(self.Name + " is receiving Damage")
        if self.hitTick == HITTIME:
            self.statBlock.HEALTH = self.statBlock.HEALTH - player.statBlock.ATTACK
        self.hitTick = self.hitTick - 1
        if self.hitTick > 0:
            # Update the Health Block
            self.statBlock.HealthBar.update(self)
            self.monsterX = self.monsterX + self.hitMove[0]
            self.monsterY = self.monsterY + self.hitMove[1]
        elif self.hitTick == 0:
            self.isHit = False
        else:
            self.hitTick = HITTIME
            self.isHit = True

    def update(self, slime):
        if self.statBlock.HEALTH > 0:
            self.position = self.statBlock.pos
            self.rect.x, self.rect.y = self.statBlock.pos[0], self.statBlock.pos[1]
            self.monsterX, self.monsterY = self.statBlock.pos[0], self.statBlock.pos[1]
            # these are actually gonna come from outside the frame, but they will
            # move towards the player
            # if the monster is hit, then dont move towards the player, take damage instead
            # for this part, there is a wierd line about assigning moverate to movehit. this is a system that makes sure
            # that he moves in the right direction when he is hit.
            if self.isHit:
                if self.monsterX >= slime.slimex:
                    if self.monsterY >= slime.slimey:
                        self.hitMove = (self.hitMoveRate, self.hitMoveRate)
                    if self.monsterY < slime.slimey:
                        self.hitMove = (self.hitMoveRate, -self.hitMoveRate)
                else:
                    if self.monsterY >= slime.slimey:
                        self.hitMove = (-self.hitMoveRate, self.hitMoveRate)
                    if self.monsterY < slime.slimey:
                        self.hitMove = (-self.hitMoveRate, -self.hitMoveRate)
                # his position will be adjusted here
                self.takeDamage(slime)
            # make sure that the monster doesnt go inside of slime. IF they arent Overlapping, move enemy
            elif not pygame.Rect.colliderect(self.rect, slime.rect.inflate(-5, -5)):
                # for this part, there is a wierd line about assigning moverate to movehit.
                # this is a system that makes sure that he moves in the right direction when he is hit.
                if self.monsterX > slime.slimex:
                    self.hitMove = (self.hitMoveRate, 0)
                    if self.monsterY > slime.slimey:
                        self.monsterY -= MonsterMoveSpeed
                        self.direction = 'up-left'
                        self.hitMove = (self.hitMoveRate, self.hitMoveRate)
                    else:
                        self.direction = 'left'
                    if self.monsterY < slime.slimey:
                        self.monsterY += MonsterMoveSpeed
                        self.direction = 'down-left'
                        self.hitMove = (self.hitMoveRate, -self.hitMoveRate)
                    else:
                        self.direction = 'left'
                    self.monsterX -= MonsterMoveSpeed

                elif self.monsterX < slime.slimex:
                    self.hitMove = (-self.hitMoveRate, 0)
                    if self.monsterY > slime.slimey:
                        self.monsterY -= MonsterMoveSpeed
                        self.direction = 'up-right'
                        self.hitMove = (-self.hitMoveRate, self.hitMoveRate)
                    else:
                        self.direction = 'right'
                    if self.monsterY < slime.slimey:
                        self.monsterY += MonsterMoveSpeed
                        self.direction = 'down-right'
                        self.hitMove = (-self.hitMoveRate, -self.hitMoveRate)
                    else:
                        self.direction = 'right'
                    self.monsterX += MonsterMoveSpeed

                else:
                    if self.monsterY < slime.slimey:
                        self.monsterY += MonsterMoveSpeed
                        self.hitMove = (0, -self.hitMoveRate)
                        self.direction = 'down'
                    else:
                        self.monsterY -= MonsterMoveSpeed
                        self.direction = 'up'
                        self.hitMove = (0, self.hitMoveRate)

            self.position = (self.monsterX, self.monsterY)
            self.statBlock.pos = self.position
            self.rect.x, self.rect.y = self.statBlock.pos[0], self.statBlock.pos[1]

    def rectangle(self):
        return ("\nMonster:\ntop: " + str(self.rect.top) +
                "\nbottom:" + str(self.rect.bottom) +
                "\nleft: " + str(self.rect.left) +
                "\nright: " + str(self.rect.right) +
                "\nx: " + str(self.rect.x) +
                "\ny: " + str(self.rect.y))
