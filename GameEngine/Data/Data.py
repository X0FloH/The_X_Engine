import os

def getIndex(find, lst):
    i = 0
    while i < len(lst):
        if find == lst[i]:
            return i
        i = i + 1
    return -1
def displayGames():
    path = "Saves"
    files = os.listdir(path)
    return files
