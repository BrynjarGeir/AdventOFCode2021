from collections import defaultdict
from igraph import Graph
import pprint as pp

lines = open('example').readlines()
lines = [[int(item) for item in line.strip()] for line in lines]

points = [[(x,y) for x in range(len(lines[0]))] for y in range(len(lines))]
startingPoint = points[0][0]
endingPoints = points[-1]
grid = {}
fromPtToIdx = {}
fromIdxToPt = {}

idx = 0
for line in points:
    for point in line:
        grid[point] = [lines[point[0]][point[1]], False]
        fromPtToIdx[point] = idx
        fromIdxToPt[idx] = point
        idx += 1

def findNeighbours(point, lines):
    neighbours = []
    if point[0] > 0: neighbours.append((point[0]-1,point[1]))
    if point[0] < len(lines[0]) - 1: neighbours.append((point[0]+1, point[1]))
    if point[1] > 0: neighbours.append((point[0], point[1]-1))
    if point[1] < len(lines) - 1: neighbours.append((point[0], point[1]+1))
    return neighbours

def findAllNeighbours(lines):
    allNeighbours = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            allNeighbours[(x,y)] = findNeighbours((x,y), lines)
    return allNeighbours

def edgePointIndexes(graph, grid, points, lines, fromPtToIdx):
    edgeIndexes = []; weights = []
    for line in points:
        for point in line:
            start = fromPtToIdx[point]
            neighbours = findNeighbours(point, lines)
            for neighbour in neighbours: 
                weights.append(grid[neighbour][0])
                end = fromPtToIdx[neighbour]
                edgeIndexes.append((start, end))
    graph.add_edges(edgeIndexes)
    return graph, weights



allNeighbours = findAllNeighbours(lines)
graph = Graph(directed=True)
graph.add_vertices(len(fromPtToIdx))
graph, weights = edgePointIndexes(graph, grid, points, lines, fromPtToIdx)
graph.es['weights'] = weights
start = 0
end = fromPtToIdx[points[-1][-1]]
sps = graph.shortest_paths(start, target=end, weights='weights', mode='OUT')

print(int(sps[0][0]))
