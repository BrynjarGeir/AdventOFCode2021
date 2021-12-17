input = ['input', 'example']

lines = [line.strip() for line in open(input[0]).readlines()]

idx = lines.index('')

dots = lines[:idx]
folds = lines[idx+1:]

tmpDots = set()
maxX = 0; maxY = 0
for item in dots:
    item = item.split(',')
    x,y = int(item[0]), int(item[1])
    if x > maxX: maxX = x
    if y > maxY: maxY = y
    tmpDots.add((x,y))

dots = tmpDots

tmpFolds = []
for fold in folds:
    item = fold.split('=')
    tmpFolds.append((item[0][-1], int(item[1])))
folds = tmpFolds

def projectPointsX(dots, maxX, maxY):
    middleLine = int(maxX / 2)
    print(maxX, middleLine)
    tmpDots = set()
    for dot in dots:
        if dot[0] > middleLine:
            tmpDots.add((maxX-dot[0],dot[1]))
        else:
            tmpDots.add(dot)
    maxX = int(maxX/2)
    dots = tmpDots
    return dots, maxX, maxY



def projectPointsY(dots, maxX, maxY):
    middleLine = int(maxY / 2)
    print(maxY, middleLine)
    tmpDots = set()
    for dot in dots:
        if dot[1] > middleLine:
            tmpDots.add((dot[0], maxY-dot[1]))
        else:
            tmpDots.add(dot)
    maxY = int(maxY / 2)
    dots = tmpDots
    return dots, maxX, maxY

def projectPoints(dots, fold, maxX, maxY):
    if fold[0] == 'y': return projectPointsY(dots, maxX, maxY)
    else: return projectPointsX(dots, maxX, maxY)

def everyFold(dots, folds, maxX, maxY):
    for fold in folds:
        print(fold)
        dots, maxX, maxY = projectPoints(dots, fold, maxX, maxY)
    return dots, maxX, maxY

dots, maxX, maxY = everyFold(dots, folds, maxX, maxY)
