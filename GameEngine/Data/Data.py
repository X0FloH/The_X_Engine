import os

def magInverse(num):
    return 1-num

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

def makeFile(path):
    file = open(path, 'a+')
    file.close()

def writeFile(path, text, mode='r+'):
    makeFile(path)
    file = open(path, mode)
    file.write(text)
    file.close()

def readFile(path, mode="Lines"):
    file = open(path, 'r+')
    if mode=="Lines":
        lines = file.readlines()
        return lines
    if mode == "File":
        fileText = file.read()
        return fileText

def writeFileLines(path, text, line):
    lines = readFile(path)
    lines[line] = text+"\n"
    file = open(path, 'w')
    file.writelines(lines)
    file.close()
