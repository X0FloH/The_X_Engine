def clickedRect(mouseX, mouseY, mouseClick, xPos, yPos, xSize, ySize):
    if mouseX > xPos and mouseX < xPos + xSize and mouseY > yPos and mouseY < yPos + ySize and mouseClick:
        return True
    else:
        return False
