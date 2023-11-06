import pygame
from pygame import *

HPBARWIDE = 50
HPBARHIGH = 3
class HealthBar(pygame.sprite.Sprite):
    # 2 rectangle objects (may need to be sprites), that represent the 2 parts of the
    # bar
    remainingHP = sprite.Sprite()
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
        self.show = True
        # the image will be the merging of the 2 sprites, total firrst then remaining

        # the position will be HPBARHIGH above the monsters sprite
        # This will have to be set in the monsters program

    def noShow(self):
        self.HPBAR_SURFACE.set_colorkey((178, 34, 34))
    def update(self, target):
        if(self.show):
            self.HP_Remaining_Wide = int(HPBARWIDE * (target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
            self.HPBAR_SURFACE.fill((0, 0, 0))
            if(self.HP_Remaining_Wide <=0):
                self.HP_Remaining_Wide = 0
            self.HP_Remaining = pygame.Surface((self.HP_Remaining_Wide, HPBARHIGH))
            self.HP_Remaining.fill((178, 34, 34))
            # Blit the remaining HP onto the HPSURFACE
            self.HPBAR_SURFACE.blit(self.HP_Remaining, (0, 0))

    def dump(self):
        return "HPBARWIDE: " + str(HPBARWIDE) + "\n" + "HP_Remaining_Wide: " + str(self.HP_Remaining_Wide)

