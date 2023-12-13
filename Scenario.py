"""when the game runs gameplay, it needs to read in a scenario. the scenario will consist of
enemies and locations, the background tiles, and the music. the scenario will be loaded at gameplay, and
then run until a completion event occurs, be it the player dying or the enemies all dying.
once the scenario is complete, this main file will return all the local variables to their
defaults and await the next scenario
"""
import Armory
import SlimesDelight


class Scenario:
    # an array of monsters
    horde = []
    # an array of setPieces
    trove = []
    # the background
    vista = []
    # slimes original position
    slimyPOS = (0, 0)
    # slimes weapon
    weapon = Armory.Weapon()
    # slime himself
    TheWanderer = SlimesDelight.Slime()

    def __init__(self):
        self.name = ""
        # an array of monsters
        self.horde = []
        # an array of setPieces
        self.trove = []
        # the background
        self.vista = []
        # slimes original position
        self.slimyPOS = (0, 0)
        # slimes weapon
        self.weapon = Armory.Weapon()
        # slime himself
        self.TheWanderer = SlimesDelight.Slime()
        self.Win = False
        self.instructions = None
        # Set this to true when displaying screen text. this makes is to that if there is no text to be shown, the text
        # queue does not need to be checked
        self.isScreenText = False
        # each text item in the next list will be a three-tuple of the text to display and the place to show it, and
        # whether it should be shown (string, (posx, posy), bool)
        self.screenText = []

    def setTheScene(self, _horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer):
        # an array of monsters
        self.horde = _horde
        # an array of setPieces
        self.trove = _trove
        # the background
        self.vista = _vista
        # slimes original position
        self.slimyPOS = _slimyPOS
        # slimes weapon
        self.weapon = _weapon
        # slime himself
        self.TheWanderer = _TheWanderer
        self.Win = False

    def __del__(self):
        del self.trove
        del self.horde
        del self.vista
        del self.slimyPOS
        del self.weapon
        del self.TheWanderer
        del self.Win

    def winCondition(self, horde):
        if len(horde) == 0:
            self.Win = True

    # this allows the function that calls this to get a copy of this scenario, not the actual thing. Ideally. Hopefully
    def generate(self):
        temp = self
        return temp
