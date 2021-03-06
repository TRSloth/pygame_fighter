from Fighter import Master
from Fighter.Keyboard import InstructionsKeyboard
from Fighter.Sprite import StaticSprite
from Fighter.Mouse import Mouse


kbd = InstructionsKeyboard()
timer = 0

def init():
    
    Master.masterframe.setDrawHandler(draw)
    Mouse.screen = "splash"
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)
    Master.masterframe.setMouseHandler(Mouse.handler)
    Master.masterframe.start()

def draw(canvas):
    updateText(canvas)
    global timer
    if timer > 90:
        red.draw(canvas)
    if timer > 130:
        yellow.draw(canvas)
    if timer > 170:
        green.draw(canvas)
    if timer > 210:
        canvas.draw_text("Press any button to start!", (50, 450), 40, "White")
        if kbd.next:
            Master.menu()
    timer +=1


def updateText(canvas):
    if(road.dest[0] < 250):
        road.setDest((road.dest[0] + 15, road.dest[1]))
    if(wars.dest[0] > 250):
        wars.setDest((wars.dest[0] - 15, wars.dest[1]))
    road.draw(canvas)
    wars.draw(canvas)


greenURL = "https://i.ibb.co/649GzHp/green.png"
redURL = "https://i.ibb.co/89RbvjL/red.png"
roadURL = "https://i.ibb.co/JB8LF86/road.png"
warsURL = "https://i.ibb.co/VCdSVvJ/wars.png"
yellowURL = "https://i.ibb.co/dLN96Fd/yellow.png"


red = StaticSprite(redURL, (140,350), 1)
green = StaticSprite(greenURL, (360, 350), 1)
yellow = StaticSprite(yellowURL, (250, 350), 1)
road = StaticSprite(roadURL, (-100, 180), 1)
wars = StaticSprite(warsURL, (960, 250), 1)
