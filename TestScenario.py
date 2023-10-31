import Scenario, Jukebox, PropStorage, Arsenal, SlimesDelight, Atlas, MonsterMash, copy, Crypt
import pygame
data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])

wolf1 = Crypt.WOLF()
wolf2 = Crypt.WOLF()
wolf1.Name = "Wolf1"
wolf2.Name = "Wolf2"
wolf2.setPosition((500, 500))
#FIXME: Set horde to nothing to test the setpieces
_horde = []

_trove = [PropStorage.DEFAULTSETPIECE]
#this has to be called as a function, otherwise will just paint as lava
_vista = Atlas.DESERT()

_slimyPOS = (WINX/2, WINY/2)
_weapon = Arsenal.BLUESWORD
_TheWanderer = SlimesDelight.Slime()

SCENARIO = Scenario.Scenario(_horde, _trove, _vista, _slimyPOS, _weapon, _TheWanderer)
