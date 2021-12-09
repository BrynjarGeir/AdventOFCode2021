import numpy as np
from collections import deque

txt = 'input'
with open(txt) as f:
    line = f.readline()
    line = line.split(',')
    for idx, item in enumerate(line):
        line[idx] = int(item)

def allDays(fishes, days):
    print('Initital state ',fishes)
    fishes = deque(fishes.count(i) for i in range(9))
    for _ in range(days):
        fishes.rotate(-1)
        fishes[6] += fishes[8]
    return fishes

fishes = allDays(line, 256)

print('In the end there are ', sum(fishes), ' fishes')
