# this will be used to design and implement the different terrain pieces that the
# game will utilise.
import math

import pygame
from pygame.locals import *
from pathlib import Path
import os

data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])

sceneShop = []
"""Holds all of the Setpieces"""
setPieceList = os.listdir('./setPiecePanels')

# get all the default sprites(only ones currently generated
for sprite in setPieceList:
    temp = Path('./setPiecePanels/' + sprite)
    sceneShop.append(pygame.image.load(temp))


def stub():
    """What? Do you want every method to have drawn out implementation?

    Too bad! Instead, this one has an excessive amount of documentation!

    Worth mentioning is the fact that I am typing all of this out by hand. No chatGPT or anything.

    Why are you still reading this? It's a stub. like, there is obviously not going to be anything here.

    Alright, I like you. YOu're the thourough type. Carry on, and be Excellent!"""
    pass


class setPiece(pygame.sprite.Sprite):
    """All the setpieces that make up the props for this show thing."""
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
        """Initializes this scenario"""
        pygame.sprite.Sprite.__init__(self)

        # sprite Information
        self.image = sceneShop[0]
        self.baseImage = self.image
        self.interactionImage = pygame.transform.scale_by(self.image, 1.1)
        self.destroyedImage = sceneShop[1]
        self.rect = self.image.get_rect()
        self.pos = (0, 0)
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
        self.destroyTrigger = stub

    # buildSetPiece lets me define a new setPiece with All Details.
    # if no new details are defined, it just set everything to the defaults

    def buildSetPiece(self, _image=sceneShop[0], _rect=None, _pos=(0, 0),
                      _dealsDamage=False, _damage=0, _isPassable=False, _interactable=False,
                      _interactionTrigger=None, _killZone=False, _spawnEnemies=False,
                      _enemy=None, _spawnRate=1000, _destroyable=False, _setPieceHP=0):
        """Define the parameters of this setPiece"""
        self.image = _image
        self.baseImage = self.image
        if _rect is None:
            self.rect = self.image.get_rect()
        else:
            self.rect = _rect
        self.pos = _pos
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]
        self.dealsDamage = _dealsDamage
        self.damage = _damage
        self.isPassable = _isPassable
        self.interactable = _interactable
        # the interaction trigger needs to ALWAYS take two parameters, the player character and the horde.
        # this allows a lot more diversity in what each setpiece can do.
        self.interactionTrigger = _interactionTrigger
        self.killZone = _killZone
        self.spawnEnemies = _spawnEnemies
        self.enemy = _enemy
        self.spawnRate = _spawnRate
        self.destroyable = _destroyable
        self.setPieceHP = _setPieceHP
        self.interactionImage = pygame.transform.scale_by(self.image, 1.1)
        # destroyTrigger is overridden in the actual setpiece Definition
        # resetEnemy is overridden and defined in the actual setPiece Definition

    # set the image(does not modify the rectangle, follow with a call to setRect
    def setImage(self, newImage):
        """Set the image for this setPiece"""
        self.image = newImage

    def setBaseImage(self, newImage):
        """Set the base, unmodified Image"""
        self.baseImage = newImage

    def setBothImages(self, newImage):
        """Set both the base image, and the regular image"""
        self.image = newImage
        self.baseImage = newImage

    # set the new rectangle and position
    def setRect(self, newRect):
        """Set the rectangle, and reposition it. """
        self.rect = newRect
        self.pos = (self.rect.x, self.rect.y)

    def setPos(self, newPos):
        """Sets the position for this setPiece"""
        self.pos = newPos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def toggleDealsDamage(self):
        """Set whether this setpiece deals damage on contact"""
        self.dealsDamage = not self.dealsDamage

    def setDamage(self, newDamage):
        """Set how much damage this setPiece deals"""
        if self.dealsDamage:
            self.damage = newDamage

    def toggleIsPassable(self):
        """Set whether or not players can pass through this setPiece"""
        self.isPassable = not self.isPassable

    def toggleInteractable(self):
        """Set whether players can interact with this Setpiece"""
        self.interactable = not self.interactable

    def setInteractionTrigger(self, trigger):
        """Set what happens when the player interacts with this setPiece"""
        self.interactionTrigger = trigger

    def toggleKillZone(self):
        """Set whether or not this setpiece kills a player on contact"""
        self.killZone = not self.killZone

    def toggleSpawnEnemies(self):
        """Set whether this setPiece spawns enemies or not"""
        self.spawnEnemies = not self.spawnEnemies

    def setEnemy(self, newEnemy):
        """Set the enemy that this Setpiece spawns"""
        if self.spawnEnemies:
            self.enemy = newEnemy

    def toggleDestroyable(self):
        """set whether this setPiece is destroyable or not"""
        self.destroyable = not self.destroyable

    def setSetPieceHP(self, newHP):
        """Set the HP of this SetPiece"""
        if self.destroyable:
            self.setPieceHP = newHP

    def get_rect(self):
        """Return the rect for this setPiece"""
        return self.rect

    def toString(self):
        """Returns a string representing the setPiece"""
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
        """Updates the setPiece, checking for character contact or triggers to spawn enemies."""
        self.image = self.baseImage
        if self.spawnEnemies:
            if self.spawnTime == 0:
                # this method needs to redeclare this enemy with fresh stats.
                self.resetEnemy()
                horde.append(self.enemy)
                self.spawnTime = self.spawnRate
            else:
                self.spawnTime -= 1
        # if the slime touches this setPiece
        if slime.rect.colliderect(self.rect):
            # print(self.toString())
            # if this setPiece deals damage on contact, deal that damage
            if self.dealsDamage:
                slime.setPieceDamage(self.damage)
            # if this object is not passable, prevent entry
            if not self.isPassable:
                # get the slimes allowed movement directions.
                # this will stop the slime from moving
                # on to this surface
                self.modifyMovement(slime)
            if self.interactable:
                self.image = self.interactionImage
                # if the right shift is pressed, trigger the trigger
                if pygame.key.get_pressed()[K_LSHIFT]:
                    self.interactionTrigger()
            if self.killZone:
                # It's a kill zone, so slime DIES!!!
                slime.statBlock.HEALTH = 0
            if self.interactable:
                self.interactionTrigger(slime, horde)

    # This method will return the direction that the player is in
    # relation to the current setPiece. Used to keep the player out
    # of the object, or knock them back if damaged.
    # also used to push the object.
    def modifyMovement(self, slime):
        """Stop the player from moving through this object"""
        # If clipped_line is not an empty tuple then the line
        # collides/overlaps with the rect.
        # This method gets a little icky because I need it to not disable directions
        # there only one pixel is on the line

        # this array is to hold the sides that are currently intersected
        sides = []

        clipped_line_top = self.rect.clipline(slime.rect.bottomleft, slime.rect.bottomright)
        clipped_line_right = self.rect.clipline(slime.rect.topleft, slime.rect.bottomleft)
        clipped_line_left = self.rect.clipline(slime.rect.topright, slime.rect.bottomright)
        clipped_line_bottom = self.rect.clipline(slime.rect.topleft, slime.rect.topright)

        # go through, one side at a time, and figure out how much of each side slime currently touches.
        if clipped_line_top:
            top_cross = lineLength(clipped_line_top[0], clipped_line_top[1])
            sides.append(top_cross)
        else:
            top_cross = 0

        if clipped_line_bottom:
            bottom_cross = lineLength(clipped_line_bottom[0], clipped_line_bottom[1])
        else:
            bottom_cross = 0

        if clipped_line_left:
            left_cross = lineLength(clipped_line_left[0], clipped_line_left[1])
        else:
            left_cross = 0

        if clipped_line_right:
            right_cross = lineLength(clipped_line_right[0], clipped_line_right[1])
        else:
            right_cross = 0

        sides = [top_cross, bottom_cross, left_cross, right_cross]

        longest = -1
        for side in sides:
            # if this side is 0 or shorter than the current longest, remove it from the list of sides.
            if side > longest:
                longest = side
        # if all of the sides are 0, then return.
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

    # tests to see if Slime is touching the setpiece, used for interaction triggers.
    def slimeCollide(self, slime):
        """Returns TRUE if the player is colliding with this object"""
        return self.rect.colliderect(slime.rect)

    # this method is used to render the setpieces taking damage. if it is called, then the sword has struck the
    # setpiece. reduce the health. If it would go past zero, modify the setpiece to no longer take damage and
    # set it's image to its broken image and change any other relevant settings.
    def takeDamage(self, slime):
        """Deal damage to this setpeice based on character stats"""
        self.setPieceHP -= slime.statBlock.ATTACK
        if self.setPieceHP <= 0:
            self.destroyable = False
            self.image = self.destroyedImage
            self.destroyTrigger()

    # here, p1 and p2 are both tuples of coordinates representing the endpoints of a line. this method
    # will return a single integer representing the length of that line. It is used in getPlayerPos
    # to determine which side of the setpiece that slime is interacting with.


def lineLength(p1, p2):
    """Determine the linear length of a line given it's endpoints. """
    p1_y = p1[0] - p2[0]
    p1_x = p1[1] - p2[1]
    # use the pythagorean theorem to determine line length
    py_l = math.sqrt(((p1_y * p1_y) + (p1_x * p1_x)))
    return abs(py_l)
