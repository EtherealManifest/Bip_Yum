import math as PyMath

from SlimesDelight import *

data = (open('Meta.txt')).read()
META = data.split(':')
# Ive added a few sprite styles for this. if you want to check them out,
# try entering new colors. each color has a different size, though they all
# have the same power.
weaponName = 'blue_sword_sprite.png'
imgPath = Path("./Weapon Sprites/" + weaponName)
weaponDefaultImg = pygame.image.load(imgPath)
# sets how long the sword swing lasts
# this is read in from the Meta.txt file. To see the arrangement of the items in the file,
# see the comments on Game.py
SWINGTIME = int(META[2])


# These are placeholder animations


class Weapon(pygame.sprite.Sprite):
    """power, position, and swing handling for weapons used by the player"""
    # this is the position of the BOTTOM-CENTER of the weapon
    pos = (0, 0)
    # The maximum reach, for determining the hitbox
    size = 0
    # This is for determining which way the weapon swings
    direction = ''
    facingRight = False
    # used to tell whether the sword is being swung
    swing = False
    # this determines the frame for the sword swing
    # it is equal to the time in frames since the beginning of the sword swing
    # animation, going from the maximum time to zero
    swingTick = 0
    # the current angle of the weapon in radians, used to determine the angle.
    angle = 0
    # the boost to attack that this weapon gives to it's wielder
    power = 0
    # the total arc of this weapons swing
    arc = 0

    def __init__(self):
        """initializes the weapon, sets to defaults"""
        # this initializes it as a Sprite
        pygame.sprite.Sprite.__init__(self)
        # these are Sprite Attributes
        self.pos = (0, 0)
        self.image = weaponDefaultImg
        self.defaultImage = weaponDefaultImg
        # effectively, the Hitbox
        self.rect = self.image.get_rect()
        self.direction = ''
        swing = False
        swingTick = 0
        facingRight = False
        self.power = 0
        self.arc = 0

    def setStats(self, _power, _arc):
        """sets the arc and the power for this weapon"""
        self.arc = _arc
        self.power = _power

    def setImage(self, newImg):
        """changes the image and the rect for this weapon"""
        self.image = newImg
        self.rect = self.image.get_rect()
        self.defaultImage = newImg

    def position(self, player):
        """Based on player direction, sets position and facingRight for this weapon.

        Used with algorithm based generation to position the sword correctly"""
        if player.direction == 'up':
            self.pos = (player.slimex + self.rect.width, player.slimey)
            self.facingRight = False
        elif player.direction == 'down':
            self.pos = (player.slimex + self.rect.width, player.slimey)
            self.facingRight = False
        if (player.direction == 'down-left'
                or player.direction == 'left'
                or player.direction == 'up-left'):
            self.pos = (player.slimex - 8, player.slimey - 16)
            self.facingRight = False
        elif (player.direction == 'down-right'
              or player.direction == 'right'
              or player.direction == 'up-right'):
            self.pos = (player.slimex + 32, player.slimey - 16)
            self.facingRight = True
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.direction = player.direction

    '''Alright, big explain here. this is an attempt at creating a method that will
    Uniformly generate the position and angle of the weapon based on its current
    angle and how far through it's swing animation it is. it directly modifies the 
    passed weapons positon information, changing the angle and the pos attributes.
    Pass it the player that is using the weapon, the global variable SWINGTIME, 
    the amount of time elapsed (SWINGTIME - swingtime), the total angle that this
    sword swing will occupy(in degrees), and the starting angle(also in degrees)
    '''
    def getWeaponImg(self):
        return self.image
    def weaponPosition(self, player, SWINGTIME, elapsed, swingAngle, startAngle):
        """
        Correctly and mathematically positons the sword through the duration of it's swing.

        The swing angle is the total arc that the sword will traverse
        The startAngle is used to correctly position the Sword at the beginning of the swing
        Elapsed is how long the sword has been swimnging, so that is is smoothly angled through it's swing
        """
        adjustX = (player.rect.width + self.rect.height / 3)
        adjustY = (player.rect.height + self.rect.height / 3)
        swingAngle = PyMath.radians(swingAngle)
        # the starting angle is the degrees counterclockwise from the horizontal the swing should start at
        startAngle = PyMath.radians(startAngle)
        if elapsed == 0:
            self.angle = startAngle + swingAngle
        else:
            self.angle = startAngle + ((elapsed / SWINGTIME) * swingAngle)
        self.pos = (
            player.rect.x + (adjustX * (PyMath.cos(self.angle)) - self.rect.width / 2),
            player.rect.y + (adjustY * (PyMath.sin(self.angle))) - self.rect.width / 2)
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]
        self.angle = PyMath.degrees(self.angle)
        # rotate the image accordingly
        self.image = pygame.transform.rotate(self.image, -self.angle - 90)
        # update (called once per frame)

    def update(self, player):
        """Positions the sword and listens for swing actions.

        Calls weaponPosition to correctly position, and redraws the sword in the correct spot based
        on it's attributes. rotates the sword sprite appropriately, and resets the rectangle and facing
        direction if appropriate."""
        # it is positioned at the top of the slime, then moved back to
        # center the blade.
        # this will all be implemented in position()
        self.position(player)
        self.image = self.defaultImage
        # the documentataion said to call get() before get_pressed()
        pygame.event.get()
        # if the mouse is clicked, swing the sword
        if not self.swing:
            if pygame.mouse.get_pressed()[0]:
                self.swing = True
                self.swingTick = SWINGTIME
                self.angle = 0
        # if sword is swinging, determine the direction, and then pass the corresponding parameters to
        # weaponPosition()
        if self.swing:
            if self.direction == 'up':
                if self.swingTick > 0:
                    self.weaponPosition(player, SWINGTIME, self.swingTick, self.arc, -180)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False
            elif self.direction == 'down':
                if self.swingTick > 0:
                    self.weaponPosition(player, SWINGTIME, self.swingTick, self.arc, 0)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False

            # if slime is facing left, the swing angle needs to be negative
            elif (self.direction == 'left' or self.direction == 'down-left'
                  or self.direction == 'up-left'):
                if self.swingTick > 0:
                    self.weaponPosition(player, SWINGTIME, self.swingTick, self.arc, 90)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False

            # if the player is facing right, then Acoomodate and adjust accordingly
            else:
                if self.swingTick > 0:
                    self.weaponPosition(player, SWINGTIME, self.swingTick, -self.arc, 90)
                    self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                else:
                    self.swing = False
            # decrement the swing counter
            self.swingTick = self.swingTick - 1
            # logging.info("Weapon rect Coordinates (" + str(self.rect.x) + ", " + str(self.rect.y) + ")")
