# This file will be used to store the screen overlay.
import pygame.sprite
import SlimesDelight

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
    remainingHP = pygame.sprite.Sprite()
    pos = (0, 0)
    HPBAR_SURFACE = pygame.Surface((HPBARWIDE, HPBARHIGH))
    HP_Remaining = pygame.Surface((HPBARWIDE, HPBARHIGH))
    HP_Remaining_Wide = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (0, 0)
        self.HPBAR_SURFACE = pygame.Surface((HPBARWIDE, HPBARHIGH))
        self.HPBAR_SURFACE.fill((178, 34, 34))
        self.HP_Remaining.fill((178, 34, 34))
        self.HP_Remaining_Wide = 0
        # the image will be the merging of the 2 sprites, total first then remaining

        # the position will be HPBARHIGH above the monsters sprite
        # This will have to be set in the monsters program

    def update(self, target):
        self.HP_Remaining_Wide = int(HPBARWIDE * (target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
        # logging.info("current Attributes:\nHP: " + str(target.statBlock.HEALTH) + "\nTOTALHEALTH: " + str(target.statBlock.TOTALHEALTH) + "\nRATIO: " + str(target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
        self.HPBAR_SURFACE.fill((0, 0, 0))
        self.HP_Remaining = pygame.Surface((self.HP_Remaining_Wide, HPBARHIGH))
        self.HP_Remaining.fill((178, 34, 34))
        # Blit the remaining HP onto the HPSURFACE
        self.HPBAR_SURFACE.blit(self.HP_Remaining, (0, 0))

# the name of the area
# the number of monsters remaining
# and Q to quit in the corner.
