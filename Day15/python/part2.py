from igraph import Graph
import pprint as pp

lines = open('input').readlines()
lines = [[int(item) for item in line.strip()] for line in lines]

def generate_full_cave_map(cave): 
    original_width = len(cave[0])
    original_height = len(cave)

    # for row in range(5):

    for row in range(5):
        for row_idx in range(original_height):
            for col in range(5): 
                if row == 0 and col == 0: 
                    continue 
                for col_idx in range(original_width):
                    original_value = cave[row_idx][col_idx]
                    new_value = original_value + (col + row)
                    while new_value > 9: 
                        new_value -= 9
                    
                    # Add the new value to the cave 
                    cave[row_idx + row * original_height].append(new_value) 

        # Starting a new segment, append original height 
        if row != 4:
            for _ in range(original_height):
                cave.append([])


    return cave

lines = generate_full_cave_map(lines)

points = [[(x,y) for x in range(len(lines[0]))] for y in range(len(lines))]
startingPoint = points[0][0]
endingPoints = points[-1]
grid = {}
fromPtToIdx = {}
fromIdxToPt = {}

# Have to expand after this
#Populating from index to point and the other way around and also populate grid
idx = 0
for line in points:
    for point in line:
        grid[point] = [lines[point[0]][point[1]], False]
        fromPtToIdx[point] = idx
        fromIdxToPt[idx] = point
        idx += 1

#Find all the neighbours of particular point
def findNeighbours(point, lines):
    neighbours = []
    if point[0] > 0: neighbours.append((point[0]-1,point[1]))
    if point[0] < len(lines[0]) - 1: neighbours.append((point[0]+1, point[1]))
    if point[1] > 0: neighbours.append((point[0], point[1]-1))
    if point[1] < len(lines) - 1: neighbours.append((point[0], point[1]+1))
    return neighbours
#Find all the neighbours of every point
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
