import AICore
import random

def agressiveMovement(monster, slime):
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

def passiveMovement(monster, slime):
    #this is a vector that corresponds with directions.
    #it is defined as follows:
    #[U, UR, R, DR, D, DL, L, UL]
    #load the vector to determine his movements
    movementVector = [0,0,0,0,0,0,0,0]
    #change a random direction to 1
    movementVector[random.randint(0,7)] = 1
    if movementVector[7] == 1:
        monster.monsterY -= monster.MonsterMoveSpeed
        monster.monsterX -= monster.MonsterMoveSpeed
        monster.hitMove = (monster.hitMoveRate, monster.hitMoveRate)
        monster.direction = 'up-left'
    elif movementVector[6] == 1:
        monster.monsterX -= monster.MonsterMoveSpeed
        monster.hitMove = (monster.hitMoveRate, 0)
        monster.direction = 'left'
    elif movementVector[5] == 1:
        monster.monsterY += monster.MonsterMoveSpeed
        monster.monsterX -= monster.MonsterMoveSpeed
        monster.direction = 'down-left'
        monster.hitMove = (monster.hitMoveRate, -monster.hitMoveRate)
    elif movementVector[4] == 1:
        monster.monsterY += monster.MonsterMoveSpeed
        monster.direction = 'down'
        monster.hitMove = (0, -monster.hitMoveRate)
    elif movementVector[3] == 1:
        monster.monsterY += monster.MonsterMoveSpeed
        monster.monsterX += monster.MonsterMoveSpeed
        monster.direction = 'down-right'
        monster.hitMove = (-monster.hitMoveRate, -monster.hitMoveRate)
    elif movementVector[2] == 1:
        monster.monsterX += monster.MonsterMoveSpeed
        monster.direction = 'right'
        monster.hitMove = (-monster.hitMoveRate, 0)
    elif movementVector[1] == 1:
        monster.monsterY -= monster.MonsterMoveSpeed
        monster.monsterX += monster.MonsterMoveSpeed
        monster.direction = 'up-right'
        monster.hitMove = (-monster.hitMoveRate, monster.hitMoveRate)
    elif movementVector[0] == 1:
        monster.monsterY -= monster.MonsterMoveSpeed
        monster.direction = 'up'
        monster.hitMove = (0, monster.hitMoveRate)

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

SIMPLE = AICore.AICore()
AGRESSIVE = AICore.AICore()
PASSIVE = AICore.AICore()
STAY = AICore.AICore()

SIMPLE.movement = simpleMovement
PASSIVE.movement = passiveMovement
AGRESSIVE.movement = agressiveMovement
STAY.movement = Stay
