# This file will be used to store the screen overlay.
import pygame.sprite
import SlimesDelight
import sys

#This initializes the font module as using "monospace"
#May change this later
font = pygame.font.SysFont("monospace", 25, bold = True)

META = (open('Meta.txt').read()).split(':')
WINX = int(META[0])
WINY = int(META[1])

# this will hold the sprite that will be the current Health bar
HealthBar = pygame.sprite.Sprite()
HPBARWIDE = (2 / 3) * WINY
HPBARHIGH = ((1 / 50) * WINX) + 15


# it will include the Health Bar for the Slime

class PlayerHealthBar(pygame.sprite.Sprite):
    # 2 rectangle objects (may need to be sprites), that represent the 2 parts of the
    # bar
    #I want the Screen to Show, in numbers, how much health Slime has remaining
    # On the health bar, Justified to the left.


    remainingHP = pygame.sprite.Sprite()
    pos = (0, 0)
    HPBAR_SURFACE = pygame.Surface((HPBARWIDE, HPBARHIGH))
    HP_Remaining = pygame.Surface((HPBARWIDE, HPBARHIGH))
    HP_Remaining_Wide = 0
    Hp_Remaining_Text = font.render("0/0", False, (1,1,1,1))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (0, 0)
        self.HPBAR_SURFACE = pygame.Surface((HPBARWIDE, HPBARHIGH))
        self.HPBAR_SURFACE.fill((178, 34, 34))
        self.HP_Remaining.fill((178, 34, 34))
        self.HP_Remaining_Wide = 0
        self.HP_Remaining_Text = font.render("0/0", False, (1,1,1,1))
        # the image will be the merging of the 2 sprites, total first then remaining
        #The text displaying the total HP will be justified to the left

    def update(self, target):
        #set the rendered text to be the current health over the Total Health
        self.HP_Remaining_Text = font.render("Health: " + str(target.statBlock.HEALTH) + " / " + str(
            target.statBlock.TOTALHEALTH), False, (1,1,1,1))
        self.HP_Remaining_Wide = int(HPBARWIDE * (target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
        # logging.info("current Attributes:\nHP: " + str(target.statBlock.HEALTH) + "\nTOTALHEALTH: " + str(target.statBlock.TOTALHEALTH) + "\nRATIO: " + str(target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
        self.HPBAR_SURFACE.fill((0, 0, 0))
        self.HP_Remaining = pygame.Surface((self.HP_Remaining_Wide, HPBARHIGH))
        self.HP_Remaining.fill((178, 34, 34))
        # Blit the remaining HP onto the HPSURFACE
        self.HPBAR_SURFACE.blit(self.HP_Remaining, (0, 0))
        #Blit the number vsalues onto the HPSURFACE
        self.HPBAR_SURFACE.blit(self.HP_Remaining_Text, (0,0))



# and Q to quit in the corner.

