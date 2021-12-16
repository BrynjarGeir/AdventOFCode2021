import numpy as np
import pprint as pp

txt = 'input'
#Reading in data and cleaning it
with open(txt) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [[int(item) for item in line] for line in lines]

grid = np.array(lines)
gridBool = np.zeros(grid.shape, dtype=bool)

# Everybody increases at the start of each round
def addOneToGrid(grid):
    return grid + 1
#Just simplifying keeping track of neighbours for neighbour flashing
#Finding neighbours given a specific point
def findNeighbours(point):
    x,y = point[0],point[1]
    return [[x-1,y-1], [x-1,y], [x-1,y+1], [x,y-1], [x,y+1], [x+1,y-1], [x+1,y], [x+1,y+1]]
#Finding neighbours for everyone in the grid
def findAllNeighbours(grid):
    allNeighbours = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for idx, line in enumerate(grid):
        for i, item in enumerate(line):
            allNeighbours[idx][i] = findNeighbours([idx, i])
    return allNeighbours
#Everybody at 9 or above increases their neighbours by 1, with tmp
def increaseNeighboursOf9(grid, gridBool, allNeighbours):
    numberOfNines = np.count_nonzero(grid>9)
    lstNumberOfNines = 0
    while(numberOfNines != lstNumberOfNines):
        for idx, line in enumerate(grid):
            for i, item in enumerate(line):
                if item > 9 and gridBool[idx][i] == False:
                    for n in allNeighbours[idx][i]:
                        x,y = n[0],n[1]
                        if -1 < x < len(grid) and -1 < y < len(grid[0]):
                            grid[x,y] += 1
                    gridBool[idx, i] = True
        lstNumberOfNines = numberOfNines
        numberOfNines = np.count_nonzero(grid>9)
    return grid, gridBool
#Reset everyone that is at or above 9 to 0 and sets gridBool to false and keeps count of how many flashes have occurred
def resetGrids(grid, gridBool):
    flashes = np.count_nonzero(gridBool)
    gridBool = np.zeros(grid.shape, dtype=bool)
    for idx, line in enumerate(grid):
        for i, item in enumerate(line):
            if item > 9:
                grid[idx, i] = 0
    return grid, gridBool, flashes

def part1(grid, gridBool, iterations):
    allNeighbours = findAllNeighbours(grid)
    flashes = 0
    for _ in range(iterations):
        grid = addOneToGrid(grid)
        grid, gridBool = increaseNeighboursOf9(grid, gridBool, allNeighbours)
        grid, gridBool, currFlashes = resetGrids(grid, gridBool)
        flashes += currFlashes
    return grid, gridBool, flashes

iterations = 100
grid, gridBool, flashes = part1(grid, gridBool, iterations)

print('The answer to part 1 is ',flashes)

print('After ',iterations,' iterations the grid looks like:')
pp.pprint(grid)


