import Armory
from pathlib import Path
import pygame

red = Armory.Weapon()
red.setImage(pygame.image.load(Path("./Weapon Sprites/red_sword_sprite.png")))
red.setStats(15, 180)

blue = Armory.Weapon()
blue.setImage(pygame.image.load(Path("./Weapon Sprites/blue_sword_sprite.png")))
blue.setStats(10, 180)

green = Armory.Weapon()
green.setImage(pygame.image.load(Path("./Weapon Sprites/green_sword_sprite.png")))
green.setStats(25, 180)

REDSWORD = red
"""A slightly larger sword. 

Power:15, Arc: 180"""
BLUESWORD = blue
"""A short sword

Power: 10, Arc: 180"""
GREENSWORD = green
"""A long sword.

Power: 25, Arc: 180"""
