import pygame
from pygame import *

import HealthBar
import logging

logging.basicConfig(filename='MainLog.txt', level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s -  %(message)s - MAIN')


# a healthBar will consist of 2 sprites, a black one underneath that
# denotes total health, and a red one above that denotes health remaining
# As the monster takes damage, the red rectangle will get smaller to the left.

class StatBlock():
    """Attribute for this creature"""
    TOTALHEALTH = 0
    HEALTH = 0
    ATTACK = 0
    DEFENSE = 0
    ARCANA = 0
    ARCDEF = 0
    SPEED = 0
    LUCK = 0
    pos = (0, 0)
    HealthBar = HealthBar.HealthBar()

    def __init__(self):
        """initialize the stats for this statBlock"""
        self.TOTALHEALTH = 0
        self.HEALTH = 0
        self.ATTACK = 0
        self.DEFENSE = 0
        self.ARCANA = 0
        self.ARCDEF = 0
        self.SPEED = 0
        self.LUCK = 0
        self.HealthBar = HealthBar.HealthBar()
        self.pos = (0, 0)

    def setStats(self, HP, ATK, DEF, ARC, ARD, SPD, LCK):
        """Set this Statblocks Attributes"""
        # logging.info("SETTING STATS")
        self.TOTALHEALTH = HP
        self.HEALTH = HP
        self.ATTACK = ATK
        self.DEFENSE = DEF
        self.ARCANA = ARC
        self.ARCDEF = ARD
        self.SPEED = SPD
        self.LUCK = LCK
        self.pos = (0, 0)

    def getStats(self):
        """return a string representation of this StatBlock"""
        return [self.TOTALHEALTH, self.HEALTH, self.ATTACK, self.DEFENSE, self.ARCANA,
                self.ARCDEF, self.SPEED, self.LUCK, self.pos]

    def showStats(self):
        """returns a string representation of the health Attributes"""
        return ("TOTAL HEALTH: " + str(self.TOTALHEALTH)
                + "\nHealth: " + str(self.HEALTH))

    def setPos(self, newPos):
        "Set the position attribute"
        self.pos = newPos
