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
from Overlay import *
import pathlib
import TitleSlide
import time

# I'm going to create a .txt file called meta to store all the overhead information.
# it will be a string of numbers and words delimited by :
# In order, the data is currently:
# Screen size X
# Screen size Y
# SWINGTIME
# FRAMERATE

#IN PREPERATION FOR THE SCENARIO UPDATE
'''I want the map generation to be done 
completely externally, with random setpieces being 
included in the new map. the only interaction that 
needs to be done in this file is checking when the 
player is over the setpiece, if it has interactions
then triggering them.'''


data = (open('Meta.txt')).read()
META = data.split(':')

logging.basicConfig(filename='MainLog.txt', level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s -  %(message)s - MAIN')

# initialize and run the game from here. All other modules will send sprites with coordinates
# related to where on screen they should be shown.

# FOr slime specifically, at the beginning, the controller will call initialize() on the slime, with
# optional coordinates for where to position him on screen. THis method will return the sprite object
# with coordinated and properties.
# from there, the update() call will hande
# his positions and input for movement, etc.
WINX = int(META[0])
WINY = int(META[1])
fpsClock = pygame.time.Clock()
pygame.key.set_repeat(20)
FPS = int(META[3])  # frames per second setting
# This sets the size of the display
DISPLAYSURF = pygame.display.set_mode((WINX, WINY), 0, 32)
# setting the caption on the screen
pygame.display.set_caption('Bip Yum')
pygame.display.set_icon(slimeImg)


# this method will be used to render the title screen, which is the next project
def titleScreen():
    return TitleSlide.runTitle(DISPLAYSURF)

def initializePlay():
    # build the land takes the background tiles and generates the scenery
    global BackGround
    global slime
    global weapons
    global horde
    global overlay

    overlay = Overlay()
    BackGround = BuildTheLand(WINX, WINY)
    # create the player character
    # create Bip Himself
    slime = Slime()
    slime.setPosition(WINX / 2, WINY / 2)
    # create the weapon array
    weapons = pygame.sprite.Group()
    # For now, add a weapon. in the future, have a method to read this in from a file
    sword = Weapon()
    weapons.add(sword)
    # create the monster groups
    horde = pygame.sprite.Group()
    # For now, add a monster. in the future, have a method to read this in from a file


def initializeMonsters():
    monster = Monster()
    Stats = []
    # randomly assign the stats for the Monsterd
    for i in range(0, 8):
        Stats.append(random.randrange(1, 100))
    monster.setMonsterStats(Stats[0] + 12, Stats[1], Stats[2], Stats[3], Stats[4], Stats[5] % 4, Stats[6])
    monster.statBlock.setPos((0, 0))
    monster.setName("Enemy 1")
    #horde.add(monster)
    # add another monster for funsies


def gameplay():
    # play music
    end = False
    BattleMusicPath = Path('./Music(not Owned)/Meta Knight s Revenge.mp3')
    BattleMusic = pygame.mixer.Sound(BattleMusicPath)
    BattleMusic.play(-1)

    while True:  # the main game loop
        global BackGround
        global slime
        global weapons
        global horde
        global overlay
        BackGround.draw(DISPLAYSURF)
        slime.update()
        #UPDATE THE SETPIECES HERE!!! that way, if slime is taking damage, he is updated accordingly
        #And CHanges are not overwritten
        weapons.update(slime)
        overlay.update(slime)
        overlay.showText("Test", duration = 60)
        # for each monster in the horde, draw them on the screen in their current position if their health is above 0
        for enemy in horde:
            if enemy.statBlock.HEALTH > 0:
                enemy.update(slime)
                DISPLAYSURF.blit(enemy.image, (enemy.position))
                DISPLAYSURF.blit(enemy.statBlock.HealthBar.HPBAR_SURFACE, (enemy.position))
                # this checks to see if slime is touched by an enemy.
                if (pygame.Rect.colliderect(slime.rect.inflate(-5, -5), enemy.rect)):
                    slime.takeDamage(enemy)
            if enemy.statBlock.HEALTH <= 0:
                enemy.remove(horde)

        # Draw the Overlay

        for sword in weapons:
            if sword.swing:
                weapons.draw(DISPLAYSURF)
                # check to see if any monsters are hit by the sword
                for enemy in horde:
                    if (pygame.sprite.collide_rect(sword, enemy)
                            and enemy.statBlock.HEALTH > 0
                            and not enemy.isHit):
                        # logging.info("Enemy has been hit by sword")
                        enemy.takeDamage(slime)
                        enemy.statBlock.HealthBar.update(enemy)

            # I am become death, destroyer of slimes
            if slime.statBlock.HEALTH <= 0:
                # for now, just exit. In the future, display a death message and then reset the scenario
                BattleMusic.stop()
                #overlay.showText("You Lose!")
                return
            if len(horde.sprites()) == 0:
                BattleMusic.stop()
                #overlay.showText("You Win!")
                #return
        DISPLAYSURF.blit(overlay, (0, 0))

        # draw the slime to the screen
        DISPLAYSURF.blit(slime.image, slime.position)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


# Program Start

# this runs the titlescreen, and returns the users selection
while True:
    initializePlay()
    initializeMonsters()
    logging.info("Game Initialized")
    nextStep = titleScreen()
    if nextStep == 'Q' or nextStep == 'quit-button':
        pygame.quit()
        sys.exit()
    # when TitleScreen Returns, it will have an Event generated.
    # Currently, the only two events to be implemented are the
    # "go to gameplay" event to move to the gameplay loop
    # and the "quit" event that ends the game
    if nextStep == "start-button":
        # clears the event queue so that the gameplay starts fresh
        pygame.event.clear()
        gameplay()
        # if i am running this game multiple times in a row, It becomes SUPER laggy

'''when the game runs gameplay, it needs to read in a scenario. the scenario will consist of 
enemies and locations, the background tiles, and the music. the scenario will be loaded at gameplay, and
then run until a completion event occurs, be it the player dying or the enemies all dying. 
once the scenario is complete, this main file will return all the local variables to their 
defaults and await the next scenario
'''