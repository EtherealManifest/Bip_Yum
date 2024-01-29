import Cluster
from SlimesDelight import *
import logging
from pathlib import Path
import os

logging.basicConfig(filename='MainLog.txt', level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s -  %(message)s  - MONSTER')

# this part will import (for now) all the enemy sprites and adds them to an array
GraveYardSmash = []
"""This is designed to hold all of the images for the sprites for this file"""

monsterList = os.listdir('./EnemySprites/')

for sprite in monsterList:
    temp = Path('./EnemySprites/' + sprite)
    GraveYardSmash.append(pygame.image.load(temp))

# not the acidity of the enemy, but the PlaceHolder for the sprite
EnemyPH = GraveYardSmash[0]


class Monster(pygame.sprite.Sprite):
    """Monster class, has stats, images, and position."""
    hitMoveRate = 1

    def __init__(self):
        """Initializes this monster."""
        # this initializes it as a sprite object by calling the Parent COnstructor
        pygame.sprite.Sprite.__init__(self)
        self.Name = ""
        self.Description = ""
        self.statBlock = StatBlock()
        self.setMonsterStats(20, 10, 10, 10, 10, 10, 10)
        self.monsterX = self.statBlock.pos[0]
        self.monsterY = self.statBlock.pos[1]
        self.position = (self.monsterX, self.monsterY)
        self.MonsterMoveSpeed = self.statBlock.SPEED
        self.isHit = False
        # the amount of time the monster is knocked back after being hit
        self.hitTime = 10
        self.hitTick = 0
        self.hitMoveRate = 1
        self.hitMove = (self.hitMoveRate, self.hitMoveRate)
        # This is the knockback rate, how far this enemy moves when slime hits it
        # giving it an image so that it shows up helps to establish position
        # the placeholder I use for this is a skull.
        self.normalImage = EnemyPH
        self.damageImage = EnemyPH
        self.deadImage = EnemyPH
        self.image = self.normalImage
        # because it extends Sprite, it has to have a rectangle and a position
        self.rect = self.image.get_rect()
        self.AICore = Cluster.STAY
        self.AICore.monster = self
        self.isDead = False
        self.deathAnimFrame = 10
        self.stopOnHit = True
        #these two are experimental. they are used by the movement cores to pause the monster for a time.
        self.waitClock = 0
        self.waitTick = 0
    # These are a variety of set and mod options for the stats and attributes.
    def setName(self, name):
        """Change the name of this monster"""
        self.Name = name

    def setDescription(self, desc):
        """Change the description for this monster"""
        self.Description = desc

    def setNameAndDescription(self, name, desc):
        """Change both the name and description for this monster"""
        self.Name = name
        self.Description = desc

    def setMonsterStats(self, HP, ATK, DEF, ARC, ARD, SPD, LCK):
        """Change the stats for this monster"""
        self.statBlock.setStats(HP, ATK, DEF, ARC, ARD, SPD, LCK)
        self.MonsterMoveSpeed = self.statBlock.SPEED

    def setAll(self, name, desc, HP, ATK, DEF, ARC, ARD, SPD, LCK):
        """Set all attributes for this monster"""
        self.statBlock.setStats(HP, ATK, DEF, ARC, ARD, SPD, LCK)
        self.MonsterMoveSpeed = SPD
        self.Name = name
        self.Name = name
        self.Description = desc

    # THe knockback is defined as the number of pixels the enemy will be pushed back per frame
    def setKnockback(self, num):
        """Change the knockback for this monster.

        num is the number of pixels to push the enemy back"""
        if num > 0:
            self.hitMoveRate = num
        else:
            self.hitMoveRate = 0
        self.hitMove = (self.hitMoveRate, self.hitMoveRate)

    def setHitTime(self, time):
        """Change the Hit time for this monster."""
        self.hitTime = time

    # These methods deal with setting the look of the beastie
    def setImage(self, Img):
        """Set the image for this monster"""
        self.image = Img

    def setPosition(self, position):
        """Change the position for this monster"""
        self.position = position
        self.statBlock.pos = position
        self.monsterY = self.position[1]
        self.monsterX = self.position[0]
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def setRect(self):
        """Set the rectange for this monster sprite based on it's image"""
        self.rect = self.image.get_rect()

    def setCore(self, core):
        """Change the AICore for this monster"""
        self.AICore = core
        self.AICore.monster = self

    def takeDamage(self, player):
        """The monster takes damage according to 'player''s stats."""
        if self.hitTick == self.hitTime:
            self.image = self.damageImage
            self.statBlock.HEALTH = self.statBlock.HEALTH - player.statBlock.ATTACK
        self.hitTick = self.hitTick - 1
        if self.hitTick > 0:
            # Update the Health Block
            self.statBlock.HealthBar.update(self)
            self.monsterX = self.monsterX + self.hitMove[0]
            self.monsterY = self.monsterY + self.hitMove[1]

        elif self.hitTick == 0:
            self.image = self.normalImage
            self.isHit = False
        else:
            self.hitTick = self.hitTime
            self.isHit = True

    def update(self, slime):
        """Update the creatures position on the screen, based on the currently set AICore, and knock it back if hit. """
        if self.statBlock.HEALTH > 0:
            # as long as he's alive, run the AICore's movement option to determine his new position
            self.position = self.statBlock.pos
            self.rect.x, self.rect.y = self.statBlock.pos[0], self.statBlock.pos[1]
            self.monsterX, self.monsterY = self.statBlock.pos[0], self.statBlock.pos[1]

            # if the monster is hit, then dont move towards the player, take damage instead
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
            self.AICore.update(slime)
            self.position = (self.monsterX, self.monsterY)
            self.statBlock.pos = self.position
            self.rect.x, self.rect.y = self.statBlock.pos[0], self.statBlock.pos[1]
        elif self.statBlock.HEALTH <= 0 and self.deathAnimFrame != 0:  # health is less than 0
            self.image = self.deadImage
            self.isDead = True
            self.deathAnimFrame -= 1

    def rectangle(self):
        """Returns the current rectangle for this Sprite as a string"""
        return ("\nMonster:\ntop: " + str(self.rect.top) +
                "\nbottom:" + str(self.rect.bottom) +
                "\nleft: " + str(self.rect.left) +
                "\nright: " + str(self.rect.right) +
                "\nx: " + str(self.rect.x) +
                "\ny: " + str(self.rect.y))
