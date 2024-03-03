import AICore
import random
import pygame.transform

data = (open('Meta.txt')).read()
META = data.split(':')
WINX = int(META[0])
WINY = int(META[1])




class AgressiveMovement(AICore.AICore):
    """Used to contain agressive Movement, moves at top speed towards the player"""
    def __init__(self):
        """initializes this core, sets the movement method to agressive"""
        super().__init__()
        self.movement = agressiveMovement

class ChaoticMovement(AICore.AICore):
    """Used to contain chaotic Movement, moves randomly in 8 directions"""
    def __init__(self):
        """Initializes this core, sets the movement method to chaotic"""
        super().__init__()
        self.movement = chaoticMovement

class SimpleMovement(AICore.AICore):
    """Used to contain simple movement. slowly move towards the player"""
    def __init__(self):
        """Initializes this core, sets the movement method to Simple"""
        super().__init__()
        self.movement = simpleMovement

class TumbleweedMovement(AICore.AICore):
    """Used to contain tubleweed-style movement. Bounce to the left!"""
    def __init__(self):
        """Initializes this core, sets the movement method to tumbleweed"""
        super().__init__()
        self.movement = tumbeweedMovement


#Omen, while currently being used for testing, is gonna be the first complex-level Core that i will
#desgin. he will have various moves, all of which will be chosen based on criteria.
#this will be accomplished by having multiple methods that can be set to the movement attribute
# at different times. when he uses a 'move', set a new core and his movement will change.
class OmenMovement(AICore.AICore):
    """Holds Omen's Movement. Manages the core-switches."""
    def __init__(self):
        """initializes the defaults for this core."""
        super().__init__()
        self.movement = agressiveMovement
        self.moveRate = (0,0)

    #this will handle decision making for OMEN:
    def update(self, slime):
        """Manages the moves that Omen Uses.

        Every few frames(initially 100), Randomly switches the method for movement, causing Omen to use
        a different move."""
        # using the monsters timer, randomly decide on an action.
        if self.monster.waitTick == 0:
            newMove = random.randrange(0, 12)
            # potentially choose a new move. At the end of each clock cycle, there is a 1/7 chance to choose a move.
            # after that, there is a 1/5 chance that a specific move will be chosen. .
            if newMove > 6:
                if newMove <= 8:
                    self.movement = teleport
                elif newMove <= 10:
                    self.movement = lunge
                else:
                    self.movement = Stay
            elif newMove < 3:
                #doesn't happen often, but might be funny.
                if newMove == 0:
                    self.movement = tumbeweedMovement
                if newMove == 1:
                    self.movement = chaoticMovement
                if newMove == 2:
                    self.movement = simpleMovement
            else:
                self.movement = agressiveMovement
        # occasionally check the time, and if needed, check the player to see if an update can be made
        #regardless, use the current movement core to update movement.
        self.monster.waitTick -= 1
        if self.monster.waitTick < 0:
            self.monster.waitTick = self.monster.waitClock
        self.movement(self.monster, slime)
        # These make sure little Monster man doesnt go outside the window
        # to do this, see if he is even a little clipped outside the window.
        # if he is, set him back in the correct direction to exactly the border of the screen.
        if self.monster.monsterX >= WINX - 32:
            self.monster.monsterX = WINX - 32
        if self.monster.monsterY >= WINY - 24:
            self.monster.monsterY = WINY - 24
        if self.monster.monsterY <= 0:
            self.monster.monsterY = 0
        if self.monster.monsterX <= 0:
            self.monster.monsterX = 0


# warp to a random location
# in order for a monster to use teleport, it has to have a time counter on it, so that it can
# complete the action.
def teleport(monster, slime):
    """Pauses, then moves the monster to a random location on the screen very quickly."""
    #this location is where the monster moves to, and is used later.
    #these are each the amount that the monster needs to move over the course of the teleport
    moveX = 0
    moveY = 0
    # for the first 20 Frames, do nothing, and dont move.
    if monster.waitTick > monster.waitClock - 20:
        return
    #then, on frame 21, choose a random location in the window
    if monster.waitTick == monster.waitClock - 21:
        teleportLocation = (random.randrange(0,WINX), random.randrange(0,WINY))
        #determine how far the monster needs to move per frame
        moveX = int((monster.monsterX - teleportLocation[0]) / 10)
        moveY = int((monster.monsterY - teleportLocation[1]) / 10)
        monster.moveRate = (moveX, moveY)

    # then, over the course of 10 frames, move to the random location
    if monster.waitClock - 32 < monster.waitTick < monster.waitClock - 22:
        monster.monsterY += monster.moveRate[1] / 10
        monster.monsterX += monster.moveRate[0] / 10

    #once it reappears, just stay in place until teh next timer cycle
    if monster.waitTick < monster.waitClock - 33:
        return

def lunge(monster, slime):
    """Pause, then quickly move to the player

    Does not follow the player, but reads the players position during the pause and lunges there.
    the speed will vary depending on how far away the player is"""
    moveX, moveY = 0, 0
    # use the first 5 frames to aim
    if monster.waitTick > monster.waitClock - 5:
        #determine and save the players location.
        target = slime.position
        moveX, moveY = target[0] - monster.position[0] ,  target[1] - monster.position[1]
        monster.moveRate = (moveX, moveY)

    #then for teh next 30 frames, stay in place
    elif monster.waitTick > monster.waitClock - 35:
    # for the next 55 frames, lunge at the player
        return
    elif monster.waitTick > monster.waitClock - 90:
        monster.monsterX += monster.moveRate[0] / 55
        monster.monsterY += monster.moveRate[1] / 55
    else:
        #smooth the movement
        monster.monsterX += monster.moveRate[0] - (((10 - monster.hitTick) / 10) * monster.moveRate[0])
        monster.monsterY += monster.moveRate[1] - (((10 - monster.hitTick) / 10) * monster.moveRate[1])
def agressiveMovement(monster, slime):
    """Read the player's position, then move in that direction.

    also sets the knockback direction correctly. """
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


# the monster will randomly move in one of 8 directions, at random intervals.
# The parameter slime is here because the number of parameters needs to be standardized so that all the modules
# work together.
def chaoticMovement(monster, slime):
    """move at speed in one of eight randomly chosen cardinal directions each frame.

    also sets knockback appropriatley."""
    # this is a vector that corresponds with directions.
    # it is defined as follows:
    # [U, UR, R, DR, D, DL, L, UL]
    # load the vector to determine his movement
    movementVector = [0, 0, 0, 0, 0, 0, 0, 0]
    # change a random direction to 1
    movementVector[random.randint(0, 7)] = 1
    if random.randint(0, 5) == 2:
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
    elif movementVector[5] and monster.monsterX > 0 and monster.monsterY < WINY:
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


# the monster will constantly move to the left, and bounce according to the function. height width can be universally
# set
def tumbeweedMovement(monster, slime):
    """Moves the Monster to the left while bouncing!

    modifies the monsters rotations attribute

    uses the monsters bounceHeight and bouncewidth to determine how the bounce works on screen.

    """
    # tumbleweed movement just moves the enemy from left to right, bouncing.
    monster.rotations += 1
    monster.image = monster.baseImage
    # the very last number in this is the number of degrees to rotate by per frame
    monster.image = pygame.transform.rotate(monster.image, monster.rotations * 10)
    monster.monsterX -= monster.MonsterMoveSpeed
    if monster.bounceCount == (1 + monster.bounceWidth):
        monster.bounceCount = 0
    heightJump = -((monster.bounceHeight * (monster.bounceCount - 10)) / 25)
    monster.monsterY += heightJump
    monster.bounceCount += 1


# Similar to agressive monement, always moves towards the player, but moves slower than regular speed
def simpleMovement(monster, slime):
    """Slowly moves towards the player at a constant speed

    speed is half the monsters move speed"""
    if monster.monsterX > slime.slimex:
        monster.hitMove = (monster.hitMoveRate, 0)
        if monster.monsterY > slime.slimey:
            monster.monsterY -= int(monster.MonsterMoveSpeed / 2)
            monster.direction = 'up-left'
            monster.hitMove = (monster.hitMoveRate, monster.hitMoveRate)
        else:
            monster.direction = 'left'
        if monster.monsterY < slime.slimey:
            monster.monsterY += int(monster.MonsterMoveSpeed / 2)
            monster.direction = 'down-left'
            monster.hitMove = (monster.hitMoveRate, -monster.hitMoveRate)
        else:
            monster.direction = 'left'
        monster.monsterX -= int(monster.MonsterMoveSpeed / 2)

    elif monster.monsterX < slime.slimex:
        monster.hitMove = (-monster.hitMoveRate, 0)
        if monster.monsterY > slime.slimey:
            monster.monsterY -= int(monster.MonsterMoveSpeed / 2)
            monster.direction = 'up-right'
            monster.hitMove = (-monster.hitMoveRate, monster.hitMoveRate)
        else:
            monster.direction = 'right'
        if monster.monsterY < slime.slimey:
            monster.monsterY += int(monster.MonsterMoveSpeed / 2)
            monster.direction = 'down-right'
            monster.hitMove = (-monster.hitMoveRate, -monster.hitMoveRate)
        else:
            monster.direction = 'right'
        monster.monsterX += int(monster.MonsterMoveSpeed / 2)

    else:
        if monster.monsterY < slime.slimey:
            monster.monsterY += int(monster.MonsterMoveSpeed / 2)
            monster.hitMove = (0, -monster.hitMoveRate)
            monster.direction = 'down'
        else:
            monster.monsterY -= int(monster.MonsterMoveSpeed / 2)
            monster.direction = 'up'
            monster.hitMove = (0, monster.hitMoveRate)


def Stay(monster, slime):
    """Monster Does not Move"""
    return


def printDirection(monster):
    """returns the Monster's current direction and speed as a string"""
    return (monster.Name + " : " + monster.direction + ", (" + str(monster.monsterX) + ", " + str(monster.monsterY) +
            "), Speed: " + str(monster.statBlock.SPEED))


SIMPLE = AICore.AICore()
"""The simple AI Core, move slowly towards the player"""
AGRESSIVE = AICore.AICore()
"""The agressive AI Core. Move quickly towards the player"""
CHAOTIC = AICore.AICore()
"""The Chaotic Movement Core. Move sprodically in all directions"""
STAY = AICore.AICore()
"""The Stay Movement Core. The Monster Does not Move"""
TUMBLEWEED = AICore.AICore()
"""The tumbleweed Movement core. bounces the monster to the left"""

SIMPLE.movement = simpleMovement
CHAOTIC.movement = chaoticMovement
AGRESSIVE.movement = agressiveMovement
STAY.movement = Stay
TUMBLEWEED.movement = tumbeweedMovement
