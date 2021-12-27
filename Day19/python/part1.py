from ast import literal_eval as le
import pprint as pp
from math import sqrt, pow
import numpy as np
from igraph import Graph
#Data preparation
data = open('../data/example').readlines()
data = [d.strip() for d in data]
tmpDict = {}; tmp = []
for i,d in enumerate(data):
    if 'scanner' in d: key = d.replace('-','').replace(' s','s').rstrip(' ')
    elif d == '' or i == len(data)-1:
        tmpDict[key] = tmp
        tmp = []
    else:
        tmp.append(d)
for key in tmpDict:
    currList = tmpDict[key]
    for idx, item in enumerate(currList):
        currList[idx] = le(item)
    tmpDict[key] = currList
data = tmpDict
rotations = [([2, 0, 1], [-1, -1, 1]), ([0, 1, 2], [1, -1, -1]), ([2, 1, 0], [-1, -1, -1]), ([2, 1, 0], [1, -1, 1]),
             ([0, 2, 1], [-1, -1, -1]), ([1, 2, 0], [1, -1, -1]), ([1, 0, 2], [-1, -1, -1]), ([1, 2, 0], [1, 1, 1]),
             ([0, 2, 1], [-1, 1, 1]), ([0, 1, 2], [-1, 1, -1]), ([0, 2, 1], [1, -1, 1]), ([2, 0, 1], [-1, 1, -1]),
             ([1, 0, 2], [1, 1, -1]), ([2, 1, 0], [1, 1, -1]), ([2, 0, 1], [1, 1, 1]), ([2, 1, 0], [-1, 1, 1]),
             ([0, 1, 2], [1, 1, 1]), ([1, 0, 2], [1, -1, 1]), ([1, 0, 2], [-1, 1, 1]), ([0, 1, 2], [-1, -1, 1]),
             ([1, 2, 0], [-1, 1, -1]), ([1, 2, 0], [-1, -1, 1]), ([0, 2, 1], [1, 1, -1]), ([2, 0, 1], [1, -1, -1])]

#End of data preparation

##Start of solution
## What if I just try to find inside each axis points that are equal distance from the first point
## Like what if I just look at the first point for each scanner and create a list of the difference for each axis for each point??
## Or rather look at the first point in each scanner and the distance to all it's neighbours? In the end I will probably have to find all
## the neighbours of all the points but let's start with one (that would take a loooong time)
def dist(a, b):
    return sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2) + pow(a[2]-b[2], 2))

def firstPointNeighbours(scanner):
    distances = []
    points = []
    for i in range(len(scanner)):
        first = scanner[i]
        for point in scanner:
            if first != point:
                distances.append(dist(first, point))
                points.append((first, point))
    return distances, points

def allFirstPointNeighbours(data):
    allDistances = {}
    points = {}
    for key in data:
        allDistances[key], points[key] = firstPointNeighbours(data[key])
    return allDistances, points

def findSameDistanceInAnotherScanner(allDistances, points):
    matchingPointsAndDistance = {}
    for scanner in allDistances:
        for idx, dist in enumerate(allDistances[scanner]):
            for sc in allDistances:
                for i, d in enumerate(allDistances[sc]):
                    if scanner != sc and dist == d:
                        keys = matchingPointsAndDistance.keys(); a = points[scanner][idx]; b = points[sc][i]
                        if (a,b) not in keys and (b,a) not in keys and ((a[1],a[0]), b) not in keys and (a,(b[1],b[0])) not in keys and ((a[1],a[0]), (b[1],b[0])) not in keys:# and d not in matchingPointsAndDistance.values():
                            matchingPointsAndDistance[((scanner, sc),(a,b))] = d
    return matchingPointsAndDistance

allDistances, points = allFirstPointNeighbours(data)
matching = findSameDistanceInAnotherScanner(allDistances, points)
print('Finished Matching')
totally_matching = []
for value in matching.values():
    curr = [key for key in matching if matching[key] == value]
    totally_matching.append(curr[0])
print('Finished Totally Matching')
#Maybe I should create some dictionaries that map a point from one to the possible values it can take in another scanner
#Like what would that mean? Ok so let's say that we want to look at point a from scanner 0 (this would be a key) 
#The value would have to be like scanner 1: possible values and then tak intersection
#So if I can do this once the I get the corresponding total point value but still haven't figured out what to do about
#The totality of the thing, like how do I figure out how it is rotated? But first thing is first
possibilitiesMatch = {}
for m in totally_matching:
    curr = (m[0][0], m[0][1], m[1][0][0])
    if curr not in possibilitiesMatch.keys():
        possibilitiesMatch[curr] = set((m[1][1][0], m[1][1][1]))
    else: 
        prev = possibilitiesMatch[curr]
        new = set((m[1][1][0], m[1][1][1]))
        possibilitiesMatch[curr] = new.intersection(prev)
    curr = (m[0][0], m[0][1], m[1][0][1])
    if curr not in possibilitiesMatch.keys():
        possibilitiesMatch[curr] = set((m[1][1][0], m[1][1][1]))
    else:
        prev = possibilitiesMatch[curr]
        new = set((m[1][1][0], m[1][1][1]))
        possibilitiesMatch[curr] = new.intersection(prev)
    curr = (m[0][1], m[0][0], m[1][1][0])
    if curr not in possibilitiesMatch.keys():
        possibilitiesMatch[curr] = set((m[1][0][0], m[1][0][1]))
    else:
        prev = possibilitiesMatch[curr]
        new = set((m[1][0][0], m[1][0][1]))
        possibilitiesMatch[curr] = new.intersection(prev)
    curr = (m[0][1], m[0][0], m[1][1][1])
    if curr not in possibilitiesMatch.keys():
        possibilitiesMatch[curr] = set((m[1][0][0], m[1][0][1]))
    else:
        prev = possibilitiesMatch[curr]
        new = set((m[1][0][0], m[1][0][1]))
        possibilitiesMatch[curr] = new.intersection(prev)
print('Finished Possibilities Matching')
#Ok so I end up with a 1 to 1 match and at least for scanner 0 to 1 I get 12 results
#Maybe as expected I got some of these correct but others might be missing, but let's see
#Get 108/5/2 = 10.8 so I don't know maybe this is ok
#pp.pprint(len(possibilitiesMatch))
#I just youtubed something and caught a quick climpse (as in didn't copy anything but saw a comment that might help me)
#The comment was basically that Assume that one mapping is correct. That is, assume that a Beacon from one Scanner is the 
#Same as some other Beacon from another scanner. Can I from that find at least 11 other matches? Sounds like a reasonable idea
#And I've already found good candidates but how does assuming one help me find others? Like yes I assume two points are the same 
#but what about the projections? If I could assume two points I should be able to figure it out right? Like if I know that for
#One Scanner x2-x1 = a that should be the same for the other scanner, right? Like the difference between two points should be the same
#However the observer is situated So for scanner 0 and 1, 1 seems to be (x,y,z) to 0 but also (-1,-1,-1) this should mean I pretty much
#Can figure out everything for 1 in terms of 0 if these two points make sense. And I think I have exactly 12 overlapping so that is good
#Ok so let's figure out the projections for at least the first scanner (like in code not just by looking at it)
def checkProjection(scanner0, scanner1):
    try :
        possibilities = []
        for key in possibilitiesMatch:
            if scanner0 in key[0] and scanner1 in key[1]:
                possibilities.append((key, tuple(possibilitiesMatch[key])))
        prev = possibilities[0]; curr = possibilities[1]
        projections = []
        signs = [i==j for i,j in zip(np.sign(prev[0][2]), np.sign(prev[1][0]))]
        x0 = abs(prev[0][2][0]); x1 = abs(prev[1][0][0]); y0 = abs(prev[0][2][1]); y1 = abs(prev[1][0][1]); z0 = abs(prev[0][2][2]); z1 = abs(prev[1][0][2])
        x0Diff = prev[0][2][0] - curr[0][2][0]; x1Diff = prev[1][0][0] - curr[1][0][0]
        y0Diff = prev[0][2][1] - curr[0][2][1]; y1Diff = prev[1][0][1] - curr[1][0][1]
        z0Diff = prev[0][2][2] - curr[0][2][2]; z1Diff = prev[1][0][2] - curr[1][0][2]
        if abs(x0Diff) == abs(x1Diff):
            if signs[0]: projections.append(('x',1,x0-x1))
            else: projections.append(('x', -1, x0-x1))
        elif abs(x0Diff) == abs(y1Diff):
            if signs[0]: projections.append(('y',1,x0-y1))
            else: projections.append(('y', -1,x0-y1))
        elif abs(x0Diff) == abs(z1Diff):
            if signs[0]: projections.append(('z',1,x0-z1))
            else: projections.append(('z', -1,x0-z1))
        else: print('Points Not Matching!')
        if abs(y0Diff) == abs(x1Diff):
            if signs[1]: projections.append(('x',1,y0-x1))
            else: projections.append(('x', -1,y0-x1))
        elif abs(y0Diff) == abs(y1Diff):
            if signs[1]: projections.append(('y',1,y0-y1))
            else: projections.append(('y', -1,y0-y1))
        elif abs(y0Diff) == abs(z1Diff):
            if signs[1]: projections.append(('z',1,y0-z1))
            else: projections.append(('z', -1,y0-z1))
        else: print('Points Not Matching!')
        if abs(z0Diff) == abs(x1Diff):
            if signs[2]: projections.append(('x',1,z0-x1))
            else: projections.append(('x', -1,z0-x1))
        elif abs(z0Diff) == abs(y1Diff):
            if signs[2]: projections.append(('y',1,z0-y1))
            else: projections.append(('y', -1,z0-y1))
        elif abs(z0Diff) == abs(z1Diff):
            if signs[2]: projections.append(('z',1,z0-z1))
            else: projections.append(('z', -1,z0-z1))
        else: print('Points Not Matching!')
        return (projections, (scanner0, scanner1))
    except :
        #print(scanner0, scanner1, 'Some problem with the projection for these scanners. Probably no projections or something.')
        return possibilities

def checkAllProjections(lengthOfDataKeys):
    allProjections = []
    for i in range(lengthOfDataKeys):
        for j in range(lengthOfDataKeys):
            if i != j:
                scanner0 = 'scanner ' + str(i)
                scanner1 = 'scanner '+ str(j)
                curr = checkProjection(scanner0, scanner1)
                if curr not in allProjections: allProjections.append(curr)
    return allProjections


allProjections = checkAllProjections(len(data))
print('Finished all projections')

# I'm just trying to see if there is a path from scanner 0 to scanner 4 that goes through all paths
# Or rather I want to write any scanner data in terms of scanner 0
# So I'm just going to Start by removing duplicates (1-->2 = 2-->1)
def removeUnProjections(allProjections):
    updatedProjections = []
    completedProjections = []
    for item in allProjections:
        if item != [] and set((item[1][0], item[1][1])) not in completedProjections:
            completedProjections.append(set((item[1][0],item[1][1])))
            updatedProjections.append(item)
    return updatedProjections
# This one should be used to turn a projection like scanner2, scanner 4 to scanner0, scanner4
# Basically so I can have one projection for each scanner to get to 0 that we decided to be the base coordinate
# system 
def projectionsInTermsOfZero(allProjections): 
    projectionPaths = {}
    keys = allProjections.keys()
    g = Graph(); g.add_vertices(len(data)); g.add_edges(keys)
    for idx in range(1,len(data)):
        projectionPaths[idx] = g.get_all_simple_paths(0, to=idx)
    return projectionPaths
# Now I want to get the actual projection for any one scanner, finally
def totalProjection(allProjections, projectionPaths):
    actualScannerProjection = {}
    for scanner in projectionPaths:
        if len(projectionPaths[scanner]) == 2:
            actualScannerProjection[scanner] = allProjections[(0,scanner)]
        else:
            path = projectionPaths[scanner].copy()
            scannerProjection = {'x':'x', 'y':'y', 'z':'z', 'fx':1, 'fy':1, 'fz':1, 'distx':0, 'disty':0, 'distz':0}
            while len(path)>1:
                currProjection = allProjections[(path[0],path[1])]
                x,y,z = currProjection
            return
    return actualScannerProjection

# I'm going to add one more function that will just take the list and create a dictionary to make things simpler
def fromListToDict(allProjections):
    dictionary = {}
    for item in allProjections:
        i,j = int(''.join(filter(str.isdigit,item[1][0]))),int(''.join(filter(str.isdigit,item[1][1]))) 
        dictionary[(i,j)] = item[0]
    return dictionary

# Getting the shortest path from dict of paths
def getShortestPath(projectionPaths):
    for scanner in projectionPaths:
        projectionPaths[scanner] = sorted(projectionPaths[scanner], key = len)[0]
    return projectionPaths
upProj = removeUnProjections(allProjections)
print('Finished upProj')

allProjections = fromListToDict(upProj)
print('Finished turning the list to dict')

# Ok so now I can see for each non zero scanner how to get from 0 to them
# Now I probably just need some kind of converter to convert from list of projections to one projection
# But first let's look at the shortest path
projectionPaths = getShortestPath(projectionsInTermsOfZero(allProjections))
print('Finished getting all the shortest paths')

pp.pprint(allProjections)
pp.pprint(projectionPaths)
