import Armory
from pathlib import Path
import pygame


red = Armory.Weapon()
red.setImage(pygame.image.load(Path("./Weapon Sprites/red_sword_sprite.png")))
red.setStats(15, 150)

blue = Armory.Weapon()
blue.setImage(pygame.image.load(Path("./Weapon Sprites/blue_sword_sprite.png")))
blue.setStats(10, 100)

green = Armory.Weapon()
green.setImage(pygame.image.load(Path("./Weapon Sprites/green_sword_sprite.png")))
green.setStats(25, 180)


REDSWORD =red
BLUESWORD = blue
GREENSOWRD = green