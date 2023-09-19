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
# build the land takes the background tiles and generates the scenery
BackGround = BuildTheLand(WINX, WINY)

# create Bip Himself
slime = Slime()
# Create a sample Monster

monster = Monster()
monster.statBlock.setPos((100, 100))
# THis is a container to hold the weapons. It will hold a dirtySprite weapon, that way it can be made
# to appear and disappear with each swing
weapons = pygame.sprite.Group()
# create a new weapon called sword
sword = Weapon()
weapons.add(sword)
# This is where the little man is born, keep track of it

# Trying to do the fight scenes in another program isnt working, so I need this main part to
# Move to another part locally, otherwie it keeps executing the true loop, causing major bugs.

# I've decided to do an action-RPG instead (A-la a Link to the Past.) Instead of having a battle scene, its
# Gonna be a sword swing action, tied to the mouse click)
logging.info("Game Initialized")
while True:  # the main game loop
    # Instead of filling with white, lets make a tiling of the background and blit it here
    BackGround.draw(DISPLAYSURF)
    slime.update()
    weapons.update(slime)
    # draw Slime to the screen, with any potential updates accounted for.
    if (monster.statBlock.HEALTH > 0):
        monster.update(slime)
        DISPLAYSURF.blit(monster.image, (monster.position))
        DISPLAYSURF.blit(monster.statBlock.HealthBar.HPBAR_SURFACE, (monster.position))
        # this checks to see if slime is touched by an enemy.
        if (pygame.Rect.colliderect(slime.rect.inflate(-5, -5), monster.rect)):
            slime.takeDamage(monster)
    DISPLAYSURF.blit(slime.image, slime.position)
    if (sword.swing):
        weapons.draw(DISPLAYSURF)
        if (pygame.sprite.collide_rect(sword, monster) and monster.statBlock.HEALTH > 0):
            # logging.info("Enemy has been hit by sword")
            monster.takeDamage(slime)
    if (slime.statBlock.HEALTH <= 0):
        exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
