from collections import defaultdict
from functools import reduce

with open("input") as f:
    mat = [[int(n) for n in row.strip()] for row in f.read().strip().splitlines()]

rows, cols = len(mat), len(mat[0])
coords = defaultdict(lambda:10, {(x, y): mat[y][x] for x in range(cols) for y in range(rows)})

d = ((0, -1), (0, 1), (1, 0), (-1, 0))

low = set()

for y in range(rows):
    for x in range(cols):
        for dx, dy in d:
            if coords[(x, y)] >= coords[(x+dx, y+dy)]:
                break
            if dx == -1:
                low.add((x, y))

print(low)
print("Answer 1:", sum([coords[(x, y)] + 1 for x, y in low]))