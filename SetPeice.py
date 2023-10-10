#this will be used to design and implement the different terrain pieces that the
#game will utilise.

#each setpiece will have a sprite, a location to be put on the map, and properties that
#dictate what it will do, should slime interact with it.

'''property ideas:
Damage on Contact
block progress
interactable
   interaction => new sprite?
swimming?
death on contact
regain life
spawns enemies
destroyable
'''


import pygame
from pathlib import Path
import os


sceneShop = []
setPieceList = os.listdir('./setPiecePanels')

#get all the default sprites(only ones currently generated
for sprite in setPieceList:
    temp = Path('./setPiecePanels/' + sprite)
    sceneShop.append(pygame.image.load(temp))
class setPiece(pygame.sprite.Sprite):
    dealsDamage = False
    damage = 0
    isPassable = False
    interactable = False
    interactionTrigger = None
    swim = False
    killZone = False
    spawnEnemies = False
    enemy = None
    destroyable = False
    setPieceHP = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #sprite Information
        self.image = sceneShop[0]
        self.rect = self.image.get_rect()
        self.pos= (0,0)
        self.dealsDamage = False
        self.damage = 0
        self.isPassable = False
        self.interactable = False
        self.interactionTrigger = None
        self.swim = False
        self.killZone = False
        self.spawnEnemies = False
        self.enemy = None
        self.destroyable = False
        self.setPieceHP = 0

    #buildSetPiece lets me define a new setPiece with All Details.
    #if no new details are defined, it just set everything to the defaults

    def buildSetPiece(self, _image = sceneShop[0], _rect = self.image.get_rect(), _pos = (0,0),
                      _dealsDamage = False, _damage = 0, _isPassable = False, _interactable = False,
                      _interactionTrigger = None, _swim = False, _killZone = False, _spawnEnemies = False,
                      _enemy = None, _destroyable = False, _setPieceHP = 0):

        self.image = _image
        self.rect = _rect
        self.pos = _pos
        self.dealsDamage = _dealsDamage
        self.damage = _damage
        self.isPassable = _isPassable
        self.interactable = _interactable
        self.interactionTrigger = _interactionTrigger
        self.swim = _swim
        self.killZone = _killZone
        self.spawnEnemies = _spawnEnemies
        self.enemy = _enemy
        self.destroyable = _destroyable
        self.setPieceHP = _setPieceHP

    def setImage(self, newImage):
        self.image = newImage
    def setRect(self, newRect):
        self.rect = newRect
    def setPos(self, newPos):
        self.pos = newPos
    def toggleDealsDamage(self):
        self.dealsDamage = not self.dealsDamage
    def setDamage(self, newDamage):
        if(self.dealsDamage):
            self.damage = newDamage
    def toggleIsPassable(self):
        self.isPassable = not self.isPassable
    def toggleInteractable(self):
        self.interactable = not self.interactable
    def setInteractionTrigger(self, trigger):
        self.interactionTrigger = trigger
    def toggleSwim(self):
        self.swim = not self.swim
    def toggleKillZone(self):
        self.killZone = not self.killZone
    def toggleSpawnEnemies(self):
        self.spawnEnemies = not self.spawnEnemies
    def setEnemy(self, newEnemy):
        if(self.spawnEnemies):
            self.enemy = newEnemy
    def toggleDestroyable(self):
        self.destroyable = not self.destroyable
    def setSetPieceHP(self, newHP):
        if(self.destroyable):
            self.setPieceHP = newHP


