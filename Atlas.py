# define the different backgrounds here
import GroundMaker
from pathlib import Path

data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])

PLAINS = Path("./GroundPanels/Grass/")
SANDS = Path("./GroundPanels/Desert/")
FLAMES = Path("./GroundPanels/Lava/")
SPACES = Path("./GroundPanels/Space/")
LAB = Path("./GroundPanels/TestZone/")


# each of these is a group of sprites
def GRASS():
    """Builds the background to fit the screen size using the PLAINS background Panels"""
    return GroundMaker.BuildTheLand(WINX, WINY, PLAINS)

def TEST():
    """Builds the background to fit the screen size using the LAB background Panels"""
    return GroundMaker.BuildTheLand(WINX, WINY, LAB)

def DESERT():
    """Builds the background to fit the screen size using the SANDS background Panels"""
    return GroundMaker.BuildTheLand(WINX, WINY, SANDS)


def LAVA():
    """Builds the background to fit the screen size using the FLAMES background Panels"""
    return GroundMaker.BuildTheLand(WINX, WINY, FLAMES)


def SPACE():
    """Builds the background to fit the screen size using the SPACES background Panels"""
    return GroundMaker.BuildTheLand(WINX, WINY, SPACES)
