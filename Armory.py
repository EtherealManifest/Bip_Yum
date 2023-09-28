import pygame, sys
from pygame.locals import *
import SlimesDelight
from SlimesDelight import *
import logging
import math
from pathlib import Path

data = (open('Meta.txt')).read()
META = data.split(':')

logging.basicConfig(filename='MainLog.txt', level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s -  %(message)s - MAIN')

#Ive added a few sprite styles for this. if you want to check them out,
#try entering new colors. each color has a different size, though they all
#have the same power.
weaponName = 'green_sword_sprite.png'
imgPath = Path("./Weapon Sprites/" + weaponName)
weaponDefaultImg = pygame.image.load(imgPath)


# sets how long the sword swing lasts
#this is read in from the Meta.txt file. To see the arrangement of the items in the file,
#see the comments on Game.py
SWINGTIME = int(META[2])


# These are placeholder animations


class Weapon(pygame.sprite.Sprite):
    # this is the position of the BOTTOM-CENTER of the weapon
    pos = (0, 0)
    # The maximum reach, for determining the hitbox
    size = 0
    # This is for determining which way the weapon swings
    direction = ''
    facingRight = False
    # used to tell whether the sword is being swung
    swing = False
    # this determines the frame for the sword swing
    # it is equal to the time in frames since the beginning of the sword swing
    # animation, going from the maximum time to zero
    swingTick = 0
    # the current angle of the weapon in radians, used to determine the angle.
    angle = 0

    def position(self, player):
        if (player.direction == 'up'):
            self.pos = (player.slimex + self.rect.width, player.slimey)
            self.facingRight = False
        elif (player.direction == 'down'):
            self.pos = (player.slimex + self.rect.width, player.slimey)
            self.facingRight = False
        if (player.direction == 'down-left'
                or player.direction == 'left'
                or player.direction == 'up-left'):
            self.pos = (player.slimex - 8, player.slimey - 16)
            self.facingRight = False
        elif (player.direction == 'down-right'
              or player.direction == 'right'
              or player.direction == 'up-right'):
            self.pos = (player.slimex + 32, player.slimey - 16)
            self.facingRight = True
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.direction = player.direction

    def __init__(self):
        # this initializes it as a Sprite
        pygame.sprite.Sprite.__init__(self)
        # these are Sprite Attributes
        self.pos = (0, 0)
        self.image = weaponDefaultImg
        # effectively, the Hitbox
        self.rect = self.image.get_rect()
        self.direction = ''
        swing = False
        swingTick = 0
        facingRight = False


    '''Alright, big explain here. this is an attempt at creating a method that will
    Uniformly generate the position and angle of the weapon based on its current
    angle and how far through it's swing animation it is. it directly modifies the 
    passed weapons positon information, changing the angle and the pos attributes.
    Pass it the player that is using the weapon, the global variable SWINGTIME, 
    the amount of time elapsed (SWINGTIME - swingtime), the total angle that this
    sword swing will occupy(in degrees), and the starting angle(also in degrees)
    '''
    def weaponPosition(self, player, SWINGTIME, elapsed, swingAngle, startAngle):
        # the swing angle is the total arc that the sword will take
        #these numbers are long, so i decided to declare them here.
        #they are the necessary offset that is added to the position determiner
        adjustX = (player.rect.width + self.rect.height / 3)
        adjustY = (player.rect.height + self.rect.height / 3)
        swingAngle = math.radians(swingAngle)
        # the starting angle is the degrees counterclockwise from the horizontal the swing should start at
        startAngle = math.radians(startAngle)
        if elapsed == 0:
            self.angle = startAngle + swingAngle
        else:
            self.angle = startAngle + ((elapsed/SWINGTIME ) * swingAngle)
        self.pos = (
            player.rect.x + (adjustX * (math.cos(self.angle)) - self.rect.width/2),
            player.rect.y + (adjustY * (math.sin(self.angle))) - self.rect.width/2)
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]
        self.angle = math.degrees(self.angle)
        # rotate the image accordingly
        self.image = pygame.transform.rotate(self.image, -self.angle - 90)
        #update (called once per frame)
    def update(self, player):
        # it is positioned at the top of the slime, then moved back to
        # center the blade.
        # MAY NEED TUNING
        # this will all be implemented in position()
        self.position(player)
        self.image = weaponDefaultImg
        # the documentataion said to call get() before get_pressed()
        pygame.event.get()
        # if the mouse is clicked, swing the sword
        if not self.swing:
            if pygame.mouse.get_pressed()[0]:
                self.swing = True
                self.swingTick = SWINGTIME
                self.angle = 0
        #if sword is swinging, determine the direction, and then pass the corresponding parameters to
        #weaponPosition()
        if self.swing == True:
            if self.direction == 'up':
                if (self.swingTick > 0):
                    self.weaponPosition(player, SWINGTIME, self.swingTick, 180, -180)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False
            elif self.direction == 'down':
                if (self.swingTick > 0):
                    self.weaponPosition(player, SWINGTIME, self.swingTick, 180, 0)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False

            # if slime is facing left, the swing angle needs to be negative
            elif (self.direction == 'left' or self.direction == 'down-left'
                  or self.direction == 'up-left'):
                if (self.swingTick > 0):
                    self.weaponPosition(player, SWINGTIME, self.swingTick, 180, 90)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False

            # if the player is facing right, then Acoomodate and adjust accordingly
            else:
                if (self.swingTick > 0):
                    self.weaponPosition(player, SWINGTIME, self.swingTick, -180, 90)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False
            # decrement the swing counter
            self.swingTick = self.swingTick - 1
            # logging.info("Weapon rect Coordinates (" + str(self.rect.x) + ", " + str(self.rect.y) + ")")


