try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Keyboard:

    #uses boolean arrays for inputs - [0] is for p1, [1] is for p2
    def __init__(self):
        self.right = [False,False]
        self.left = [False,False]
        self.up = [False,False]
        self.down = [False,False]
        self.attack = [False,False]
        self.fire = [False,False]
        self.idle = [False, False]
        #binds [0]-[5] are p1 bindings, [6]-[11] are p2 bindings

        self.key_binds = ['w','a','s','d','q','e','i','j','k','l','u','o']

    #key down handler, sets booleans on keypress
    def key_down(self, key):
        #player 1
        if key == simplegui.KEY_MAP[self.key_binds[3]]:
            #if 'd', go right
            self.right[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[1]]:
            #if 'a', go left
            self.left[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[0]]:
            #if 'w', jump
            self.up[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[2]]:
            #if 's', block
            self.down[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[5]]:
            #if 'e', attack
            self.attack[0] = True
        if key == simplegui.KEY_MAP[self.key_binds[4]]:
            #if 'q', fire
            self.fire[0] = True

        ##repeated for player 2
        if key == simplegui.KEY_MAP[self.key_binds[9]]:
            self.right[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[7]]:
            self.left[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[6]]:
            self.up[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[8]]:
            self.down[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[11]]:
            self.attack[1] = True
        if key == simplegui.KEY_MAP[self.key_binds[10]]:
            self.fire[1] = True
        self.checkIdle(0)
        self.checkIdle(1)

    #key up handler, same principle as key_down
    def key_up(self, key):
        #player 1
        if key == simplegui.KEY_MAP[self.key_binds[3]]:
            self.right[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[1]]:
            self.left[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[0]]:
            self.up[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[2]]:
            self.down[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[5]]:
            self.attack[0] = False
        if key == simplegui.KEY_MAP[self.key_binds[4]]:
            self.fire[0] = False
        #player 2
        if key == simplegui.KEY_MAP[self.key_binds[9]]:
            self.right[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[7]]:
            self.left[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[6]]:
            self.up[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[8]]:
            self.down[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[11]]:
            self.attack[1] = False
        if key == simplegui.KEY_MAP[self.key_binds[10]]:
            self.fire[1] = False
        self.checkIdle(0)
        self.checkIdle(1)

    def checkIdle(self,b):
        if any([self.right[b], self.left[b], self.up[b], self.down[b], self.attack[b], self.fire[b]]):
            self.idle[b] = False
        else:
            self.idle[b] = True