import AICore
import random
import pygame.transform

data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])
class AgressiveMovement(AICore.AICore):
    def __init__(self):
        super().__init__()
        self.movement = agressiveMovement

class ChaoticMovement(AICore.AICore):
    def __init__(self):
        super().__init__()
        self.movement = chaoticMovement


class SimpleMovement(AICore.AICore):
    def __init__(self):
        super().__init__()
        self.movement = simpleMovement

class TumbleweedMovement(AICore.AICore):
    def __init__(self):
        super().__init__()
        self.movement = tumbeweedMovement


def agressiveMovement(monster, slime):
    if monster.monsterX > slime.slimex and monster.monsterX > 0:
        monster.hitMove = (monster.hitMoveRate, 0)
        if monster.monsterY > slime.slimey and monster.monsterY > 0:
            monster.monsterY -= monster.MonsterMoveSpeed
            monster.direction = 'up-left'
            monster.hitMove = (monster.hitMoveRate, monster.hitMoveRate)
        else:
            monster.direction = 'left'
        if monster.monsterY < slime.slimey and monster.monsterY < WINY:
            monster.monsterY += monster.MonsterMoveSpeed
            monster.direction = 'down-left'
            monster.hitMove = (monster.hitMoveRate, -monster.hitMoveRate)
        else:
            monster.direction = 'left'
        monster.monsterX -= monster.MonsterMoveSpeed

    elif monster.monsterX < slime.slimex and monster.monsterX < WINX:
        monster.hitMove = (-monster.hitMoveRate, 0)
        if monster.monsterY > slime.slimey and monster.monsterY > 0:
            monster.monsterY -= monster.MonsterMoveSpeed
            monster.direction = 'up-right'
            monster.hitMove = (-monster.hitMoveRate, monster.hitMoveRate)
        else:
            monster.direction = 'right'
        if monster.monsterY < slime.slimey and monster.monsterY < WINY:
            monster.monsterY += monster.MonsterMoveSpeed
            monster.direction = 'down-right'
            monster.hitMove = (-monster.hitMoveRate, -monster.hitMoveRate)
        else:
            monster.direction = 'right'
        monster.monsterX += monster.MonsterMoveSpeed

    else:
        if monster.monsterY < slime.slimey and monster.monsterY < WINY:
            monster.monsterY += monster.MonsterMoveSpeed
            monster.hitMove = (0, -monster.hitMoveRate)
            monster.direction = 'down'
        elif monster.monsterY > 0:
            monster.monsterY -= monster.MonsterMoveSpeed
            monster.direction = 'up'
            monster.hitMove = (0, monster.hitMoveRate)
def chaoticMovement(monster, slime):
    #this is a vector that corresponds with directions.
    #it is defined as follows:
    #[U, UR, R, DR, D, DL, L, UL]
    #load the vector to determine his movement
    movementVector = [0,0,0,0,0,0,0,0]
    #change a random direction to 1
    movementVector[random.randint(0,7)] = 1
    if(random.randint(0,5)== 2):
        movementVector[random.randint(0, 7)] = 1
    if movementVector[7] and monster.monsterX > 0 and monster.monsterY > 0:
        monster.monsterY -= monster.MonsterMoveSpeed
        monster.monsterX -= monster.MonsterMoveSpeed
        monster.hitMove = (monster.hitMoveRate, monster.hitMoveRate)
        monster.direction = 'up-left'
    elif movementVector[6] and monster.monsterX > 0:
        monster.monsterX -= monster.MonsterMoveSpeed
        monster.hitMove = (monster.hitMoveRate, 0)
        monster.direction = 'left'
    elif movementVector[5]  and monster.monsterX > 0 and monster.monsterY < WINY:
        monster.monsterY += monster.MonsterMoveSpeed
        monster.monsterX -= monster.MonsterMoveSpeed
        monster.direction = 'down-left'
        monster.hitMove = (monster.hitMoveRate, -monster.hitMoveRate)
    elif movementVector[4] and monster.monsterY < WINY:
        monster.monsterY += monster.MonsterMoveSpeed
        monster.direction = 'down'
        monster.hitMove = (0, -monster.hitMoveRate)
    elif movementVector[3] and monster.monsterX < WINX and monster.monsterY < WINY:
        monster.monsterY += monster.MonsterMoveSpeed
        monster.monsterX += monster.MonsterMoveSpeed
        monster.direction = 'down-right'
        monster.hitMove = (-monster.hitMoveRate, -monster.hitMoveRate)
    elif movementVector[2] and monster.monsterX < WINX:
        monster.monsterX += monster.MonsterMoveSpeed
        monster.direction = 'right'
        monster.hitMove = (-monster.hitMoveRate, 0)
    elif movementVector[1] and monster.monsterX < WINX and monster.monsterY > 0:
        monster.monsterY -= monster.MonsterMoveSpeed
        monster.monsterX += monster.MonsterMoveSpeed
        monster.direction = 'up-right'
        monster.hitMove = (-monster.hitMoveRate, monster.hitMoveRate)
    elif movementVector[0] and monster.monsterY > 0:
        monster.monsterY -= monster.MonsterMoveSpeed
        monster.direction = 'up'
        monster.hitMove = (0, monster.hitMoveRate)

def tumbeweedMovement(monster, slime):
    #tumbleweed movement just moves the enemy from left to right, bouncing.
    monster.rotations += 1
    monster.image = monster.baseImage
    #the very last number in this is the number of degrees to rotate by per frame
    monster.image = pygame.transform.rotate(monster.image, monster.rotations * 10)
    monster.monsterX -= monster.MonsterMoveSpeed
    if monster.bounceCount == (1 + monster.bounceWidth):
        monster.bounceCount = 0
    heightJump = -(    (monster.bounceHeight * (monster.bounceCount - 10))/25   )
    monster.monsterY += heightJump
    monster.bounceCount += 1

def simpleMovement(monster, slime):
    if(random.randint(0,100) < 75):
        if monster.monsterX > slime.slimex:
            monster.hitMove = (monster.hitMoveRate, 0)
            if monster.monsterY > slime.slimey:
                monster.monsterY -= monster.MonsterMoveSpeed
                monster.direction = 'up-left'
                monster.hitMove = (monster.hitMoveRate, monster.hitMoveRate)
            else:
                monster.direction = 'left'
            if monster.monsterY < slime.slimey:
                monster.monsterY += monster.MonsterMoveSpeed
                monster.direction = 'down-left'
                monster.hitMove = (monster.hitMoveRate, -monster.hitMoveRate)
            else:
                monster.direction = 'left'
            monster.monsterX -= monster.MonsterMoveSpeed

        elif monster.monsterX < slime.slimex:
            monster.hitMove = (-monster.hitMoveRate, 0)
            if monster.monsterY > slime.slimey:
                monster.monsterY -= monster.MonsterMoveSpeed
                monster.direction = 'up-right'
                monster.hitMove = (-monster.hitMoveRate, monster.hitMoveRate)
            else:
                monster.direction = 'right'
            if monster.monsterY < slime.slimey:
                monster.monsterY += monster.MonsterMoveSpeed
                monster.direction = 'down-right'
                monster.hitMove = (-monster.hitMoveRate, -monster.hitMoveRate)
            else:
                monster.direction = 'right'
            monster.monsterX += monster.MonsterMoveSpeed

        else:
            if monster.monsterY < slime.slimey:
                monster.monsterY += monster.MonsterMoveSpeed
                monster.hitMove = (0, -monster.hitMoveRate)
                monster.direction = 'down'
            else:
                monster.monsterY -= monster.MonsterMoveSpeed
                monster.direction = 'up'
                monster.hitMove = (0, monster.hitMoveRate)

def Stay(monster, slime):
    return

def printDirection(monster):
    return (monster.Name + " : " + monster.direction + ", (" + str(monster.monsterX) + ", " + str(monster.monsterY) +
        "), Speed: " + str(monster.statBlock.SPEED))


SIMPLE = AICore.AICore()
AGRESSIVE = AICore.AICore()
CHAOTIC = AICore.AICore()
STAY = AICore.AICore()
TUMBLEWEED = AICore.AICore()

SIMPLE.movement = simpleMovement
CHAOTIC.movement = chaoticMovement
AGRESSIVE.movement = agressiveMovement
STAY.movement = Stay
TUMBLEWEED.movement = tumbeweedMovement

