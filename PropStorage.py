# Define the setpieces to be used here
from pathlib import Path

import Crypt
import SetPiece
import os
import pygame
import random

data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])
sceneShop = {}
"""Dictionary that holds all Created SetPeices"""
setPieceList = os.listdir('./setPiecePanels')

# get all the default sprites(only ones currently generated)
# for each sprite in the listed directory
# get all the default sprites(only ones currently generated
for sprite in setPieceList:
    temp = Path('./setPiecePanels/' + sprite)
    # scene shop has every entry as a sprite surface and a name as a series of list entries
    sceneShop[sprite] = pygame.image.load(temp)


class exit(SetPiece.setPiece):
    """A default setpiece"""

    def __init__(self):
        """initializes this default setpiece"""
        super().__init__()
        self.image = sceneShop.get("Default.png", None)
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (WINX - 35, WINY - 35))
        self.isPassable = True
        self.dealsDamage = False
        self.killZone = False
        self.spawnEnemies = False
        self.destroyable = False
        self.interactable = True
        self.interactionTrigger = self.trigger
        self.triggered = False

    def reset(self):
        """reset this setPiece to it's __init__() form."""
        self.__init__()


    def trigger(self, slime, horde):
        self.triggered = True


class DefaultSetPiece(SetPiece.setPiece):
    """A default setpiece"""

    def __init__(self):
        """initializes this default setpiece"""
        super().__init__()
        self.image = sceneShop.get("Destroyable_0.png", None)
        self.destroyedImage = sceneShop.get("Destroyable_1.png", None)
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (99, 123))
        self.isPassable = False
        self.dealsDamage = True
        self.damage = 10
        self.killZone = True
        self.spawnEnemies = True
        self.enemy = Crypt.WOLF()
        self.spawnRate = 300
        self.spawnTime = 0
        self.resetEnemy = self.wolfResetEnemy
        self.destroyable = True
        self.setPieceHP = 300
        self.destroyTrigger = self.destroyDefaultSetpiece

    def reset(self):
        """reset this setPiece to it's __init__() form."""
        self.__init__()

    def wolfResetEnemy(self):
        """Reset the Wolf Enemy"""
        self.enemy = Crypt.WOLF()

    def destroyDefaultSetpiece(self):
        """destroy this default setPiece"""
        self.toggleSpawnEnemies()
        self.toggleIsPassable()


DEFAULTSETPIECE = DefaultSetPiece()
"""The default Setpiece, its attributes are very dynamic"""


class Round_Cactus(SetPiece.setPiece):
    """Creates a small, round cactus. Hurts to touch"""

    def __init__(self):
        """Initializes this cactus"""
        super().__init__()
        self.image = sceneShop.get("Round_Cactus.png", None)
        self.setBothImages(self.image)
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (10, 123))
        self.isPassable = False
        self.dealsDamage = True
        self.damage = 35
        self.killZone = False
        self.spawnEnemies = False
        self.destroyable = False
        self.setPieceHP = 300

    def reset(self):
        """resets this cactus"""
        self.__init__()


class Tall_Cactus(SetPiece.setPiece):
    """Creates a tall cactus. Hurts to touch!"""

    def __init__(self):
        """Initializes this cactus"""
        super().__init__()
        self.setBothImages(sceneShop.get("Tall_Cactus.png", None))
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (100, 300))
        self.isPassable = False
        self.dealsDamage = True
        self.damage = 45
        self.killZone = False
        self.spawnEnemies = False
        self.destroyable = False
        self.setPieceHP = 300

    def reset(self):
        """Resets this cactus"""
        self.__init__()


class TumbleweedLord(SetPiece.setPiece):
    """Creates a small tumbleweed! Scratches as it tumbles by"""

    def __init__(self):
        """Initializes this tumbleweed"""
        super().__init__()
        self.setBothImages(sceneShop.get("Buzz-Buzz.png"))
        self.rect = self.image.get_rect()
        self.pos = (WINX, WINY)
        self.dealsDamage = False
        self.isPassable = True
        self.spawnEnemies = True
        self.enemy = Crypt.TUMBLEWEED()
        self.wrath = 1
        """This number multiplies teh tumbleweeds damage"""
        self.spawnRate = 15
        self.spawnTime = 0
        self.resetEnemy = self.tumbleweedResetEnemy
        self.tumbleWeedsKilled = 0

    def tumbleweedResetEnemy(self):
        """Resets this tumbleweed"""
        scaleFactor = (.5 + (1.5 - .5) * random.random())  # this should generate a number between .5 and 1.5
        self.enemy = Crypt.TUMBLEWEED()
        self.enemy.statBlock.ATTACK *= self.wrath
        self.enemy.baseImage = pygame.transform.scale_by(self.enemy.image, scaleFactor)
        self.enemy.setPosition((WINX + 1, random.randint(32, int(WINY))))


class Cabbage(SetPiece.setPiece):
    """Creates a round, green cabbage. Tasty!"""

    def __init__(self):
        super().__init__()
        self.setBothImages(sceneShop.get("Cabbage_0.png"))
        self.rect = self.image.get_rect()
        self.pos = (0, 0)
        self.dealsDamage = False
        self.isPassable = True
        self.interactable = True
        self.interactionTrigger = self.eat
        self.eaten = False

    def eat(self, slime, horde):
        """Om, nom, nom!"""
        self.setBothImages(sceneShop.get("Cabbage_1.png"))
        self.interactable = False
        self.eaten = True
        if slime.statBlock.HEALTH < slime.statBlock.TOTALHEALTH:
            slime.statBlock.HEALTH += 20
        if slime.statBlock.HEALTH > slime.statBlock.TOTALHEALTH:
            slime.statBlock.HEALTH = slime.statBlock.TOTALHEALTH
