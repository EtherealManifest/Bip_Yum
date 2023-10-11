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

    def update(self, slime):
        #if the slime touches this setPiece
        if pygame.sprite.collide_rect(self, slime):
            #if this setPiece deals damage on contact, deal that damage
            if self.dealsDamage:
                slime.setPieceDamage(self.damage)
            #if this object is not passable, prevent entry
            if not self.isPassable:
                #get the players position, then reduce their motion in that direction
                position = self.getPlayerPos(slime)
                slimesPosition = slime.getPosition()
                playerDir = slime.direction



    #This method will return the direction that the player is in
    #relation to the current setPiece. Used to keep the player out
    #of the object, or knock them back if damaged.
    #also used to push the object.
    def getPlayerPos(self, slime):
        slimey = slime.rect.y
        slimex = slime.rect.x
        player_pos = "None"

        #player is to the left
        if self.rect.x > slimex:
            player_pos = "left"
            if self.rect.y > slimey:
                player_pos = "up-left"
            elif self.rect.y < slimey:
                player_pos = "down-left"
        #player is to the right
        elif self.rect.x < slimex:
            player_pos = "right"
            if self.rect.y > slimey:
                player_pos = "up-right"
            elif self.rect.y < slimey:
                player_pos = "down-right"
        elif self.rect.x == slimex:
            if self.rect.y > slimey:
                player_pos = "up"
            elif self.rect.y < slimey:
                player_pos = "down"
        else:
            player_pos = "centered"

        return player_pos




#Add a method setTheStage that takes in the screen size and returns a
#surface with a (reasonable) random number of setPieces set on it.
#in the future, this will read in from the Scenario to determine what
#and where to put the setPieces

#Temp class to hold all of the test Sprites:
class setPieceTester():
    tester = setPiece()
    def __init(self):
        self.tester = setPiece()

def setTheStage(setPieces = 5):

    for i in range(0, setPieces):
        #create a random setpiece
        #choose a random number
        #based on that number, create a new object with properties





