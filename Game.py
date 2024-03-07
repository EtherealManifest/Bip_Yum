# This is the file for the main game loop, seperated from the class
# implementation for bip yum
from Armory import *
import Overlay
from pathlib import Path
import TitleSlide
import Anthology
# I'm going to create a .txt file called meta to store all the overhead information.
# it will be a string of numbers and words delimited by :
# In order, the data is currently:a
# Screen size X
# Screen size Y
# SWINGTIME
# FRAMERATE


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
"""THe primary surface that the Game is rendered on"""
# setting the caption on the screen
pygame.display.set_caption('Bip Yum')
pygame.display.set_icon(slimeImg)

def playScenario(Scenario):
    """Take the Scenario and play it through."""
    # read the Scenario
    scenario = Scenario
    slime = scenario.TheWanderer
    slime.setPosition(scenario.slimyPOS[0], scenario.slimyPOS[1])
    setPieces = scenario.trove
    BackGround = scenario.vista
    horde = []
    for monster in scenario.horde:
        horde.append(monster)
    sword = scenario.weapon
    # set the overlay
    overlay = Overlay.Overlay()

    while True:  # the main game loop
        BackGround.draw(DISPLAYSURF)
        # UPDATE THE SETPIECES HERE!!! that way, if slime is taking damage, he is updated accordingly
        # And CHanges are not overwritten
        slime.allowAllDirections()
        sword.update(slime)
        overlay.update(slime)
        for prop in setPieces:
            DISPLAYSURF.blit(prop.image, prop.pos)
            prop.update(slime, horde)
        if scenario.Win:
            slime.update(win=True)
        else:
            slime.update()
        scenario.winCondition(horde, setPieces)
        # for each monster in the horde, draw them on the screen in their current position if their health is above 0
        for i in range(0, len(horde)):
            if not horde[i].isDead:
                horde[i].setKnockback(slime.statBlock.ATTACK - horde[i].statBlock.DEFENSE)
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
        if sword.swing and not scenario.Win:
            DISPLAYSURF.blit(sword.image, sword.pos)
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
        if slime.statBlock.HEALTH <= 0 and slime.deathFrame <= 0:
            #slimes timer is only 0 after his conclusion animation, and therefore he is ready to exit the scenario
            return
        if scenario.Win and slime.deathFrame <= 0:
            scenario.reset()
            return None
        for enemy in horde:
            if enemy.isDead and enemy.deathAnimFrame == 0:
                horde.remove(enemy)

        DISPLAYSURF.blit(overlay, (0, 0))
        # draw the slime to the screen
        DISPLAYSURF.blit(slime.image, slime.position)
        # if q is pressed, quit
        if pygame.key.get_pressed()[K_q]:
            return
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


def runScenario(Scenario):
    """Run this Scenario... Calls playScenario"""
    playScenario(Scenario)


# Program Start

# this runs the titlescreen, and returns the users selection
logging.info("Game Initialized")
nextStep = TitleSlide.runTitle(DISPLAYSURF)
"""nextstep is either going to be Q, or it will be the name of a scenario that can be found
in ANTHOLOGY.ANTHOLOGY 
if it is the latter, go get it and set that as the current scenario, then run it.
Otherwise:"""
if nextStep == 'Q' or nextStep == 'quit-button':
    pygame.quit()
    sys.exit()
# when TitleScreen Returns, it will have an Event generated.
# Currently, the only two events to be implemented are the
# "go to gameplay" event to move to the gameplay loop
# and the "quit" event that ends the game
if nextStep != "":
    print("Playing " + nextStep)
    runScenario(Anthology.retrieveScenario(nextStep))
    nextStep = TitleSlide.runTitle(DISPLAYSURF)
while (nextStep != ''):
    if nextStep == 'Q' or nextStep == 'quit-button':
        pygame.quit()
        sys.exit()
    # clears the event queue so that the gameplay starts fresh
    runScenario(Anthology.retrieveScenario(nextStep))
    nextStep = TitleSlide.runTitle((DISPLAYSURF))
