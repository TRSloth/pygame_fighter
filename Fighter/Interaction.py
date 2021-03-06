from Fighter.Vector import Vector

class Interaction:

    characters = []

    #initialises interaction class with 3 arrays (so the objects can be addressed iteratively) and a keyboard
    def __init__(self, keyboard):
        #self.characters = []
        self.platforms = []
        self.walls = []
        self.keyboard = keyboard

    #add a character to the interaction class
    def addCharacter(self, character):
        self.characters.append(character)

    #add a platform to the interaction class
    def addPlatform(self, platform):
        self.platforms.append(platform)

    #add a wall to the interaction class
    def addWall(self,wall):
        self.walls.append(wall)

    #process keyboard input and translate into character movement
    #for use of bool, see keyboard class
    #   -   used to split keyboard inputs
    def movements(self,character, other, bool):
        #movements that are only available when not blocking
        if not character.dead:
            if not self.keyboard.down[bool]:
                character.not_blocking()
                # x velocity can only be changed when not jumping (no midair direction changes)
                if self.keyboard.left[bool] and not character.jumping:
                    character.vel = Vector(-1, character.vel.getY())
                    character.setState("walk")
                if self.keyboard.right[bool] and not character.jumping:
                    character.vel = Vector(1, character.vel.getY())
                    character.setState("walk")
                # no double jumping
                if self.keyboard.up[bool] and not character.jumping:
                    character.attemptJump()
                # can attack if jumping (attack becomes jump kick
                if self.keyboard.attack[bool]:
                    character.punch(other)
                # fires a fireball if the character is on the ground
                if self.keyboard.fire[bool] and not character.jumping:
                    character.fire(other)
                if self.keyboard.idle[bool] and not character.jumping:
                    character.setState("idle")
            #can block if not jumping
            if self.keyboard.down[bool] and not character.jumping:
                character.blocking()
                character.setState("block")
            character.move()
            character.setfacing(other)

    def update(self, round):
        #updates the movements for both character
        self.movements(self.characters[0], self.characters[1], 0)
        self.movements(self.characters[1], self.characters[0], 1)

        #checks for wall collisions
        for wall in self.walls:
            for character in self.characters:
                #moves characters out of walls if collision occurs
                if wall.touch(character) == 'right':
                    character.pos = Vector(wall.lEdge - (character.sprite.scaling * character.sprite.spriteDim[0] / 2), character.pos.getY())
                elif wall.touch(character) == 'left':
                    character.pos = Vector(wall.rEdge + (character.sprite.scaling * character.sprite.spriteDim[0] / 2), character.pos.getY())

        #checks for platform collisions
        for platform in self.platforms:
            for character in self.characters:
                if platform.touch(character):
                    #stops falling on collision with platform
                    character.stop_fall()
                else:
                    #fall
                    character.fall()
                #make sure no character goes under platform
                if (character.pos.getY() + (character.sprite.scaling * character.sprite.spriteDim[1] / 2)) - 4 > platform.edge_top:
                    character.pos = Vector(character.pos.getX(),
                                           platform.edge_top - (character.sprite.scaling * character.sprite.spriteDim[1] / 2) - 4)
        for character in self.characters:
            if character.dead:
                round.over(character)

