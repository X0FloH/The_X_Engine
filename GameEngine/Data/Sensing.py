def inWindow(windowX, windowY, posX, posY, sizeX, sizeY):
    if posX < windowX and posX + sizeX > 0 and posY + sizeY > 0 and posY < windowY:
        return True
    else:
        return False
