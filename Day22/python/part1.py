import regex as re
from time import time

inp = input('What data set do you want? ')
with open('../data/'+inp) as f:
    lines = f.read().split('\n')
    lines = [line.split(' ') for line in lines]
    lines = [[line[0], re.findall(r'-?\d+',line[1])] for line in lines]
for idx,line in enumerate(lines): lines[idx][1] = [int(item) for item in line[1]]
for idx, line in enumerate(lines): lines[idx] = (line[0], (line[1][0], line[1][1]), (line[1][2], line[1][3]), (line[1][4], line[1][5]))

def getPoints(ranges):
    xRange = list(ranges[0]); yRange = list(ranges[1]); zRange = list(ranges[2])
    points = set()
    if xRange[0] < -50: xRange[0] = -50
    if xRange[1] > 50: xRange[1] = 50
    if yRange[0] < -50: yRange[0] = -50
    if yRange[1] > 50: yRange[1] = 50
    if zRange[0] < -50: zRange[0] = -50
    if zRange[1] > 50: zRange[1] = 50
    if xRange[0] > xRange[1] or yRange[0] > yRange[1] or zRange[0] > zRange[1]: return points
    for x in range(xRange[0],xRange[1]+1):
        for y in range(yRange[0], yRange[1]+1):
            for z in range(zRange[0], zRange[1]+1):
                points.add((x,y,z))
    return points

def applyLine(litPoints, line):
    points = getPoints(line[1:])
    if line[0] == 'on': litPoints.update(points)
    else: litPoints.difference_update(points)
    return litPoints

def applyAllLines(lines):
    litPoints = set()
    for line in lines: litPoints = applyLine(litPoints, line)
    return litPoints

initialTime = time()
litPoints = applyAllLines(lines)
finalTime = time()
print(len(litPoints))
print(finalTime - initialTime)