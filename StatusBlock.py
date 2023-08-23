import pygame
from pygame import *

import logging
logging.basicConfig(filename='MainLog.txt', level=logging.INFO, format='%(asctime)s -  %(levelname)s -  %(message)s - MAIN')


HPBARWIDE = 50
HPBARHIGH = 3
#a healthBar will consist of 2 sprites, a black one underneath that
#denotes total health, and a red one above that denotes health remaining
#As the monster takes damage, the red rectangle will get smaller to the left.
class HealthBar(pygame.sprite.Sprite):
    
    #2 rectangle objects (may need to be sprites), that represent the 2 parts of the
    #bar
    remainingHP = sprite.Sprite()
    pos = (0,0)
    HPBAR_SURFACE = pygame.Surface((HPBARWIDE, HPBARHIGH))
    HP_Remaining = pygame.Surface((HPBARWIDE, HPBARHIGH))
    HP_Remaining_Wide = 0
    
    

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (0,0)
        self.HPBAR_SURFACE = pygame.Surface((HPBARWIDE, HPBARHIGH))
        self.HPBAR_SURFACE.fill((178,34,34))
        self.HP_Remaining.fill((178,34,34))
        self.HP_Remaining_Wide = 0
        #the image will be the merging of the 2 sprites, total firrst then remaining
        
        #the position will be HPBARHIGH above the monsters sprite
        #This will have to be set in the monsters program
    def update(self, target):
        self.HP_Remaining_Wide = int(HPBARWIDE * (target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
        #logging.info("current Attributes:\nHP: " + str(target.statBlock.HEALTH) + "\nTOTALHEALTH: " + str(target.statBlock.TOTALHEALTH) + "\nRATIO: " + str(target.statBlock.HEALTH / target.statBlock.TOTALHEALTH))
        self.HPBAR_SURFACE.fill((0,0,0))
        #FIXME: CHANGE THE 1 to self.HP_Remaining.Wide
        self.HP_Remaining = pygame.Surface((self.HP_Remaining_Wide, HPBARHIGH))
        self.HP_Remaining.fill((178,34,34))
        #Blit the remaining HP onto the HPSURFACE
        self.HPBAR_SURFACE.blit(self.HP_Remaining, (0,0))

        
        
        
        

class StatBlock():
    TOTALHEALTH = 0
    HEALTH = 0
    ATTACK = 0
    DEFENSE = 0
    ARCANA = 0
    ARCDEF = 0
    SPEED = 0
    LUCK = 0
    pos = (0,0)
    HealthBar = HealthBar()
    def __init__(self):
        self.TOTALHEALTH = 0
        self.HEALTH = 0
        self.ATTACK = 0
        self.DEFENSE = 0
        self.ARCANA = 0
        self.ARCDEF = 0
        self.SPEED = 0
        self.LUCK = 0
        self.pos = (0,0)

    def setStats(self, HP, ATK, DEF, ARC, ARD, SPD, LCK):
        #logging.info("SETTING STATS")
        self.TOTALHEALTH = HP
        self.HEALTH = HP
        self.ATTACK = ATK
        self.DEFENSE = DEF
        self.ARCANA = ARC
        self.ARCDEF = ARD
        self.SPEED = SPD
        self.LUCK = LCK
        self.pos = (0,0)

    def showStats(self):
        return("TOTAL HEALTH: " +  str(self.TOTALHEALTH)
               + "\nHealth: "  + str(self.HEALTH))
    def setPos(self, newPos):
        self.pos = newPos
    
    
    
