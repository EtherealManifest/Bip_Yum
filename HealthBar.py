import pygame
from pygame import *

HPBARWIDE = 50
"""Global width of the Health Bar."""
HPBARHIGH = 3
"""Global height of the HP Bars."""

class HealthBar(pygame.sprite.Sprite):
    """A red bar that indicates the Enemies Health."""
    # 2 rectangle objects (may need to be sprites), that represent the 2 parts of the
    # bar
    remainingHP = sprite.Sprite()
    pos = (0, 0)
    HPBAR_SURFACE = pygame.Surface((HPBARWIDE, HPBARHIGH))
    """Base for the health bar."""
    HP_Remaining = pygame.Surface((HPBARWIDE, HPBARHIGH))
    HP_Remaining_Wide = 0

    def __init__(self):
        """Initializes this HPBAR to be solid red, and shown"""
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
        """Run this prior to displaying it to stop the Health bar from being shown"""
        self.HPBAR_SURFACE.set_colorkey((178, 34, 34))

    def update(self, target):
        """Modify the HPBAR to reflect the current health of the monster it's assiciated with"""
        if self.show:
            self.HP_Remaining_Wide = int(HPBARWIDE * (target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
            self.HPBAR_SURFACE.fill((0, 0, 0))
            if self.HP_Remaining_Wide <= 0:
                self.HP_Remaining_Wide = 0
            self.HP_Remaining = pygame.Surface((self.HP_Remaining_Wide, HPBARHIGH))
            self.HP_Remaining.fill((178, 34, 34))
            # Blit the remaining HP onto the HPSURFACE
            self.HPBAR_SURFACE.blit(self.HP_Remaining, (0, 0))

    def dump(self):
        """Return a string translation of the Status of this HP Bar"""
        return "HPBARWIDE: " + str(HPBARWIDE) + "\n" + "HP_Remaining_Wide: " + str(self.HP_Remaining_Wide)
