from pathlib import Path

import os
import pygame
import random

pygame.init()

# this is the path to the panel folder, the loop below it loads all of them in to the
# grasspanels list, which is used to build the background
TheLand = pygame.sprite.Group()
"""This holds the rendered sprite group as the background"""
plantTiles = []
ThePlants = pygame.sprite.Group()
# These are grass tiles. they are all 100 px x 100 px

# loads the plant panels in, just like the grass panels
# FOR THE SCENARIO UPDATE::
# READ IN FROM THE SCENARIO WHICH DIRECTORY TO PULL FROM
panelList = os.listdir('./PlantPanels/')
for panel in panelList:
    temp = Path('./PlantPanels/' + panel)
    plantTiles.append(pygame.image.load(temp))


# FOR THE SCENARIO UPDATE:
# READ IN THE LIST OF CREATED SET PIECES AND ADD THEM TO
# ANOTHER GROUP. THIS GROUP WILL BE RETURNED TO THE MAIN GAME LOOP
# THE REASON FOR THIS IS THAT THE MAIN GAME LOOP NEEDS TO BE ABLE
# TO SEE THE PROPERTIES OF EVERY SETPIECE.
# THE SETPEICES WILL BE BLIT ONTO THE MAP NORMALLY

class Land(pygame.sprite.Sprite):
    """Holds an individual Sprite background tile"""
    position = (0, 0)

    def __init__(self, img):
        """Initializes this tile, giving all sprite attributes"""
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.position = (0, 0)


class Plant(pygame.sprite.Sprite):
    """THis is a plant tile, used to render the grass on the title screen"""
    position = (0, 0)

    def __init__(self, img):
        """Initializes this plant tile"""
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.position = (0, 0)

    def update(self, DispSurf):
        """Allows the plants to be updated, potentially allowing for movement."""
        ThePlants.draw(DispSurf)


def BuildTheLand(width, height, locale=Path('./GroundPanels/Grass')):
    """Given the name of a collection of tiles, builds the background.

    The background is sized according to the global screen dimensions, and is sized to
    slightly overfill it. """
    # this loop adds random tiles to the land group. it then "stitches" them all together
    # And returns them as a group.
    # search the given folder, and get the list of land tiles
    # search the given folder, and get the list of land tiles
    TheLand.empty()
    landTiles = []
    panelList = os.listdir(locale)
    for panel in panelList:
        temp = Path(str(locale) + '\\' + panel)
        landTiles.append(pygame.image.load(temp))

    for i in range(0, width + 1, 100):
        for j in range(0, height + 1, 100):
            selec = random.choice(landTiles)
            selec = Land(selec)
            selec.rect.x = j
            selec.rect.y = i
            TheLand.add(selec)
    return TheLand


# this method is used by TitleScreen to create the grass that makes up the bottom of the screen
# It also stoes three frames of animation for them.
def PlantTheGrass(width, height):
    """Randomly generates a line of plant tiles as long as the global screen width and returns the group."""
    for i in range(0, width + 1, 64):
        selec = random.choice(plantTiles)
        selec = Plant(selec)
        selec.rect.x = i
        selec.rect.y = height - 64
        ThePlants.add(selec)
    return ThePlants
