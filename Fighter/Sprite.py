try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


states = {
        "idle"  : [0, 2],
        "walk"  : [2, 2],
        "jump"  : [12, 1],
        "kick"  : [13, 1],
        "hit"   : [11, 1],
        "punch" : [4, 2],
        "fire"  : [6, 2],
        "block" : [10, 1],
        "die"   : [8, 2],
        "fireball" : [0, 4]
    }


class Sprite:

    #initialises sprite from local path, with spritesheet height and width, number of rows and columns, destination and size
    def __init__(self, path, width, height, rows, columns, destination, scale, state):
        self.img = simplegui.load_image(path)
        self.spriteDim = [(width / columns), height / rows]
        self.dest = destination
        self.scale = (self.spriteDim[0] * scale, self.spriteDim[1] * scale)
        self.columns = columns
        self.rows = rows
        self.frameIndex = [0, 0]
        self.currentState = states[state]
        self.timer = 0

    #sets destination of sprite (used in character class to update position
    def setDest(self, dest):
        self.dest = dest

    def changeState(self, state):
        self.currentState = states[state]

    #moves to nextSprite
    def nextSprite(self):
        self.frameIndex[0] = (self.frameIndex[0] + 1) % self.columns


    #draws sprite on canvas
    def draw(self, canvas):
        canvas.draw_image(self.img,
                                   (self.spriteDim[0] * self.frameIndex[0] + self.spriteDim[0] / 2,
                                   self.spriteDim[1] * self.frameIndex[1] + self.spriteDim[1] / 2),
                                   (self.spriteDim[0], self.spriteDim[1]),
                                    self.dest,
                                    self.scale
                                   )

    #draws sprite and cycles to next
    def update(self, canvas, position):
        self.setDest(position)
        self.draw(canvas)
        if self.timer % 6 == 0:
            self.nextSprite()
        self.timer += 1