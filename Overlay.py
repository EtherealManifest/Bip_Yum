# This file will be used to store the screen overlay.
import pygame.sprite
import SlimesDelight
import sys
import math

META = (open('Meta.txt').read()).split(':')
WINX = int(META[0])
WINY = int(META[1])

# All objects for the overlay will be blit onto the overlay
# The overlay is a surface that is the size of the screen

# this will hold the sprite that will be the current Health bar
HealthBar = pygame.sprite.Sprite()
HPBARWIDE = (2 / 3) * WINY
HPBARHIGH = ((1 / 50) * WINX) + 15

# This initializes the font module as using "Planet Comic" Font
# May change this later
font = pygame.font.SysFont("Planet Comic", math.ceil(1.2 * HPBARHIGH))




class PlayerHealthBar(pygame.sprite.Sprite):
    # 2 rectangle objects (may need to be sprites), that represent the 2 parts of the
    # bar
    # I want the Screen to Show, in numbers, how much health Slime has remaining
    # On the health bar, Justified to the left.

    remainingHP = pygame.sprite.Sprite()
    pos = (0, 0)
    HPBAR_CASE_WIDTH = 4
    HPBAR_CASE = pygame.Surface((HPBARWIDE + HPBAR_CASE_WIDTH, HPBARHIGH + HPBAR_CASE_WIDTH))
    HPBAR_SURFACE = pygame.Surface((HPBARWIDE, HPBARHIGH))
    HP_Remaining = pygame.Surface((HPBARWIDE, HPBARHIGH))
    HP_Remaining_Wide = 0
    Hp_Remaining_Text = font.render("0/0", False, (1.0, 1.0, 0.0, 1.0))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (0, 0)
        self.HPBAR_SURFACE = pygame.Surface((HPBARWIDE, HPBARHIGH))
        self.HPBAR_SURFACE.fill((178, 34, 34))
        # The HPBAR_CASE is the outline for the HealthBar. The color for it is set here.
        self.HPBAR_CASE.fill((0, 89, 255))
        self.HP_Remaining.fill((178, 34, 34))
        self.HP_Remaining_Wide = 0
        self.HP_Remaining_Text = font.render("0/0", False, (255, 255, 255))
        # the image will be the merging of the 2 sprites, total first then remaining
        # The text displaying the total HP will be justified to the left

    def update(self, target):
        # set the rendered text to be the current health over the Total Health
        self.HP_Remaining_Text = font.render("Health: " + str(target.statBlock.HEALTH) + " / " + str(
            target.statBlock.TOTALHEALTH), False, (255, 255, 255))
        self.HP_Remaining_Wide = int(HPBARWIDE * (target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
        # logging.info("current Attributes:\nHP: " + str(target.statBlock.HEALTH) + "\nTOTALHEALTH: " + str(
        # target.statBlock.TOTALHEALTH) + "\nRATIO: " + str(target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
        self.HPBAR_SURFACE.fill((0, 0, 0))
        self.HP_Remaining = pygame.Surface((self.HP_Remaining_Wide, HPBARHIGH))
        self.HP_Remaining.fill((178, 34, 34))
        # Blit the remaining HP onto the HPSURFACE
        self.HPBAR_SURFACE.blit(self.HP_Remaining, (0, 0))
        # Blit the number vsalues onto the HPSURFACE
        self.HPBAR_SURFACE.blit(self.HP_Remaining_Text, (0, 0))
        # THis looks really complicated, but essentially this blits the health bar squarely in the middle of the
        # HPBAR_CASE, half of its height in, by half of its width
        self.HPBAR_CASE.blit(self.HPBAR_SURFACE, (self.HPBAR_CASE_WIDTH / 2, self.HPBAR_CASE_WIDTH / 2))


class Overlay(pygame.Surface):
    playerHealth = PlayerHealthBar()
    textSurf = pygame.Surface((WINX, WINY))
    textSurf.set_colorkey((1,1,1))
    textSurf.fill((1,1,1))
    text = "NotSet"
    textTime = 0

    def __init__(self):
        pygame.Surface.__init__(self, (WINX, WINY))
        # this fills the surface with a dummy color that is filtered out. It has to be here to be referenced by
        # the colorkey, that way no intentional pixels are cut. if the value needs changed later, then change it here
        self.fill((123, 123, 123))
        self.playerHealth = PlayerHealthBar()

    def update(self, target):
        self.playerHealth.update(target)
        # this makes the base layer transparent
        self.set_colorkey((123, 123, 123))
        #now the HPBAR is on this surface
        self.blit(self.playerHealth.HPBAR_CASE, self.playerHealth.pos)
        if(self.textTime >= 0):
            self.blit(self.textSurf, (0,0))
            self.textTime -= 1




    def showText(self, text, color = (255,255,255), size = 12, duration = 100):
        self.textTime = duration
        #define a text object
        textFont = pygame.font.SysFont("Planet Comic", size)
        #text is a surface. it needs a location to blit
        textLabel = font.render(text, False, color)

        textPosition = (
            (WINX + textLabel.get_width()) / 2,
            WINY - textLabel.get_height() - 10
            )
        self.textSurf.blit(textLabel, textPosition)

