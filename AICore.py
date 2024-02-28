class AICore:
    """Used to Control Monster Movement and Actions.

    ...

    Attributes
    ----------

    monster : the monster that this core acts on
    movement : the method that is executed on update()
    """
    # the monster that this Core acts on
    # this will have to be a deep copy of the monster, it has to directly modify its stats.
    monster = None
    # movement is by far the most complicated assignment in this program to date.
    # it is the assignment of a function to a variable. In the file where the Monsters will be created,
    # there will be prebuilt functions that define the different Movement AIs for the enemies to use.
    # this variable Movement will hold those functions. When update is called, Movement should modify the
    # monsters position and return it's new statblock.
    movement = None

    def __init__(self):
        """Initializes. Sets monster to none and movement to DefaultMovement"""
        self.monster = None
        self.movement = defaultMovement

    def setMovement(self, func):
        """Sets the current movement attribute.

        ...

        Parameters:
        -----------

        func: method"""
        self.movement = func

    def update(self, slime):
        """Calls the bound movement method"""
        # call the local movement function, using the local monster.
        self.movement(self.monster, slime)


# THis is the Default Movement method for the Core.
def defaultMovement(monster, slime):
    """Always move towards the player"""
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
