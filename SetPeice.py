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
import math

import pygame
from pygame.locals import *
from pathlib import Path
import os
import Crypt
import copy

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

def stub():
    pass

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
        self.resetEnemy = stub

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
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]
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
        self.pos = (self.rect.x, self.rect.y)

    def setPos(self, newPos):
        self.pos = newPos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
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
    def get_rect(self):
        return self.rect

    def toString(self):
        return ("\n  Deals Damage: " + str(self.dealsDamage) +
                ",\n Rect: X:" + str(self.rect.x) + ", Y: " + str(self.rect.y) +
                ",\n Position: " + str(self.pos) +
                ",\n damage: " + str(self.damage) +
                ",\n is passable: " + str(self.isPassable) +
                ",\n is Interactable: " + str(self.interactable) +
                ",\n Killzone: " + str(self.killZone) +
                ",\n SPawns Enemies: " + str(self.spawnEnemies) +
                ",\n Destroyable: " + str(self.destroyable) +
                ",\n HP: " + str(self.setPieceHP))

    def update(self, slime, horde):
        if self.spawnEnemies:
            if self.spawnTime == 0:
                #this method needs to redeclare this enemy with fresh stats.
                self.resetEnemy()
                horde.append(self.enemy)
                self.spawnTime = self.spawnRate
            else:
                self.spawnTime -= 1
        #if the slime touches this setPiece
        if slime.rect.colliderect(self.rect):
            #print(self.toString())
            #if this setPiece deals damage on contact, deal that damage
            if self.dealsDamage:
                slime.setPieceDamage(self.damage)
            #if this object is not passable, prevent entry
            if not self.isPassable:
                #get the slimes allowed movement directions.
                #this will stop the slime from moving
                #on to this surface
                self.slimeCollide(slime)
            if self.interactable:
                #if the spacebar is pressed, trigger the trigger
                if pygame.key.get_pressed()[K_SPACE]:
                    self.interactionTrigger()
            if self.killZone:
                #It's a kill zone, so slime DIES!!!
                slime.statBlock.HEALTH = 0







    #This method will return the direction that the player is in
    #relation to the current setPiece. Used to keep the player out
    #of the object, or knock them back if damaged.
    #also used to push the object.
    def slimeCollide(self, slime):
        # If clipped_line is not an empty tuple then the line
        # collides/overlaps with the rect.
        #This method gets a little icky because I need it to not disable directions
        #there only one pixel is on the line

        #this array is to hold the sides that are currently intersected
        sides = []

        clipped_line_top = self.rect.clipline(slime.rect.bottomleft, slime.rect.bottomright)
        clipped_line_right = self.rect.clipline(slime.rect.topleft, slime.rect.bottomleft)
        clipped_line_left = self.rect.clipline(slime.rect.topright, slime.rect.bottomright)
        clipped_line_bottom = self.rect.clipline(slime.rect.topleft, slime.rect.topright)

        #go through, one side at a time, and figure out how much of each side slime currently touches.
        if(clipped_line_top):
            top_cross = lineLength(clipped_line_top[0], clipped_line_top[1])
            sides.append(top_cross)
        else:
            top_cross = 0

        if(clipped_line_bottom):
            bottom_cross = lineLength(clipped_line_bottom[0], clipped_line_bottom[1])
        else:
            bottom_cross = 0

        if(clipped_line_left):
            left_cross = lineLength(clipped_line_left[0], clipped_line_left[1])
        else:
            left_cross = 0

        if(clipped_line_right):
            right_cross = lineLength(clipped_line_right[0], clipped_line_right[1])
        else:
            right_cross = 0

        sides = [top_cross, bottom_cross, left_cross, right_cross]

        longest = -1
        for side in sides:
            #if this side is 0 or shorter than the current longest, remove it from the list of sides.
            if side > longest:
                longest = side
        #if all of the sides are 0, then return.
        if longest == 0:
            return


        if top_cross == longest:
            slime.allowedMoves['down'] = False
        if bottom_cross == longest:
            slime.allowedMoves['up'] = False
        if left_cross == longest:
            slime.allowedMoves['right'] = False
        if right_cross == longest:
            slime.allowedMoves['left'] = False

    # here, p1 and p2 are both tuples of coordinates representing the endpoints of a line. this method
    # will return a single integer representing the length of that line. It is used in getPlayerPos
    # to determine which side of the setpiece that slime is interacting with.
def lineLength(p1, p2):
    p1_y = p1[0] - p2[0]
    p1_x = p1[1] - p2[1]
    #use the pythagorean theorem to determine line length
    py_l = math.sqrt(((p1_y * p1_y) + (p1_x * p1_x)))
    return abs(py_l)



