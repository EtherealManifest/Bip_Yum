"""when the game runs gameplay, it needs to read in a scenario. the scenario will consist of
enemies and locations, the background tiles, and the music. the scenario will be loaded at gameplay, and
then run until a completion event occurs, be it the player dying or the enemies all dying.
once the scenario is complete, this main file will return all the local variables to their
defaults and await the next scenario
"""
import Armory
import SlimesDelight


class Scenario:
    """Scenarios are the 'Levels' of this little game.

    They are the complex structures that are based on almost every other module in this project"""
    # an array of monsters
    horde = []
    """Holds the Monsters"""
    # an array of setPieces
    trove = []
    """Holds the setPieces"""
    # the background
    vista = []
    """Holds the background"""
    # slimes original position
    slimyPOS = (0, 0)
    """The position for the Slime"""
    # slimes weapon
    weapon = Armory.Weapon()
    """The primary weapon for this scenario"""
    # slime himself
    TheWanderer = SlimesDelight.Slime()
    """The slime himself"""

    def __init__(self):
        """Initializes this scenario"""
        self.name = ""
        # an array of monsters
        self.horde = []
        """Holds the Monsters"""
        # an array of setPieces
        self.trove = []
        """Holds the setPieces"""
        # the background
        self.vista = []
        """Holds the background"""
        # slimes original position
        self.slimyPOS = (0, 0)
        """The Player's position"""
        # slimes weapon
        self.weapon = Armory.Weapon()
        """The primary weapon for this Scenario"""
        # slime himself
        self.TheWanderer = SlimesDelight.Slime()
        """The player for this Scenario"""
        self.Win = False
        """Whether this scenario is complete or Not"""
        self.instructions = None
        # Set this to true when displaying screen text. this makes is to that if there is no text to be shown, the text
        # queue does not need to be checked
        self.isScreenText = False
        # each text item in the next list will be a three-tuple of the text to display and the place to show it, and
        # whether it should be shown (string, (posx, posy), bool)
        self.screenText = []

    def setTheScene(self, _horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer):
        """Set all of the attributes for this scenario. Requires a LOT of legwork, usually."""
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
        """Delete this Scenario"""
        del self.trove
        del self.horde
        del self.vista
        del self.slimyPOS
        del self.weapon
        del self.TheWanderer
        del self.Win

    def winCondition(self, horde):
        """The default win condition"""
        if len(horde) == 0:
            self.Win = True

    # this allows the function that calls this to get a copy of this scenario, not the actual thing. Ideally. Hopefully
    def generate(self):
        """Create this Scenario"""
        temp = self
        return temp
