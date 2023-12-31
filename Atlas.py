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
    return GroundMaker.BuildTheLand(WINX, WINY, PLAINS)

def TEST():
    return GroundMaker.BuildTheLand(WINX, WINY, LAB)

def DESERT():
    return GroundMaker.BuildTheLand(WINX, WINY, SANDS)


def LAVA():
    return GroundMaker.BuildTheLand(WINX, WINY, FLAMES)


def SPACE():
    return GroundMaker.BuildTheLand(WINX, WINY, SPACES)
