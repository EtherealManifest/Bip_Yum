#Define the monsters Here
import MonsterMash, Cluster
import pygame
from pathlib import Path

monsterName = 'wolf_1.png'
imgPath = Path("./EnemySprites/" + monsterName)
wolf1 = pygame.image.load(imgPath)

WOLF = MonsterMash.Monster()
WOLF.setAll("Wolf", "A small Canine. Ferocious, but not usually a threat unless attacking in Packs.",
            150, 5, 5, 0, 5, 2, 20)
WOLF.setImage(wolf1)
WOLF.setRect()
WOLF.setCore(Cluster.SIMPLE)



CRYPT = [WOLF,]
