#THis is the collection for different scenarios

import Scenario, Jukebox, PropStorage, Arsenal, SlimesDelight, Atlas, MonsterMash, copy, Crypt
import pygame
data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])



class DesertScenario(Scenario.Scenario):
    def __init__(self):
        super().__init__()
        self.name = "Desert Battle"
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
        self.__init__()

    #to win, kill teh wolves. This can be checked by whether or not the first and second
    # enemies are named wolf1 and wolf2
    def winCondition(self, horde):
        if (horde[0].Name != "Wolf1" and horde[0].Name != "Wolf2") and horde[1].Name != "Wolf2":
            self.Win = True
        else:
            self.Win = False
    def alldestroyed(self):
        for pieces in self.trove:
            if pieces.destroyable != False:
                return False
        return True

class PlainsScenario(Scenario.Scenario):
    def __init__(self):
        super().__init__()
        #FIXME: CHANGE ENEMIES
        self.name = "Plains Adventure"
        wolf1 = Crypt.WOLF()
        wolf2 = Crypt.WOLF()
        wolf1.Name = "Wolf1"
        wolf2.Name = "Wolf2"
        wolf2.setPosition((500, 500))
        _horde = [wolf1, wolf2]
        #FIXME: CHANGE TROVE
        _trove = [PropStorage.Round_Cactus(), PropStorage.Tall_Cactus(), PropStorage.TumbleweedLord()]
        # this has to be called as a function, otherwise will just paint as lava
        _vista = Atlas.GRASS()
        _slimyPOS = (WINX / 2, WINY / 2)
        _weapon = Arsenal.BLUESWORD
        _TheWanderer = SlimesDelight.Slime()
        super().setTheScene(_horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer)
        self.Win = False
    def reset(self):
        self.__init__()
    #should see if the wolves are dead. may not work right.
    def winCondition(self, horde):
        pass
    def alldestroyed(self):
        for pieces in self.trove:
            if pieces.destroyable != False:
                return False
        return True


DESERT = DesertScenario()

ANTHOLOGY = [DESERT]


#in the menu, the button related to each scenario will return the name for that scenario when it is pressed.
#the main menu will then call this, passing the name as a parameter. return the scenario they are looking for.
def retrieveScenario(target_name):
    for scenario in ANTHOLOGY:
        if scenario.name == target_name:
            return scenario
    #return nothing to indicate that the scenario could not be found.
    return ""

