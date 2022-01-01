
from functools import reduce
from operator import mul
from math import inf
import re

blocks = list()
for line in open("../data/input"):
    parts = line.strip().split(" ", 1)

    # parse new block
    new = dict()
    for dimension in parts[1].split(","):
        d, start, end = re.fullmatch(r"(.*)=([-+]?\d+(?:\.\d+)?)\.\.([-+]?\d+(?:\.\d+)?)", dimension).groups()
        new[d] = (float(start), float(end) + 1)

    # cut old blocks
    new_blocks = list()
    for old in blocks:
        if any(d in old and (old[d][1] <= new[d][0] or new[d][1] <= old[d][0]) for d in new):
            # disjoint
            new_blocks.append(old)
        else:
            for d in new:
                if d not in old:
                    new_blocks.append({**old, d: (-inf, new[d][0])})
                    new_blocks.append({**old, d: (new[d][1], inf)})
                    old[d] = (new[d][0], new[d][1])
                elif old[d][0] < new[d][0] and new[d][1] < old[d][1]:
                    new_blocks.append({**old, d: (old[d][0], new[d][0])})
                    new_blocks.append({**old, d: (new[d][1], old[d][1])})
                    old[d] = (new[d][0], new[d][1])
                elif old[d][0] < new[d][0] <= old[d][1]:
                    new_blocks.append({**old, d: (old[d][0], new[d][0])})
                    old[d] = (new[d][0], old[d][1])
                elif old[d][0] <= new[d][1] < old[d][1]:
                    new_blocks.append({**old, d: (new[d][1], old[d][1])})
                    old[d] = (old[d][0], new[d][1])
    blocks = new_blocks

    # add new block
    if parts[0] == "on":
        blocks.append(new)
    else:
        assert parts[0] == "off"


print(sum(reduce(mul, (end - start for start, end in block.values())) for block in blocks))