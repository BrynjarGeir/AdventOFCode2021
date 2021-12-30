from functools import lru_cache as lcache
from itertools import product

inp = input('What data set do you want? ')
data = open("../data/"+inp).read().strip().split("\n")
pos1 = int(data[0].split(': ')[1]); pos2 = int(data[1].split(': ')[1])
score1 = 0; score2 = 0
comb = ((1,2,3), (1,2,3), (1,2,3))

# part 2
@lcache(maxsize=None)
def findTotalNumberOfWorlds(pos1, score1, pos2, score2):
    w1 = w2 = 0
    for d1, d2, d3 in product((1,2,3), (1,2,3), (1,2,3)):
        p1_copy = (pos1 + d1 + d2 + d3) % 10 if (pos1 + d1 + d2 + d3) % 10 else 10
        s1_copy = score1 + p1_copy
        if s1_copy >= 21:
            w1 += 1
        else:
            w2_copy, w1_copy = findTotalNumberOfWorlds(pos2, score2, p1_copy, s1_copy)
            w1 += w1_copy
            w2 += w2_copy
    return w1, w2

print("Part 2:" ,max(findTotalNumberOfWorlds(pos1, score1, pos2, score2)))