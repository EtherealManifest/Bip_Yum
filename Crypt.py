# Define the monsters Here
import os
from pathlib import Path
import pygame
import Cluster
import MonsterMash

Mausoleum = {}
"""Holds the monster Image Sprites, pulls from ./EnemySprites

use Mausoleum.get(_filename_) for setting images, must know the image name and file type."""
BeastList = os.listdir('./EnemySprites')

# get all the default sprites(only ones currently generated)
# for each sprite in the listed directory
# get all the default sprites(only ones currently generated
for sprite in BeastList:
    temp = Path('./EnemySprites/' + sprite)
    # scene shop has every entry as a sprite surface and a name as a series of list entries
    Mausoleum[sprite] = pygame.image.load(temp)


def imgPath(image):
    """Used to concat the proper path to the image for efficient retrieval"""
    return Path("./EnemySprites/" + image)


class WOLF(MonsterMash.Monster):
    """A wolf enemy. Fast and relentless"""

    def __init__(self):
        """Initializes the wolf enemy and sets stats."""
        super().__init__()
        self.setAll("Wolf", "A small Canine. Ferocious, but not usually a threat unless attacking in Packs.",
                    150, 5, 5, 0, 5, 3, 20)
        self.setImage(Mausoleum.get("Wolf_1.png"))
        self.setRect()
        self.setCore(Cluster.AgressiveMovement())
        self.setPosition((200, 200))
        self.normalImage = Mausoleum.get("Wolf_1.png")
        self.damageImage = Mausoleum.get("Wolf_2.png")
        self.deadImage = Mausoleum.get("Wolf_2.png")


class Chaark(MonsterMash.Monster):
    """This is a fire monster that will jump towards the player slowly"""
    # run it on a cyle of 60 frames to jump, 60 frames to rest.


class SNOWMAN(MonsterMash.Monster):
    """A Snowman! He throws Snowballs"""

    def __init__(self):
        # FIXME: INCOMPLETE
        """Initializes the Snowman"""
        super().__init__()
        self.setAll("Snowman", "He got invited to a snowball fight, but no one else "
                               "showed up...", 100, 3, 5, 10, 1, 1, 10)
        self.setImage(Mausoleum.get("Snowman_0.png"))
        self.setRect()
        self.setCore(Cluster.SnowmanMovement())
        self.setPosition((20, 100))
        self.normalImage = Mausoleum.get("Snowman_0.png")
        self.baseImage = self.normalImage
        self.damageImage = Mausoleum.get("Snowman_1.png")
        self.deadImage = Mausoleum.get("Snowman_3.png")
        self.setKnockback(1)
        self.setHitTime(10)
        self.timer = 100
        # use this to determine how often a new move may be chosen
        self.waitClock = 100
        self.waitTick = 0
        self.moveRate = (0, 0)


class TUMBLEWEED(MonsterMash.Monster):
    """A bouncing tumbleweed, moves to the left and bounces

        To change the bounces of a tumbleweed, change it's .bounceHeight and .bounceWidth"""

    def __init__(self):
        """Initializes this tumbleweed and sets stats."""
        super().__init__()
        self.setAll("Tumbleweed", "Just a bouncing tumbleweed",
                    1, 1, 1, 0, 0, 5, 1)

        self.setImage(Mausoleum.get("Tumbleweed.png"))
        self.setRect()
        self.setCore(Cluster.TumbleweedMovement())
        self.setPosition((200, 200))
        self.bounceHeight = -20
        self.bounceWidth = 20
        self.bounceCount = 0
        self.direction = 'left'
        self.rotations = 0
        self.statBlock.HealthBar.noShow()
        self.deadImage = Mausoleum.get("Tumbleweed_1.png")
        self.baseImage = self.image
        self.stopOnHit = False


class AGGRABBAGE(MonsterMash.Monster):
    """A slow-moving cabbage-looking monster. very tough"""

    def __init__(self):
        """Initializes this monster and it's stats"""
        super().__init__()
        self.setAll("Aggrabbage", "Massive and angry. While it appears to be a cabbage, it is, in fact, made "
                                  "of stone. Very defensive. ",
                    100, 11, 12, 15, 5, 1, 20)
        self.setImage(Mausoleum.get("Aggrabbage_0.png"))
        self.setRect()
        self.setCore(Cluster.AgressiveMovement())
        self.setPosition((200, 200))
        self.normalImage = Mausoleum.get("Aggrabbage_0.png")
        self.damageImage = Mausoleum.get("Aggrabbage_1.png")
        self.deadImage = Mausoleum.get("Aggrabbage_2.png")
        self.setKnockback(.5)
        self.setHitTime(5)


class OMEN(MonsterMash.Monster):
    """A Boss enemy. Has a variety of moves and is rather hardy."""

    def __init__(self):
        """Initializes this monster and set's it's stats."""
        super().__init__()
        self.setAll("OMEN", "A Harbinger of doom, and a loyal test subject",
                    350, 23, 50, 15, 5, 1.5, 20)
        self.setImage(Mausoleum.get("Omen_0.png"))
        self.setRect()
        self.setCore(Cluster.OmenMovement())
        self.setPosition((200, 200))
        self.normalImage = Mausoleum.get("Omen_0.png")
        self.baseImage = self.normalImage
        self.damageImage = Mausoleum.get("Omen_1.png")
        self.deadImage = Mausoleum.get("Omen_2.png")
        self.setKnockback(15)
        self.setHitTime(10)
        self.timer = 100
        # use this to determine how often a new move may be chosen
        self.waitClock = 100
        self.waitTick = 0
        self.rotations = 0
        self.bounceCount = 0
        self.bounceWidth = 10
        self.bounceHeight = 30
        self.moveRate = (0, 0)


CRYPT = [WOLF, TUMBLEWEED, AGGRABBAGE, OMEN]
"""CRYPT is where all monsters are held. Add them to a scenario by using CRYPT.get[_name_]"""
