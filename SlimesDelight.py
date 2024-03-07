import sys
from pygame.locals import *
from StatusBlock import *
from pathlib import Path

META = (open('Meta.txt')).read().split(':')

WINX = int(META[0])
WINY = int(META[1])

pygame.init()
moveDirection = ''

# these three are constants to make testing easier. they set the rate of slowing, time of movement, and rate of movement.
SLOWR = 1
MOVET = 100  # determines how long to smooth the movement
MOVER = 2  # This is used to determine slimes speed across the screen, it is the number of pixels moved per movement
# of input.
FPS = 60  # Should match FPS in Main
ANIMR = 300  # determines the animation rate, in frames. used in SmoothGrooves
# I have finally organized my files, and there is some wild pathing involved with
# Loading the right sprite to the right place.
SlimeImgPath = Path('./SlimyIdleFrames/')

slimeImg1 = pygame.image.load(Path(SlimeImgPath / 'Slime0.png'))
slimeImg2 = pygame.image.load(Path(SlimeImgPath / 'Slime1.png'))
frontSlime1 = pygame.image.load(Path(SlimeImgPath / 'front_slime_sprite_0.png'))
frontSlime2 = pygame.image.load(Path(SlimeImgPath / 'front_slime_sprite_1.png'))
backSlime1 = pygame.image.load(Path(SlimeImgPath / 'back_slime_sprite_0.png'))
backSlime2 = pygame.image.load(Path(SlimeImgPath / 'back_slime_sprite_1.png'))
doomSlime = pygame.image.load(Path(SlimeImgPath / 'doom_slime_sprite_0.png'))
victorySlime = pygame.image.load(Path(SlimeImgPath / 'victory_slime_sprite.png'))
# This is an old placeholder
slimeImg = pygame.image.load(Path(SlimeImgPath / 'SlimeOld.png'))
jumpTick = 10  # sets the time for a jump.
jumpHeight = 10  # the height of the jump [duh]
jump = False  # flag for hopping
jumpTime = 0  # this is used to track how long hes been in the air for
slimeImgLeft = slimeImg1
# this flips the sprite around, making it face to the right. the booleans indicate
# whether the sprite will be flipped about that axis
slimeImgRight = pygame.transform.flip(slimeImg1, True, False)


# This is a controller for the animations
def SmoothGrooves(self):
    """This controls the animation for the slime, switching the sprite back and forth every so often."""
    # These are references to the files used, they are declared
    # at the top of this file
    # slimeImg1= pygame.image.load('Slime0.png')
    # slimeImg2= pygame.image.load('Slime1.png')
    global slimeImg1
    global slimeImg2
    global slimeImgLeft
    global slimeImgRight

    if self.direction == 'up':
        self.image = backSlime1
        if (pygame.time.get_ticks() % ANIMR) > ANIMR / 2:
            self.image = backSlime2
    elif self.direction == 'down':
        self.image = frontSlime1
        if (pygame.time.get_ticks() % ANIMR) > ANIMR / 2:
            self.image = frontSlime2
    else:
        self.image = slimeImg1
        if (pygame.time.get_ticks() % ANIMR) > ANIMR / 2:
            self.image = slimeImg2

    # These lines redefine the sprite, based on the result from above.
    slimeImgLeft = self.image

    # this flips the sprite around, making it face to the right. the booleans indicate
    # whether the sprite will be flipped about that axis
    slimeImgRight = pygame.transform.flip(self.image, True, False)


# smooth moves is an attempt to smooth the on-screen movement. the implementation is that it will add less and less
# movement per frame after the movement button is released. This method is only called from the main game loop if no
# buttons are being pressed on the keyboard, and moveTime > 0. To create a slowing effect, the game will add movement
# to slime equal to the moveTime / moveRate, while moveRate approaches 0
def smoothMoves(slime):
    """unworking method that smoothes the slime's deceleraton. Not a priority."""
    # moveDirection = ''
    # moveRate = 0
    # moveTime = 30  This is used to determine how long after input stops that the slowing happens
    # slowRate = 0 #this is the number of pixels the little guy is to be moved on this frame of movement
    slime.moveTime = slime.moveTime - 1
    # calculate how much to move
    slowRate = int(slime.moveTime / slime.moveRate)
    if slime.direction == 'right':
        slime.slimex += int(slowRate)
        slime.slimey += 0
    elif slime.direction == 'down':
        slime.slimex += 0
        slime.slimey += int(slowRate)
    elif slime.direction == 'left':
        slime.slimex -= int(slowRate)
        slime.slimey += 0
    elif slime.direction == 'up':
        slime.slimex += 0
        slime.slimey -= int(slowRate)
    elif slime.direction == 'up-right':
        slime.slimex += int(slowRate)
        slime.slimey -= int(slowRate)
    elif slime.direction == 'down-right':
        slime.slimex += int(slowRate)
        slime.slimey += int(slowRate)
    elif slime.direction == 'up-left':
        slime.slimex -= int(slowRate)
        slime.slimey -= int(slowRate)
    elif slime.direction == 'down-left':
        slime.slimex -= int(slowRate)
        slime.slimey += int(slowRate)
    slime.setPosition(slime.slimex, slime.slimey)


# Im turning slime into a sprite class, to make him easier to handle
class Slime(pygame.sprite.Sprite):
    """My Magnum Opus! He is controllable, adorable, and my pride and joy!

    His name is Bip-Yum. Its a relatively meaningless name, but its important to me!"""
    statBlock = StatBlock()
    slimex = 10  # x position
    slimey = 10  # y position
    slowRate = 0
    moveRate = 0
    moveTime = 0
    direction = ''
    position = (slimex, slimey)
    jumpTick = 10  # sets the time for a jump.
    jumpHeight = 10  # the height of the jump [duh]
    jump = False  # flag for hopping
    jumpTime = 0  # this is used to track how long hes been in the air for
    # this is used to determine if the weapon is being swung.
    swing = False
    isHit = False
    # after he takes damage or while dodging, stop him from taking damage
    immune = False
    immuneTime = 25
    immuneTick = 0
    # knockback is going to be determined based on the enemies strength stat, so it will be proportional to damage dealt
    knockback = 0
    knockDirection = ''
    allowedMoves = {'up': True, 'down': True, 'left': True, 'right': True}
    # The time between dodges
    dodgeCooldown = 100
    # Can He Dodge?
    dodge = True

    def __init__(self):
        """Initializes the player-character and stats"""
        # this initializes it as a sprite object by calling the Parent COnstructor
        pygame.sprite.Sprite.__init__(self)
        self.statBlock = StatBlock()
        # Im going to go ahead and give Bip some Dummy Stats
        self.statBlock.setStats(200, 10, 10, 10, 10, 10, 10)
        # logging.info("PLAYER INITIALIZED: " + self.statBlock.showStats())
        # sets the slime sprite to this object
        self.image = slimeImg1
        self.deathImage = doomSlime
        # defines the rectangle that bounds the sprite
        self.rect = self.image.get_rect()
        # this line uses setPosition to set slimes position(across the board) to the
        # center of the screen
        self.slimex = 0
        self.slimey = 0
        # allowed moves is a dictionary. this is the moves slime is currently allowed to make
        self.allowedMoves = {'up': True, 'down': True, 'left': True, 'right': True}

        # defines his current position, a set of coordinates
        self.direction = ''
        self.slowRate = SLOWR
        self.moveTime = MOVET
        self.moveRate = MOVER
        self.jumpTick = 10  # sets the time for a jump.
        self.jumpHeight = 10  # the height of the jump [duh]
        self.jump = False  # flag for hopping
        self.jumpTime = 0  # this is used to track how long hes been in the air for
        self.swing = False
        self.isHit = False
        self.knockback = 0
        self.knockDirection = ''
        self.deathTime = 60
        self.deathFrame = self.deathTime
        self.victoryImage = victorySlime
        self.immune = False

    def update(self, win=False):
        """Update the player: including movement and win/loss animations.

        Also controls positioning and player control. """
        #Win Animation
        if win:
            if self.deathFrame >= 0:
                self.deathFrame -= 1
                self.image = self.victoryImage
                self.rect = self.image.get_rect()
                return
            # Victory is imminent!
            return

        #Death Animation
        if self.statBlock.HEALTH <= 0:
            if self.deathFrame > 0:
                self.image = self.deathImage
                self.rect = self.image.get_rect()
                self.deathFrame -= 1
                return
            # slimy is uh...done dying (deathframe is 0 or less)
            return

        # self.setPosition(self.slimex, self.slimey)
        # this is for the animation, it sets the sprite for the animation frame.
        SmoothGrooves(self)

        #handle the Immunity Timer
        if self.immune == True:
            if self.immuneTick > 0:
                self.immuneTick -= 1
            if self.immuneTick == 0:
                self.immune = False


        #if slime is hit, move him back.
        if self.isHit:
            self.knockback -= 1
            if self.knockback == 0:
                self.isHit = False
            elif self.knockDirection == 'up':
                self.slimey -= self.knockback
            elif self.knockDirection == 'up-right':
                self.slimey -= self.knockback
                self.slimex += self.knockback
            elif self.knockDirection == 'right':
                self.slimex += self.knockback
            elif self.knockDirection == 'down-right':
                self.slimey += self.knockback
                self.slimex += self.knockback
            elif self.knockDirection == 'down':
                self.slimey += self.knockback
            elif self.knockDirection == 'down-left':
                self.slimey += self.knockback
                self.slimex -= self.knockback
            elif self.knockDirection == 'left':
                self.slimex -= self.knockback
            if self.knockDirection == 'up-left':
                self.slimey -= self.knockback
                self.slimex -= self.knockback

        # These make sure little slime man doesnt go outside the window
        # to do this, see if he is even a little clipped outside the window.
        # if he is, set him back in the correct direction to exactly the border of the screen.
        if self.slimex >= WINX - 32:
            self.allowedMoves['right'] = False
            self.slimex = WINX - 32
        if self.slimey >= WINY - 24:
            self.allowedMoves['down'] = False
            self.slimey = WINY - 24
        if self.slimey <= 0:
            self.allowedMoves['up'] = False
            self.slimey = 0
        if self.slimex <= 0:
            self.allowedMoves['left'] = False
            self.slimex = 0

        # this is jump stuff. he's only in the air for a little bit, but set jump to false once he's back down.
        if self.jump:
            # The last frame before landing
            if self.jumpTime == 1:
                self.slimey = self.slimey + self.jumpHeight
                self.jump = False
            # Decrement jumpTime every frame
            self.jumpTime = self.jumpTime - 1
            # If slime has landed, jump is no longer true

        # these next few checks update slime's position based on what the player has input, by moveRate (Set above)
        # at a time. It also sets the corresponding direction. Im also adding a check at the front to see if
        # smoothMovement should be triggered
        if self.moveTime > 0 and not (pygame.key.get_focused()):
            smoothMoves(self)

            # if slime isn't hit, hes free to  move in any direction, assuming its allowed
        if not self.isHit:
            if ((pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_w])
                    or (pygame.key.get_pressed()[K_LEFT] and pygame.key.get_pressed()[K_UP])):  # A W or <- and ^
                if self.allowedMoves['up']:
                    self.slimey -= 2 * (self.moveRate) / 3
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimey -= 2 * self.moveRate
                if self.allowedMoves['left']:
                    self.slimex -= 2 * self.moveRate / 3
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimex -= 2 * self.moveRate
                self.moveTime = MOVET
                # flip the sprite to face left
                self.image = slimeImgLeft
                self.direction = 'up-left'

            elif ((pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_s])
                  or (pygame.key.get_pressed()[K_LEFT] and pygame.key.get_pressed()[K_DOWN])):  # A S <- and \/
                if self.allowedMoves['down']:
                    self.slimey += 2 * self.moveRate / 3
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimey += 2 * self.moveRate
                if self.allowedMoves['left']:
                    self.slimex -= 2 * self.moveRate / 3
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimex -= 2 * self.moveRate
                self.moveTime = MOVET
                # flip the sprite to face left
                self.image = slimeImgLeft
                self.direction = 'down-left'

            elif ((pygame.key.get_pressed()[K_d] and pygame.key.get_pressed()[K_w])
                  or (pygame.key.get_pressed()[K_RIGHT] and pygame.key.get_pressed()[K_UP])):  # D W
                if self.allowedMoves['up']:
                    self.slimey -= 2 * self.moveRate / 3
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimey -= 2 * self.moveRate
                if self.allowedMoves['right']:
                    self.slimex += 2 * self.moveRate / 3
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimex += 2 * self.moveRate
                self.moveTime = MOVET
                # flip the sprite to face right
                self.image = slimeImgRight
                self.direction = 'up-right'

            elif ((pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_d])
                  or (pygame.key.get_pressed()[K_DOWN] and pygame.key.get_pressed()[K_RIGHT])):  # D S
                if self.allowedMoves['down']:
                    self.slimey += 2 * self.moveRate / 3
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimey += 2 * self.moveRate
                if self.allowedMoves['right']:
                    self.slimex += 2 * self.moveRate / 3
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimex += 2 * self.moveRate
                self.moveTime = MOVET
                # flip the sprite to face right
                self.image = slimeImgRight
                self.direction = 'down-right'

            elif pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
                if self.allowedMoves['up']:
                    self.slimey -= self.moveRate
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimey -= 2 * self.moveRate
                self.moveTime = MOVET
                self.direction = 'up'

            elif pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
                if self.allowedMoves['down']:
                    self.slimey += self.moveRate
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimey += 2 * self.moveRate
                self.moveTime = MOVET
                self.direction = 'down'

            elif pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
                if self.allowedMoves['left']:
                    self.slimex -= self.moveRate
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimex -= 2 * self.moveRate
                self.moveTime = MOVET
                # flip the sprite to face left
                self.image = slimeImgLeft
                self.direction = 'left'

            elif pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
                if self.allowedMoves['right']:
                    self.slimex += self.moveRate
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.slimex += 2 * self.moveRate
                self.moveTime = MOVET
                # flip the sprite to face right
                self.image = slimeImgRight
                self.direction = 'right'

        # If space is pressed, move him up by 10, then back down after jumptick frames.
        '''
        if pygame.key.get_pressed()[K_SPACE]:
            if self.jump == False:
                self.slimey -= self.jumpHeight
                self.jump = True
                self.jumpTime = self.jumpTick
        '''


            # FIX ME: If q is pressed, or maybe E, pull up the menu instead, inside which is an option to quit.

        # This section controls which way the sprite faces
        if self.direction == 'left' or self.direction == 'up-left' or self.direction == 'down-left':
            self.image = slimeImgLeft
        elif self.direction == 'right' or self.direction == 'up-right' or self.direction == 'down-right':
            self.image = slimeImgRight

        #this handles the immunity flashing
        if self.immune:
            self.image = pygame.transform.grayscale(self.image)

        # This is designed to make sure that when one facet of position is updated, all facets of the
        # position are updated, ensuring that Bip is where he appears to be
        self.setPosition(self.slimex, self.slimey)

    def allowAllDirections(self):
        """Allow slime to move in any direction"""
        self.allowedMoves['right'] = True
        self.allowedMoves['left'] = True
        self.allowedMoves['up'] = True
        self.allowedMoves['down'] = True

    def preventAllDirections(self):
        """prevent slime from moving in any directions"""
        self.allowedMoves['right'] = False
        self.allowedMoves['left'] = False
        self.allowedMoves['up'] = False
        self.allowedMoves['down'] = False

    def setPosition(self, x, y):
        """Change the slimes position to a set location"""
        self.slimex = x
        self.slimey = y
        self.position = (self.slimex, self.slimey)
        self.statBlock.pos = self.position
        self.rect.x, self.rect.y = self.statBlock.pos[0], self.statBlock.pos[1]

    def getPosition(self):
        """return a tuple reflecting the slimes position"""
        return self.position

    def takeDamage(self, foe):
        """deal damage to slime, based on a foes stats."""
        #if slime is immune, recieve knockback, but no damage.
        self.knockback = foe.statBlock.ATTACK % 12
        if not self.immune:
            self.statBlock.HEALTH -= foe.statBlock.ATTACK
            self.immune = True
            self.immuneTick = self.immuneTime
        if self.statBlock.HEALTH < 0:
            self.statBlock.HEALTH = 0
        self.isHit = True
        self.knockDirection = foe.direction

    def setPieceDamage(self, damage):
        """deal damage to a setpiece equal to damage"""
        self.knockback = damage%8
        if not self.immune:
            self.statBlock.HEALTH -= damage
            self.immune = True
            self.immuneTick = self.immuneTime
        if self.statBlock.HEALTH < 0:
            self.statBlock.HEALTH = 0
        self.isHit = True
        self.knockDirection = self.reverseDirection()

    def reverseDirection(self):
        """reverse the direction that the player is facing"""
        if self.direction == 'left':
            return 'right'
        if self.direction == 'down-left':
            return 'up-right'
        if self.direction == 'down':
            return 'up'
        if self.direction == 'down-right':
            return 'up-left'
        if self.direction == 'right':
            return 'left'
        if self.direction == 'up-right':
            return 'down-left'
        if self.direction == 'up':
            return 'down'
        if self.direction == 'up-left':
            return 'down-right'

    def rectangle(self):
        """return a string representation of this sprites rectangle"""
        return ("Slime:\ntop: " + str(self.rect.top) +
                "\nbottom:" + str(self.rect.bottom) +
                "\nleft: " + str(self.rect.left) +
                "\nright: " + str(self.rect.right) +
                "\nx: " + str(self.rect.x) +
                "\ny: " + str(self.rect.y))

    def printAllowedMoves(self):
        """return a string representation of the allowed moves for the slime"""
        return ("Right: " + str(self.allowedMoves['right']) +
                ", Left: " + str(self.allowedMoves['left']) +
                ", Up: " + str(self.allowedMoves['up']) +
                ", Down: " + str(self.allowedMoves['down']))

    def reset(self, pos):
        """reset the position of the slime"""
        self.setPosition(pos[0], pos[1])
        self.statBlock.HEALTH = self.statBlock.TOTALHEALTH


# This method will initialize the slime at the beginning of the program. It will
# have position, color, and animation style.
def initialize(pos_x=0, pos_y=0):
    """initialize the slime"""
    slime = Slime()
    slime.slimex = pos_x
    slime.slimey = pos_y
