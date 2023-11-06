# This is the file for the main game loop, seperated from the class
# implementation for bip yum
#FIXME It's time. the Scenario update is nearly here. This file should read in all the data from a created Scenario and
# run the scenario accordingly.
from Armory import *
import logging
from Overlay import *
from pathlib import Path
import TitleSlide
import TestScenario
import gc
import Scenario
import threading
import copy


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

#temporary tester for the new background maker
BackGroundLocale = Path('./GroundPanels/Lava/')

# this method will be used to render the title screen, which is the next project


def playScenario(Scenario):
    # play music
    #read the Scenario
    scenario = Scenario
    slime = scenario.TheWanderer
    slime.setPosition(scenario.slimyPOS[0], scenario.slimyPOS[1])
    setPieces = scenario.trove
    BackGround = scenario.vista
    horde = []
    for monster in scenario.horde:
        horde.append(monster)
    weapons = pygame.sprite.Group()
    weapons.add(scenario.weapon)
    #set the overlay
    overlay = Overlay()

    while True:  # the main game loop
        BackGround.draw(DISPLAYSURF)
        #UPDATE THE SETPIECES HERE!!! that way, if slime is taking damage, he is updated accordingly
        #And CHanges are not overwritten
        slime.allowAllDirections()
        weapons.update(slime)
        overlay.update(slime)
        for prop in setPieces:
            DISPLAYSURF.blit(prop.image, prop.pos)
            prop.update(slime, horde)
        slime.update()
        scenario.winCondition(horde)
        # for each monster in the horde, draw them on the screen in their current position if their health is above 0
        for i  in range(0, len(horde)):
            if not horde[i].isDead:
                horde[i].setKnockback(slime.statBlock.ATTACK)
                horde[i].update(slime)
                DISPLAYSURF.blit(horde[i].image, horde[i].position)
                DISPLAYSURF.blit(horde[i].statBlock.HealthBar.HPBAR_SURFACE, (horde[i].position))
                # this checks to see if slime is touched by an horde[i].
                if (pygame.Rect.colliderect(slime.rect.inflate(-5, -5), horde[i].rect)):
                    slime.takeDamage(horde[i])
            if horde[i].deathAnimFrame > 0 and horde[i].isDead:
                horde[i].update(slime)
                DISPLAYSURF.blit(horde[i].image, (horde[i].position))
            elif horde[i].isDead and horde[i].deathAnimFrame == 0:
                continue
        # Draw the Overlays
        for sword in weapons:
            if sword.swing:
                weapons.draw(DISPLAYSURF)
                # check to see if any monsters are hit by the sword
                for enemy in horde:
                    if (pygame.sprite.collide_rect(sword, enemy)
                            and enemy.statBlock.HEALTH > 0
                            and not enemy.isHit):
                        # logging.info("horde[i] has been hit by sword")
                        enemy.takeDamage(slime)
                        enemy.statBlock.HealthBar.update(horde[i])
                for i in range(0, len(setPieces)):
                    if (pygame.sprite.collide_rect(sword, setPieces[i]) and setPieces[i].destroyable):
                        setPieces[i].takeDamage(slime)
            # I have become death, destroyer of slimes
            if slime.statBlock.HEALTH <= 0:
                # for now, just exit. In the future, display a death message and then reset the scenario
                #BattleMusic.stop()
                slime.reset(scenario.slimyPOS)
        if(scenario.Win):
            return None
        for enemy in horde:
            if enemy.isDead and enemy.deathAnimFrame == 0:
                horde.remove(enemy)

        DISPLAYSURF.blit(overlay, (0, 0))
        # draw the slime to the screen
        DISPLAYSURF.blit(slime.image, slime.position)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)

def runScenario(Scenario):
    playScenario(Scenario)
# Program Start

# this runs the titlescreen, and returns the users selection

logging.info("Game Initialized")
TheScenario = None
nextStep = TitleSlide.runTitle(DISPLAYSURF)
if nextStep == 'Q' or nextStep == 'quit-button':
    pygame.quit()
    sys.exit()
# when TitleScreen Returns, it will have an Event generated.
# Currently, the only two events to be implemented are the
# "go to gameplay" event to move to the gameplay loop
# and the "quit" event that ends the game
if nextStep == "start-button":
    TheScenario = TestScenario.TestScenario()
    nextStep = TitleSlide.runTitle(DISPLAYSURF)
while(nextStep == 'start-button'):
    # clears the event queue so that the gameplay starts fresh
    TheScenario.reset()
    runScenario(TheScenario)
    print("scenario Complete")
    nextStep = TitleSlide.runTitle((DISPLAYSURF))







        # if i am running this game multiple times in a row, It becomes SUPER laggy

'''when the game runs gameplay, it needs to read in a scenario. the scenario will consist of 
enemies and locations, the background tiles, and the music. the scenario will be loaded at gameplay, and
then run until a completion event occurs, be it the player dying or the enemies all dying. 
once the scenario is complete, this main file will return all the local variables to their 
defaults and await the next scenario
'''