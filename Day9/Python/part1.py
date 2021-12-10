import numpy as np
import pprint as pr

with open('input') as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        lines[idx] = list(line.strip())
        lines[idx] = [int(item) for item in lines[idx]]

lines = np.array(lines)

def checkLowPoint(point, lines):
    x,y = point[0],point[1]
    if x == 0 and y == 0:
        return lines[x,y] < lines[x,y+1] and lines[x,y] < lines[x+1,y]
    elif x == 0 and y == len(lines[0]) - 1:
        return lines[x,y] < lines[x,y-1] and lines[x,y] < lines[x+1,y]
    elif x == len(lines) - 1 and y == 0:
        return lines[x,y] < lines[x-1,y] and lines[x,y] < lines[x,y+1]
    elif x == len(lines) - 1 and y == len(lines[0]) - 1:
        return lines[x,y] < lines[x-1,y] and lines[x,y] < lines[x,y-1]
    elif x == 0:
        return lines[x,y] < lines[x,y-1] and lines[x,y] < lines[x,y+1] and lines[x,y] < lines[x+1,y]
    elif x == len(lines) - 1:
        return lines[x,y] < lines[x-1,y] and lines[x,y] < lines[x,y-1] and lines[x,y] < lines[x,y+1]
    elif y == 0:
        return lines[x,y] < lines[x,y+1] and lines[x,y] < lines[x-1,y] and lines[x,y] < lines[x+1,y]
    elif y == len(lines[0]) - 1:
        return lines[x,y] < lines[x,y-1] and lines[x,y] < lines[x-1,y] and lines[x,y] < lines[x+1,y]
    else:
        return lines[x,y] < lines[x,y-1] and lines[x,y] < lines[x-1,y] and lines[x,y] < lines[x+1,y] and lines[x,y] < lines[x,y+1]

def findLowPoints(lines):
    lowPoints = set()
    for idx, line in enumerate(lines):
        for i, val in enumerate(line):
            curr = checkLowPoint((idx,i), lines)
            if curr: lowPoints.add((idx, i))
    return lowPoints

def findRiskLevel(point):
    x, y = point[0], point[1]
    return lines[x,y] + 1

def findAllRiskLevels(points):
    allRiskLevels = []
    for point in points:
        allRiskLevels.append(findRiskLevel(point))
    return allRiskLevels


def part1(lines):
    lowPoints = findLowPoints(lines)
    allRiskLevels = findAllRiskLevels(lowPoints)
    return sum(allRiskLevels)

print('Answer to part 1 is : ', part1(lines))
