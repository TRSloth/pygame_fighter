#Jed Arno

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Fighter.Sprite import Sprite
from Fighter.Sprite import StaticSprite
from Fighter.Keyboard import Keyboard
from Fighter.Cursor import Cursor
from Fighter.Navigation import Navigation
from Fighter import Master

kbd = Keyboard()

def init():
    Master.masterframe.setDrawHandler(drawSpriteSheet)
    Master.masterframe.setKeydownHandler(kbd)
    Master.masterframe.setKeyupHandler(kbd)

cursor1 = Cursor([125, 105], [125, 255], [250, 255], [250, 105], 'cyan')
cursor1.addPos([250, 105], [250, 255], [375, 255], [375, 105], 0)
cursor1.addPos([125, 255], [125, 420], [250, 420], [250, 255], 1)
cursor1.addPos([250, 255], [250, 420], [375, 420], [375, 255], 1)

cursor2 = Cursor([125, 105], [125, 255], [250, 255], [250, 105], 'red')
cursor2.addPos([250, 105], [250, 255], [375, 255], [375, 105], 0)
cursor2.addPos([125, 255], [125, 420], [250, 420], [250, 255], 1)
cursor2.addPos([250, 255], [250, 420], [375, 420], [375, 255], 1)

player1 = Navigation(cursor1, kbd, 0)
player2 = Navigation(cursor2, kbd, 1)

selection = StaticSprite("https://i.ibb.co/wCnM7pP/fullscaled.png", 247, 322, [250, 255], 1)
previewSprites = [ "https://i.ibb.co/M7Ff2wx/redsheet.png",

    "https://i.ibb.co/2hv9qcq/bluesheet.png",
    "https://i.ibb.co/K2616MG/greensheet.png",
    "https://i.ibb.co/CbMDdVC/yellowsheet.png"]

#previewSprites = [".//Sprites//redsheet.png", ".//Sprites//bluesheet.png", ".//Sprites//greensheet.png", ".//Sprites//yellowsheet.png"]
names = [".//Sprites//redPlaceHolder.png", ".//Sprites//bluePlaceHolder.png", ".//Sprites//greenPlaceHolder.png", ".//Sprites//yellowPlaceHolder.png"]
finalnames = [ "Red", "Blue", "Green", "Yellow"]
#previewSprite1 = Sprite(sprites[cursor1.getSelection()], 210, 52, 2, 14, (50, 250), 8)
#previewSprite2 = Sprite(sprites[cursor2.getSelection()], 210, 52, 2, 14, (450, 250), 8)
def ready():
    if cursor1.getSelected() and cursor2.getSelected():

        cursor1.deselect()
        cursor2.deselect()
        return True
    else:
        return False

def drawSpriteSheet(canvas):
    canvas.draw_polygon([[125, 105], [125, 420], [375, 420], [375, 105]], 1, 'Grey', 'Grey')
    player1.update()
    player2.update()
    selection.draw(canvas)
    cursor1.draw(canvas)
    cursor2.draw(canvas)
    #Wouldn't let me change the sprite source whilst running
    #previewSprite1.draw(canvas)
    #previewSprite2.draw(canvas)

    Sprite(previewSprites[cursor1.previewSelection()], 210, 52, 2, 14, (50, 250), 8, "idle", "right").updateStatic(canvas)
    Sprite(previewSprites[cursor2.previewSelection()], 210, 52, 2, 14, (450, 250), 8, "idle", "left").updateStatic(canvas)

    if cursor1.getSelected():
        Sprite(names[cursor1.previewSelection()], 400, 15, 2, 14, (50, 50), 4, "idle", "right").draw(canvas)
    if cursor2.getSelected():
        Sprite(names[cursor2.previewSelection()],  400,  15, 2, 14, (450, 50), 4, "idle", "left").draw(canvas)
        
    if ready():

        Master.gameLoop(finalnames[cursor1.previewSelection()], finalnames[cursor2.previewSelection()])
