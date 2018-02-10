import os

def getIndex(find, lst):
    i = 0
    while i < len(lst):
        if find == lst[i]:
            return i
        i = i + 1
    return -1

def contains(find, lst):
    for obj in lst:
        if find == obj:
            return True
    return False
    
def displayGames():
    path = "Saves"
    files = os.listdir(path)
    return files
