# Imports
import enum
from string import ascii_uppercase as upper
from networkx.classes.function import neighbors
import numpy as np
from pprint import pprint as pretty
from igraph import Graph, Plot

# Data preperations
inp = input('What data set do you want? ')
with open('../data/'+inp) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    data = np.array([np.array([item for item in line]) for line in lines])
    for i,d in enumerate(data):
        if i == 3 or i == 4:
            data[i] = np.array(['#','#',*d,'#','#'])
points = {}
correctPositions = {'A': ((3,2), (3,3)), 'B': ((5,2), (5,3)), 'C': ((7,2), (7,3)), 'D': ((9,2), (9,3))}
cost = {'A':1, 'B': 10, 'C':100, 'D':1000}
for idx, line in enumerate(data):
    for i, v in enumerate(line):
        if v in upper:
            if v+str(1) in points.keys(): points[v+str(2)] = [idx,i]
            else: points[v+str(1)] = [idx, i]
# Try to figure out how to solve the problem. I probably should use a graph but how should it work?
# Like how do I figure out in which order to move the boxes? Do I still need the distances? No that is just the number of edges traversed
# Let's just start by populating the graph
floorLayout = Graph()
value = []; coor = []
for idx, line in enumerate(data):
    for i, v in enumerate(line):
        if v != '#': 
            value.append(v)
            coor.append((idx,i))
floorLayout.add_vertices(len(value))
floorLayout.vs['coor'] = coor
floorLayout.vs['value'] = value

def findNeighbours(point, lines):
    neighbours = []
    if point[0] > 0 and lines[point[0]-1][point[1]] != '#': neighbours.append((point[0]-1,point[1]))
    if point[0] < len(lines[0]) - 1 and lines[point[0]+1][point[1]] != '#': neighbours.append((point[0]+1, point[1]))
    if point[1] > 0 and lines[point[0]][point[1]-1] != '#': neighbours.append((point[0], point[1]-1))
    if point[1] < len(lines) - 1 and lines[point[0]][point[1]+1] != '#': neighbours.append((point[0], point[1]+1))
    return neighbours

def populateEdges(coor, data):
    edges = []
    for idx, c in enumerate(coor):
        nghbrs = findNeighbours(c, data)
        for nghbr in nghbrs:
            i = coor.index(nghbr)
            if (i, idx) not in edges: edges.append((idx, i))
    return edges

edges = populateEdges(coor, data)
floorLayout.add_edges(edges)

pretty(floorLayout.vs['value '])