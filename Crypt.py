#Define the monsters Here
import MonsterMash, Cluster
import pygame
from pathlib import Path
import os


Mausoleum = {}
BeastList = os.listdir('./EnemySprites')

#get all the default sprites(only ones currently generated)
#for each sprite in the listed directory
#get all the default sprites(only ones currently generated
for sprite in BeastList:
    temp = Path('./EnemySprites/' + sprite)
    #scene shop has every entry as a sprite surface and a name as a series of list entries
    Mausoleum[sprite] = pygame.image.load(temp)
def imgPath(image):
    return Path("./EnemySprites/" + image)

class WOLF(MonsterMash.Monster):
    def __init__(self):
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

class TUMBLEWEED(MonsterMash.Monster):
    def __init__(self):
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
    def __init__(self):
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


CRYPT = [WOLF, TUMBLEWEED, AGGRABBAGE]
