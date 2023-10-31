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
        self.destroyedImage = sceneShop[3]
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (99,123))
        self.isPassable = False
        #self.dealsDamage = True
        #self.damage = 10
        #self.killZone = True
        self.spawnEnemies = True
        self.enemy = Crypt.WOLF()
        self.spawnRate = 300
        self.resetEnemy = self.wolfResetEnemy
        self.destroyable = True
        self.setPieceHP = 300
        self.destroyTrigger = self.destroyDefaultSetpiece

    def wolfResetEnemy(self):
        print("enemy reset!")
        self.enemy = Crypt.WOLF()
    def destroyDefaultSetpiece(self):
        self.toggleSpawnEnemies()
        self.toggleIsPassable()



DEFAULTSETPIECE = DefaultSetPiece()


