import pygame, sys
from pygame.locals import *
import SlimesDelight
from SlimesDelight import *
import logging
import math

logging.basicConfig(filename='MainLog.txt', level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s -  %(message)s - MAIN')

weaponDefaultImg = pygame.image.load('blue_sword_sprite.png')
# sets how long the sword swing lasts
SWINGTIME = 15


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

    def weaponPosition(self, player, SWINGTIME, elapsed, swingAngle, startAngle):
        # the swing angle is the total arc that the sword will take
        swingAngle = math.radians(swingAngle)
        # the starting angle is the degrees counterclockwise from the horizontal the swing should start at
        startAngle = math.radians(startAngle)
        if elapsed == 0:
            self.angle = startAngle
        else:
            self.angle = startAngle - ((SWINGTIME / elapsed) * swingAngle)
        self.pos = (
            player.rect.x + (player.rect.width * (math.cos(self.angle))),
            player.rect.y + (player.rect.height * (math.sin(self.angle)))
        )
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]
        self.angle = math.degrees(self.angle)
        # rotate the image accordingly
        self.image = pygame.transform.rotate(self.image, -self.angle - 90)

    def update(self, player):
        # it is positioned at the top of the slime, then moved back to
        # center the blade.
        # MAY NEED TUNING
        # this will all be implemented in position()
        self.position(player)
        self.image = weaponDefaultImg
        # the documentsataion said to call get() before get_pressed()
        pygame.event.get()
        # if the mouse is clicked, swing the sword
        # I'm gonna coordinate this as if he is facing left always.
        # if he faces right, Im going to just flip everything and move it
        if not self.swing:
            if pygame.mouse.get_pressed()[0]:
                self.swing = True
                self.swingTick = SWINGTIME

        if self.swing == True:
            # I want to optimize this. I want to make the swing angle
            # and the position a function of the time
            if self.direction == 'up':
                if (self.swingTick > 0):
                    self.weaponPosition(player, SWINGTIME, self.swingTick, -115, 135)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False
            elif self.direction == 'down':
                if (self.swingTick > 0):
                    self.weaponPosition(player, SWINGTIME, self.swingTick, -115, 310)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False

            # if slime is facing left, the swing angle needs to be negative
            elif (self.direction == 'left' or self.direction == 'down-left'
                  or self.direction == 'up-left'):
                if (self.swingTick > 0):
                    self.weaponPosition(player, SWINGTIME, self.swingTick, -115, 135)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False
            # if the player is facing right, then Acoomodate and adjust accordingly
            else:
                if (self.swingTick > 0):
                    self.weaponPosition(player, SWINGTIME, self.swingTick, -115, 135)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False
            # decrement the swing counter
            self.swingTick = self.swingTick - 1
            # logging.info("Weapon rect Coordinates (" + str(self.rect.x) + ", " + str(self.rect.y) + ")")

    '''Alright, big explain here. this is an attempt at creating a method that will
    Uniformly generate the position and angle of the weapon based on its current
    angle and how far through it's swing animation it is. it directly modifies the 
    passed weapons positon information, changing the angle and the pos attributes.
    Pass it the player that is using the weapon, the global variable SWINGTIME, 
    the amount of time elapsed (SWINGTIME - swingtime), the total angle that this
    sword swing will occupy(in degrees), and the starting angle(also in degrees)
    '''
