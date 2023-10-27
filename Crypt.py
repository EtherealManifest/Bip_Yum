#Define the monsters Here
import MonsterMash, Cluster
import pygame
from pathlib import Path

wolfName = 'wolf_1.png'
wolfDamagedName = 'wolf_2.png'
wolfDeadName = 'wolf_3.png'
def imgPath(image):
    return Path("./EnemySprites/" + image)
wolf1 = pygame.image.load(imgPath(wolfName))
wolf2 = pygame.image.load(imgPath(wolfDamagedName))
wolf3 = pygame.image.load(imgPath(wolfDeadName))


class WOLF(MonsterMash.Monster):
    def __init__(self):
        super().__init__()
        self.setAll("Wolf", "A small Canine. Ferocious, but not usually a threat unless attacking in Packs.",
                    150, 5, 5, 0, 5, 2, 20)
        self.setImage(wolf1)
        self.setRect()
        self.setCore(Cluster.AgressiveMovement())
        self.setPosition((200, 200))
        self.normalImage = wolf1
        self.damageImage = wolf2
        self.deadImage = wolf3


CRYPT = [WOLF]
