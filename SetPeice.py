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
from pygame.locals import *
from pathlib import Path
import os

data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])

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
    killZone = False
    spawnEnemies = False
    enemy = None
    spawnRate = 0
    spawnTime = 0
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
        self.killZone = False
        self.spawnEnemies = False
        self.enemy = None
        self.spawnRate = 0
        self.spawnTime = 0
        self.destroyable = False
        self.setPieceHP = 0

    #buildSetPiece lets me define a new setPiece with All Details.
    #if no new details are defined, it just set everything to the defaults

    def buildSetPiece(self, _image = sceneShop[0], _rect = None, _pos = (0,0),
                      _dealsDamage = False, _damage = 0, _isPassable = False, _interactable = False,
                      _interactionTrigger = None, _killZone = False, _spawnEnemies = False,
                      _enemy = None, _spawnRate = 1000, _destroyable = False, _setPieceHP = 0):
        self.image = _image
        if(_rect == None):
            self.rect = self.image.get_rect()
        else:
            self.rect = _rect
        self.pos = _pos
        self.dealsDamage = _dealsDamage
        self.damage = _damage
        self.isPassable = _isPassable
        self.interactable = _interactable
        self.interactionTrigger = _interactionTrigger
        self.killZone = _killZone
        self.spawnEnemies = _spawnEnemies
        self.enemy = _enemy
        self.spawnRate = _spawnRate
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

    def update(self, slime, horde):
        #if the slime touches this setPiece
        if pygame.sprite.collide_rect(self, slime):
            #if this setPiece deals damage on contact, deal that damage
            if self.dealsDamage:
                slime.setPieceDamage(self.damage)
            #if this object is not passable, prevent entry
            if not self.isPassable:
                #get the slimes allowed movement directions.
                #this will stop the slime from moving
                #on to this surface
                self.getPlayerPos(slime)
            if self.interactable:
                #if the spacebar is pressed, trigger the trigger
                if pygame.key.get_pressed()[K_SPACE]:
                    self.interactionTrigger()
            if self.killZone:
                #It's a kill zone, so slime DIES!!!
                slime.statBlock.HEALTH = 0
            if self.spawnEnemies:
                if self.spawnTime ==0:
                    horde.add(self.enemy)
                    self.spawnTime = self.spawnRate
                else:
                    self.spawnTime -= self.spawnTime






    #This method will return the direction that the player is in
    #relation to the current setPiece. Used to keep the player out
    #of the object, or knock them back if damaged.
    #also used to push the object.
    def getPlayerPos(self, slime):
        # If clipped_line is not an empty tuple then the line
        # collides/overlaps with the rect.
        clipped_line = self.rect.clipline(slime.rect.left)
        if clipped_line:
            slime.allowedMoves['left'] = False
        clipped_line = self.rect.clipline(slime.rect.right)
        if clipped_line:
            slime.allowedMoves['right'] = False
        clipped_line = self.rect.clipline(slime.rect.top)
        if clipped_line:
            slime.allowedMoves['up'] = False
        clipped_line = self.rect.clipline(slime.rect.bottom)
        if clipped_line:
            slime.allowedMoves['down'] = False

        return slime.allowedMoves





#Add a method setTheStage that takes in the screen size and returns a
#surface with a (reasonable) random number of setPieces set on it.
#in the future, this will read in from the Scenario to determine what
#and where to put the setPieces

#Temp class to hold all of the test Sprites:
class setPieceTester():
    tester = setPiece()
    def __init(self):
        self.tester = setPiece()






