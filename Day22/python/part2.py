import regex as re
from time import time

inp = input('What data set do you want? ')
with open('../data/'+inp) as f:
    lines = f.read().split('\n')
    lines = [line.split(' ') for line in lines]
    lines = [[line[0], re.findall(r'-?\d+',line[1])] for line in lines]
for idx,line in enumerate(lines): lines[idx][1] = [int(item) for item in line[1]]
for idx, line in enumerate(lines): lines[idx] = (line[0], ((line[1][0], line[1][1]), (line[1][2], line[1][3]), (line[1][4], line[1][5])))

# Ok saw this hint on reddit from u/Goodwine but basically the intersections are going to be seperate cubes
def intersect1d(a,b):
    return a[0] <= b[1] and b[0] <= a[1]
def doesItIntersect(a,b):
    (_, (xA, yA, zA)) = a; (_, (xB, yB, zB)) = b
    return intersect1d(xA,xB) and intersect1d(yA,yB) and intersect1d(zA,zB)
def intersection(a, b):
    _, (xA, yA, zA) = a; _, (xB, yB, zB) = b
    xRange = sorted([*xA, *xB])[1:3]
    yRange = sorted([*yA, *yB])[1:3]
    zRange = sorted([*zA, *zB])[1:3]
    return xRange, yRange, zRange
def combine(cube, cubes):
    state, ((x1,x2), (y1,y2), (z1,z2)) = cube
    toDel = set(); toAdd = set(); selfadded = False
    for cuboid in cubes:
        if not doesItIntersect(cube, cuboid): continue
        else:
            stateC, ((xx1, xx2), (yy1, yy2), (zz1, zz2)) = cuboid
            xRange, yRange, zRange = intersection(cube, cuboid)
            toDel.add(cuboid); selfadded = True

            if xx1 < xRange[0]: toAdd.add((stateC, ((xx1, xRange[0]), (yy1, yy2), (zz1, zz2))))
            if xRange[1] < xx2: toAdd.add((stateC, ((xRange[1] + 1, xx2), (yy1, yy2), (zz1, zz2))))
            if yy1 < yRange[0]: toAdd.add((stateC, ((xx1, xx2), (yy1, yRange[0]), (zz1, zz2))))
            if yRange[1] < yy2: toAdd.add((stateC, ((xx1, xx2), (yRange[1]+1, yy2), (zz1, zz2))))
            if zz1 < zRange[0]: toAdd.add((stateC, ((xx1, xx2), (yy1, yy2), (zz1, zRange[0]))))
            if zRange[1] < zz2: toAdd.add((stateC, ((xx1, xx2), (yy1, yy2), (zRange[1]+1, zz2))))

            toAdd.add((stateC, ((min(xRange[0],x1), max(x2, xRange[1])), (min(yRange[0], y1), max(yRange[1], y2)), (min(z1,zRange[0]), max(z2,zRange[1])))))
    for td in toDel: cubes.remove(td)
    for ta in toAdd: cubes.add(ta)
    if not selfadded: cubes.add(cube)
def initializeCubes(lines):
    cubes = set()
    for line in lines: combine(line, cubes)
    return cubes
def diff(axis): return axis[1] - axis[0] + 1
def solvePart2(cubes):
    p2 = 0
    for cube in cubes:
        (_, (x, y, z)) = cube
        p2 += diff(x)*diff(y)*diff(z)
    return p2

solution = solvePart2(initializeCubes(lines))

print(int(solution))