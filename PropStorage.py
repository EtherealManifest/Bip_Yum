#Define the setpieces to be used here
import SetPeice, os,pygame, Crypt, random
from pathlib import Path

data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])
sceneShop = {}
setPieceList = os.listdir('./setPiecePanels')



#get all the default sprites(only ones currently generated)
#for each sprite in the listed directory
#get all the default sprites(only ones currently generated
for sprite in setPieceList:
    temp = Path('./setPiecePanels/' + sprite)
    #scene shop has every entry as a sprite surface and a name as a series of list entries
    sceneShop[sprite] = pygame.image.load(temp)

class DefaultSetPiece(SetPeice.setPiece):
    def __init__(self):
        super().__init__()
        self.image = sceneShop.get("Destroyable_0.png", None)
        self.destroyedImage = sceneShop.get("Destroyable_1.png", None)
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (99,123))
        self.isPassable = False
        self.dealsDamage = True
        self.damage = 10
        self.killZone = True
        self.spawnEnemies = True
        self.enemy = Crypt.WOLF()
        self.spawnRate = 300
        self.spawnTime = 0
        self.resetEnemy = self.wolfResetEnemy
        self.destroyable = True
        self.setPieceHP = 300
        self.destroyTrigger = self.destroyDefaultSetpiece
    def reset(self):
        self.__init__()
    def wolfResetEnemy(self):
        self.enemy = Crypt.WOLF()
    def destroyDefaultSetpiece(self):
        self.toggleSpawnEnemies()
        self.toggleIsPassable()

DEFAULTSETPIECE = DefaultSetPiece()

class Round_Cactus(SetPeice.setPiece):
    def __init__(self):
        super().__init__()
        self.image = sceneShop.get("Round_Cactus.png", None)
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (10, 123))
        self.isPassable = False
        self.dealsDamage = True
        self.damage = 10
        self.killZone = False
        self.spawnEnemies = False
        self.destroyable = False
        self.setPieceHP = 300

    def reset(self):
        self.__init__()

class Tall_Cactus(SetPeice.setPiece):
    def __init__(self):
        super().__init__()
        self.image = sceneShop.get("Tall_Cactus.png", None)
        self.rect = self.image.get_rect()
        self.buildSetPiece(self.image, self.rect, (100, 300))
        self.isPassable = False
        self.dealsDamage = True
        self.damage = 10
        self.killZone = False
        self.spawnEnemies = False
        self.destroyable = False
        self.setPieceHP = 300

    def reset(self):
        self.__init__()

class TumbleweedLord(SetPeice.setPiece):
    def __init__(self):
        super().__init__()
        self.image = sceneShop.get("Buzz-Buzz.png")
        self.rect = self.image.get_rect()
        self.pos = (WINX, WINY)
        self.dealsDamage = False
        self.isPassable = True
        self.spawnEnemies = True
        self.enemy = Crypt.TUMBLEWEED()
        self.spawnRate = 10
        self.spawnTime = 0
        self.resetEnemy = self.tumbleweedResetEnemy

    def tumbleweedResetEnemy(self):
        scaleFactor = (.5 + (1.5-.5) * random.random()) #this should generate a number between .5 and 1.5
        self.enemy = Crypt.TUMBLEWEED()
        self.enemy.baseImage = pygame.transform.scale_by(self.enemy.image, scaleFactor)
        self.enemy.setPosition((WINX + 1, random.randint(32, int(WINY))))
