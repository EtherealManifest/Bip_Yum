# FIX ME: Monster is functional, but needs to be polymorphic. Add all the monsters into a group, and make all the function relating to them
# act on the group. there are pygame functions for this.

# add references from th eoverhead file for: WINX, WINY, FRAMERATE, DISPLAYSURF
# This is the file for the main game loop, seperated from the class
# implementation for bip yum
import pygame, sys
from SlimesDelight import *
import SlimesDelight  # Slimy Behavior
from GroundMaker import *
import GroundMaker  # Draws the Background
from pygame.locals import *
from MonsterMash import *
import MonsterMash
import Armory
from Armory import *

import logging

logging.basicConfig(filename='MainLog.txt', level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s -  %(message)s - MAIN')

# initialize and run the game from here. All other modules will send sprites with coordinates
# related to where on screen htye should be shown. all classes will have a cast() method that
# returns the currently displayed sprites, complete with coordinates, in a group.

# FOr slime specifically, at the beginning, the controller will call initialize() on the slime, with
# optional coordinates for where to position him on screen. THis method will return the sprite object
# with coordinated and properties.
# from there, the update() call will hande
# his positions and input for movement, etc.


fpsClock = pygame.time.Clock()
pygame.key.set_repeat(20)
FPS = 60  # frames per second setting, there is a copy in BIPYUM1 that should be the same
# This sets the size of the display
DISPLAYSURF = pygame.display.set_mode((WINX, WINY), 0, 32)

# setting the caption on the screen
pygame.display.set_caption('Bip Yum')
WHITE = (255, 255, 255)
pygame.display.set_icon(slimeImg)


# This set of variables defines the displayed objects

def initialize():
    # build the land takes the background tiles and generates the scenery
    global BackGround
    global slime
    global weapons
    global horde

    BackGround = BuildTheLand(WINX, WINY)
    # create the player character
    # create Bip Himself
    slime = Slime()
    # create the weapon array
    weapons = pygame.sprite.Group()
    # For now, add a weapon. in the future, have a method to read this in from a file
    sword = Weapon()
    weapons.add(sword)

    # create the monster group
    horde = pygame.sprite.Group()
    # For now, add a monster. in the future, have a method to read this in from a file
    monster = Monster()
    monster.statBlock.setPos((100, 100))
    horde.add(monster)
    # add another monster for funsies
    monster2 = Monster()
    monster2.statBlock.setPos((200, 200))
    horde.add(monster2)


initialize()
logging.info("Game Initialized")
while True:  # the main game loop
    # Instead of filling with white, lets make a tiling of the background and blit it here
    global BackGround
    global slime
    global weapons
    global horde

    BackGround.draw(DISPLAYSURF)
    slime.update()
    weapons.update(slime)
    # for each monster in the horde, draw them on the screen in their current position if their health is above 0
    for monster in horde:
        if (monster.statBlock.HEALTH > 0):
            monster.update(slime)
            DISPLAYSURF.blit(monster.image, (monster.position))
            DISPLAYSURF.blit(monster.statBlock.HealthBar.HPBAR_SURFACE, (monster.position))
            # this checks to see if slime is touched by an enemy.
            if (pygame.Rect.colliderect(slime.rect.inflate(-5, -5), monster.rect)):
                slime.takeDamage(monster)
    # draw the slime to the screen
    DISPLAYSURF.blit(slime.image, slime.position)
    for sword in weapons:
        if (sword.swing):
            weapons.draw(DISPLAYSURF)
            # check to see if any monsters are hit by the sword
            for monster in horde:
                if (pygame.sprite.collide_rect(sword, monster) and monster.statBlock.HEALTH > 0):
                    # logging.info("Enemy has been hit by sword")
                    monster.takeDamage(slime)
        # I am become death, destroyer of slimes
        if (slime.statBlock.HEALTH <= 0):
            # for now, just exit. In the future, display a death message and then reset the scenario
            exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
