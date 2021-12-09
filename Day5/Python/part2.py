import numpy as np
import pprint

x1, x2, y1, y2 = [], [], [], []

with open('input') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(' -> ')
        curr1 = line[0].split(',')
        curr2 = line[1].split(',')
        x1.append(int(curr1[0]))
        x2.append(int(curr2[0]))
        y1.append(int(curr1[1]))
        y2.append(int(curr2[1]))

data = np.transpose(np.array([x1, y1, x2, y2]), (1,0))

minX = min(min(data[:, 0]), min(data[:,2]))
maxX = max(max(data[:, 0]), max(data[:,2]))
minY = min(min(data[:, 1]), min(data[:,3]))
maxY = max(max(data[:, 1]), max(data[:,3]))

grid = np.zeros(shape=(maxX+1,maxY+1), dtype=int)

def generateLine(line):
    if line[0] == line[2] and line[3] > line[1]:
        points = [(line[0], y) for y in list(range(line[1], line[3] + 1))]
    elif line[0] == line[2]:
        points = [(line[0], y) for y in list(range(line[3], line[1] + 1))]
    elif line[1] == line[3] and line[2] > line[0]:
        points = [(x, line[1]) for x in list(range(line[0], line[2] + 1))]
    elif line[1] == line[3]:
        points = [(x, line[1]) for x in list(range(line[2], line[0] + 1))]
    elif abs(line[3] - line[1]) == abs(line[2] - line[0]):
        maxY, minY = max(line[3], line[1]), min(line[3], line[1])
        maxX, minX = max(line[2], line[0]), min(line[2], line[0])
        revX = line[2] < line[0]
        revY = line[3] < line[1]
        x = list(range(minX, maxX+1))
        y = list(range(minY, maxY+1))
        if revY: y.reverse()
        if revX: x.reverse()
        points = []
        for idx, val in enumerate(x):
            points.append((list(x)[idx], list(y)[idx]))
    else:
        return
    return points

def markGrid(grid, points):
    for point in points:
        grid[point[1]][point[0]] += 1
    return grid

def markLines(grid, data):
    for line in data:
        points = generateLine(line)
        if points != None:
            grid = markGrid(grid, points)
    return grid

def countMoreThanValue(grid, value):
    count = 0
    for line in grid:
        for item in line:
            if item >= value:
                count += 1
    return count

grid = markLines(grid, data)

pprint.pprint(grid)

count = countMoreThanValue(grid, 2)

print('The number of values at or above 2 is: ', count)