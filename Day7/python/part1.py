import numpy as np
from numpy.core.numeric import Inf

txt = 'input'
with open(txt) as f:
    line = f.readline()
    line = line.strip().split(',')
    line = [int(x) for x in line]

crabs = np.array(line)

def checkFuelCost(crabs, target):
    cost = 0
    for crab in crabs:
        curr = abs(crab - target)
        cost += curr
        #print('The cost for ', crab, ' is ', curr)
    return cost

def tryDifferentTargets(crabs):
    targets = range(max(crabs))
    minCost = Inf
    for target in targets:
        cost = checkFuelCost(crabs, target)
        if cost < minCost:
            minCost = cost
    return minCost


cost = tryDifferentTargets(crabs)

print('The total cost is ', cost)