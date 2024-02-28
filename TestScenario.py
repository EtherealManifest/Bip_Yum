import Scenario, PropStorage, Arsenal, SlimesDelight, Atlas, MonsterMash, copy, Crypt
import pygame
data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])



class TestScenario(Scenario.Scenario):
    """This is the testScenario, a remnant of development"""
    def __init__(self):
        """initializes this test scenario"""
        super().__init__()
        wolf1 = Crypt.WOLF()
        wolf2 = Crypt.WOLF()
        wolf1.Name = "Wolf1"
        wolf2.Name = "Wolf2"
        wolf2.setPosition((500, 500))
        _horde = [wolf1, wolf2]
        _trove = [PropStorage.Round_Cactus(), PropStorage.Tall_Cactus(), PropStorage.TumbleweedLord()]
        # this has to be called as a function, otherwise will just paint as lava
        _vista = Atlas.DESERT()
        _slimyPOS = (WINX / 2, WINY / 2)
        _weapon = Arsenal.BLUESWORD
        _TheWanderer = SlimesDelight.Slime()
        super().setTheScene(_horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer)
        self.Win = False
    def reset(self):
        """reset the default scenario"""
        self.__init__()


    def winCondition(self, horde):
        """just a stub... What was meant to be here???"""
        pass
    def alldestroyed(self):
        """is everyone Gone?"""
        for pieces in self.trove:
            if pieces.destroyable != False:
                return False
        return True