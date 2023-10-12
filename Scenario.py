'''when the game runs gameplay, it needs to read in a scenario. the scenario will consist of
enemies and locations, the background tiles, and the music. the scenario will be loaded at gameplay, and
then run until a completion event occurs, be it the player dying or the enemies all dying.
once the scenario is complete, this main file will return all the local variables to their
defaults and await the next scenario
'''
import MonsterMash, SlimesDelight, GroundMaker, Jukebox, Armory, SetPeice
from pathlib import Path


class Scenario:
    # an array of monsters
    horde = []
    # an array of setPieces
    trove = []
    # the background
    vista = []
    locale = Path("")
    # slimes original position
    slimyPOS = (0, 0)
    # slimes weapon
    weapon = Armory.Weapon()
    # slime himself
    TheWanderer = SlimesDelight.Slime()

    def __init__(self, _horde, _trove, _vista, _locale, _slimyPOS, _weapon, _TheWanderer):
        self.horde = _horde
        self.trove = _trove
        # vista is not defined because BuildTheLand needs to act on Locale First
        self.locale = _locale
        self.slimyPOS = _slimyPOS
        self.weapon = _weapon
        self.TheWanderer = _TheWanderer

    def loadScenario(self):
        # the goal of this method is to get everything as a surface.
        # this group will be passed to the main function and blit, and from there
        # relevant updates will be called.
        self.vista = GroundMaker.BuildTheLand(self.locale)
