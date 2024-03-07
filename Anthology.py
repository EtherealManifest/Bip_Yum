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

class DesertSandstormScenario(Scenario.Scenario):
    """Scenario with blowing tumbleweeds and attacking coyotes.

    Goal: Survive. Shows off mechanics."""
    def __init__(self):
        """initializes this scenario"""
        super().__init__()
        self.name = "Desert Sandstorm"
        _horde = []
        round_1 = PropStorage.Round_Cactus()
        round_1.setPos((100, 250))
        round_2 = PropStorage.Round_Cactus()
        round_2.setPos((110, 350))
        round_3 = PropStorage.Round_Cactus()
        round_3.setPos((300, 50))
        tall_1 = PropStorage.Tall_Cactus()
        tall_1.setPos((10, 25))
        tall_2 = PropStorage.Tall_Cactus()
        tall_2.setPos((200, 200))
        tall_3 = PropStorage.Tall_Cactus()
        tall_3.setPos((175, 175))
        _trove = [round_1, round_2, round_3, tall_1, tall_2, tall_3,PropStorage.TumbleweedLord()]
        # this has to be called as a function, otherwise will just paint as lava
        _vista = Atlas.DESERT()
        _slimyPOS = (WINX / 2, WINY / 2)
        _weapon = Arsenal.BLUESWORD
        _TheWanderer = SlimesDelight.Slime()
        super().setTheScene(_horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer)
        self.Win = False

    def reset(self):
        """Returns this scenario to its native state"""
        self.__init__()

    # to win, kill teh wolves. This can be checked by whether or not the first and second
    # enemies are named wolf1 and wolf2
    def winCondition(self, horde, trove):
        """Determines if the two wolves are dead or not."""
        return False

    def alldestroyed(self):
        """Checks to see if there are any setPeices in the Trove"""
        for pieces in self.trove:
            if pieces.destroyable:
                return False
        return True

class DesertScenario(Scenario.Scenario):
    """Scenario with blowing tumbleweeds and attacking coyotes.

    Goal: Defeat the coyotes to win."""
    def __init__(self):
        """initializes this scenario"""
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
        """Returns this scenario to its native state"""
        self.__init__()

    # to win, kill teh wolves. This can be checked by whether or not the first and second
    # enemies are named wolf1 and wolf2
    def winCondition(self, horde, trove):
        """Determines if the two wolves are dead or not."""
        if (horde[0].Name != "Wolf1" and horde[0].Name != "Wolf2") and horde[1].Name != "Wolf2":
            self.Win = True
        else:
            self.Win = False

    def alldestroyed(self):
        """Checks to see if there are any setPeices in the Trove"""
        for pieces in self.trove:
            if pieces.destroyable:
                return False
        return True

class DesertsWrathScenario(Scenario.Scenario):
    """Scenario with blowing tumbleweeds and attacking coyotes.

    Goal: Defeat the coyotes to win."""
    def __init__(self):
        """initializes this scenario"""
        super().__init__()
        self.name = "Desert's Wrath"
        wolf1 = Crypt.WOLF()
        wolf2 = Crypt.WOLF()
        wolf3 = Crypt.WOLF()
        wolf1.Name = "Wolf1"
        wolf2.Name = "Wolf2"
        wolf3.Name = "Wolf3"
        wolf2.setPosition((500, 500))
        wolf3.setPosition((150, 666))
        desertWarden = PropStorage.TumbleweedLord()
        desertWarden.wrath = 10
        desertWarden.spawnRate = 1
        _horde = [wolf1, wolf2, wolf3]
        _trove = [PropStorage.Round_Cactus(), PropStorage.Tall_Cactus(), desertWarden]
        _trove += self.cactusSwarm()
        # this has to be called as a function, otherwise will just paint as lava
        _vista = Atlas.DESERT()
        _slimyPOS = (WINX / 2, WINY / 2)
        _weapon = Arsenal.BLUESWORD
        _TheWanderer = SlimesDelight.Slime()
        super().setTheScene(_horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer)
        self.Win = False

    def reset(self):
        """Returns this scenario to its native state"""
        self.__init__()

    def cactusSwarm(self):
        foliage = []
        for i in range(10):
            newCactus = PropStorage.Tall_Cactus()
            newCactus.setPos((random.randrange(0,WINX), random.randrange(0,WINY)))
            foliage.append(newCactus)
        for i in range(10):
            newCactus = PropStorage.Round_Cactus()
            newCactus.setPos((random.randrange(0,WINX), random.randrange(0,WINY)))
            foliage.append(newCactus)
        return foliage

    # to win, kill teh wolves. This can be checked by whether or not the first and second
    # enemies are named wolf1 and wolf2
    def winCondition(self, horde, trove):
        """Determines if the two wolves are dead or not."""
        if (horde[0].Name != "Wolf1" and horde[0].Name != "Wolf2" and horde[0].Name != "Wolf3") and horde[1].Name != "Wolf2":
            self.Win = True
        else:
            self.Win = False

    def alldestroyed(self):
        """Checks to see if there are any setPeices in the Trove"""
        for pieces in self.trove:
            if pieces.destroyable:
                return False
        return True

class PlainsScenario(Scenario.Scenario):
    """Plains Scenario, eat the Cabbages!

    Four Aggrabbages will try to attack the player.
    Eat all 5 cabbages to win"""
    def __init__(self):
        """Initializes this Scenario, creating monsters and cabbages."""
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
        """Resets this scenario to it's native form"""
        self.__init__()

    # should see if the wolves are dead. may not work right.
    def winCondition(self, horde, trove):
        """Checks to see if there are any cabbages in teh trove"""
        for cabbage in self.trove:
            if not cabbage.eaten:
                return
        self.Win = True

class GrassAdventure(Scenario.Scenario):

    def __init__(self):
        """initializes this scenario"""
        super().__init__()
        self.name = "Grass Adventure"
        _horde = []
        exit = PropStorage.exit()
        _trove = [exit]
        # this has to be called as a function, otherwise will just paint as lava
        _vista = Atlas.GRASS()
        _slimyPOS = (WINX / 2, WINY / 2)
        _weapon = Arsenal.BLUESWORD
        _TheWanderer = SlimesDelight.Slime()
        super().setTheScene(_horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer)
        self.Win = False

    def reset(self):
        """Returns this scenario to its native state"""
        self.__init__()

    # to win, kill teh wolves. This can be checked by whether or not the first and second
    # enemies are named wolf1 and wolf2
    def winCondition(self, horde, trove):
        for setpiece in trove:
            if setpiece.triggered:
                self.Win = True



class TestZoneScenario(Scenario.Scenario):
    """Boss arena! Defeat the Omen Character to win!"""
    def __init__(self):
        """Initializes this scenario, creates Omen."""
        super().__init__()
        self.name = "Testing Zone I"
        Omen = Crypt.OMEN()
        Omen.Name = ("Omar")
        Omen.setPosition((4, 8))
        _horde = [Omen]
        _trove = []
        instructionText = font.render("Push it to the Limit!", False, (1.0, 1.0, 0.0, 1.0))
        self.instructions = (instructionText, (WINX / 2 - 20, WINY - 45), True)
        _vista = Atlas.TEST()
        _slimyPOS = (WINX / 2, WINY / 2)
        _weapon = Arsenal.REDSWORD
        _TheWanderer = SlimesDelight.Slime()
        super().setTheScene(_horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer)
        self.Win = False

    def reset(self):
        """Returns this scenario to it's native form"""
        self.__init__()

    # should see if the wolves are dead. may not work right.
    def winCondition(self, horde, trove):
        """Checks if the Horde is empty, meaning Omen is defeated"""
        if len(horde) == 0:
            self.Win = True

class TestHellScenario(Scenario.Scenario):
    """Boss arena! Defeat the Omen Character to win!"""
    def __init__(self):
        """Initializes this scenario, creates Omen."""
        super().__init__()
        self.name = "Testing Zone II"
        Omen_1 = Crypt.OMEN()
        Omen_1.Name = ("Omar")
        Omen_1.setKnockback(16)
        Omen_1.setPosition((4, 8))
        Omen_2 = Crypt.OMEN()
        Omen_2.setKnockback(16)
        Omen_2.Name = ("Omary")
        Omen_2.setPosition((500, 500))
        _horde = [Omen_1, Omen_2]
        _trove = []
        instructionText = font.render("Push it to the Limit!", False, (1.0, 1.0, 0.0, 1.0))
        self.instructions = (instructionText, (WINX / 2 - 20, WINY - 45), True)
        _vista = Atlas.TEST()
        _slimyPOS = (WINX / 2, WINY / 2)
        _weapon = Arsenal.GREENSWORD
        _TheWanderer = SlimesDelight.Slime()
        super().setTheScene(_horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer)
        self.Win = False

    def reset(self):
        """Returns this scenario to it's native form"""
        self.__init__()

    # should see if the wolves are dead. may not work right.
    def winCondition(self, horde, trove):
        """Checks if the Horde is empty, meaning Omen is defeated"""
        if len(horde) == 0:
            self.Win = True



TEST = TestZoneScenario()
"""TEST is the battle with Omen"""
DEATHTEST = TestHellScenario()
"""SuperBoss???"""
DESERT = DesertScenario()
"""The fight against the wolves"""
DESERTSANDSTORM = DesertSandstormScenario()
"""Aimless Desert Wanderings"""
DESERTSWRATH = DesertsWrathScenario()
"""Feel the wrath of the sands"""
PLAINS = PlainsScenario()
"""The mad dash for cabbages"""
GRASS = GrassAdventure()
"""No Threat, Good for Demonstrating"""
ANTHOLOGY = [GRASS, DESERT, PLAINS, DESERTSANDSTORM, DESERTSWRATH, TEST, DEATHTEST]
"""A collection of all of the scenarios in one place"""


# in the menu, the button related to each scenario will return the name for that scenario when it is pressed.
# the main menu will then call this, passing the name as a parameter. return the scenario they are looking for.
def retrieveScenario(target_name):
    """Searches ANTHOLOGY for the scenario with target_name"""
    for scenario in ANTHOLOGY:
        if scenario.name == target_name:
            scenario.reset()
            return scenario
    # return nothing to indicate that the scenario could not be found.
    return "Is... is " + target_name + " a scenario? I don't know her."


# returns a tuple of the text, the position (tuple) and True
def text_to_surface(text):
    """returns the text as rendered instruction text"""
    instructionText = font.render(text, False, (1.0, 1.0, 0.0, 1.0))
    instructions = (instructionText, (WINX / 2 - instructionText.get_width() / 2, WINY - 45), True)
    return instructions
