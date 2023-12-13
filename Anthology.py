# THis is the collection for different scenarios

import pygame

import Arsenal
import Atlas
import Crypt
import PropStorage
import Scenario
import SlimesDelight
import math
import random

data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])
font = pygame.font.SysFont("Planet Comic", math.ceil(.03 * WINY))


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

    # to win, kill teh wolves. This can be checked by whether or not the first and second
    # enemies are named wolf1 and wolf2
    def winCondition(self, horde):
        if (horde[0].Name != "Wolf1" and horde[0].Name != "Wolf2") and horde[1].Name != "Wolf2":
            self.Win = True
        else:
            self.Win = False

    def alldestroyed(self):
        for pieces in self.trove:
            if pieces.destroyable:
                return False
        return True


class PlainsScenario(Scenario.Scenario):
    def __init__(self):
        super().__init__()
        self.name = "Plains Adventure"
        aggrabbage1 = Crypt.AGGRABBAGE()
        aggrabbage2 = Crypt.AGGRABBAGE()
        aggrabbage3 = Crypt.AGGRABBAGE()
        aggrabbage4 = Crypt.AGGRABBAGE()
        aggrabbage1.Name = "Aggrabbage1"
        aggrabbage2.Name = "Aggrabbage2"
        aggrabbage3.Name = "Aggrabbage3"
        aggrabbage4.Name = "Aggrabbage4"

        aggrabbage2.setPosition((500, 500))
        aggrabbage4.setPosition((300, 212))
        aggrabbage3.setPosition((400, 400))
        _horde = [aggrabbage1, aggrabbage2, aggrabbage3, aggrabbage4]
        _trove = []
        instructionText = font.render("Eat the Cabbages!", False, (1.0, 1.0, 0.0, 1.0))
        self.instructions = (instructionText, (WINX / 2 - 20, WINY - 45), True)
        for i in range(0, 5):
            crop = PropStorage.Cabbage()
            crop.setPos((int(random.randrange(0, WINX)), int(random.randrange(0, WINY))))
            _trove.append(crop)
        _vista = Atlas.GRASS()
        _slimyPOS = (WINX / 2, WINY / 2)
        _weapon = Arsenal.GREENSWORD
        _TheWanderer = SlimesDelight.Slime()
        super().setTheScene(_horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer)
        self.Win = False
        self.instructions = ("Eat the Cabbages!", (WINY - 30, (1 / 2) * WINX - 30), True)

    def reset(self):
        self.__init__()

    # should see if the wolves are dead. may not work right.
    def winCondition(self, horde):
        for cabbage in self.trove:
            if not cabbage.eaten:
                return
        self.Win = True


DESERT = DesertScenario()
PLAINS = PlainsScenario()
ANTHOLOGY = [DESERT, PLAINS]


# in the menu, the button related to each scenario will return the name for that scenario when it is pressed.
# the main menu will then call this, passing the name as a parameter. return the scenario they are looking for.
def retrieveScenario(target_name):
    for scenario in ANTHOLOGY:
        if scenario.name == target_name:
            scenario.reset()
            return scenario
    # return nothing to indicate that the scenario could not be found.
    return "Is... is " + target_name + " a scenario? I don't know her."


# returns a tuple of the text, the position (tuple) and True
def text_to_surface(text):
    instructionText = font.render(text, False, (1.0, 1.0, 0.0, 1.0))
    instructions = (instructionText, (WINX / 2 - instructionText.get_width() / 2, WINY - 45), True)
    return instructions
