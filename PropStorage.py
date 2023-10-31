#Define the setpieces to be used here
import SetPeice, os,pygame, Crypt
from pathlib import Path


sceneShop = []
setPieceList = os.listdir('./setPiecePanels')



#get all the default sprites(only ones currently generated)
#for each sprite in the listed directory
#get all the default sprites(only ones currently generated
for sprite in setPieceList:
    temp = Path('./setPiecePanels/' + sprite)
    sceneShop.append(pygame.image.load(temp))
class DefaultSetPiece(SetPeice.setPiece):
    def __init__(self):
        super().__init__()
        self.image = sceneShop[0]
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (99,123))
        self.isPassable = True
        #self.dealsDamage = True      PASSED
        #self.damage = 10             PASSED
        #self.killZone = True         PASSED
        self.spawnEnemies = True
        self.enemy = Crypt.WOLF()
        self.spawnRate = 300
        self.resetEnemy = self.wolfResetEnemy

    def wolfResetEnemy(self):
        print("enemy reset!")
        self.enemy = Crypt.WOLF()

DEFAULTSETPIECE = DefaultSetPiece()


