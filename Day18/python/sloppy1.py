from ast import literal_eval as l_eval
from abc import ABC

lines = open('../data/finalExample').readlines()
lines = [line.strip() for line in lines]
data = [l_eval(line) for line in lines]

def countSublists(sublist): return sum(1+countSublists(i) for i in sublist if isinstance(i,list))

def countHighestLvLNestingInner(sublist):
    if type(sublist) != list: return 0
    max_lvl = 0
    for sub in sublist:
        if type(sub) == list: max_lvl = countHighestLvLNestingInner(sub)
    return max_lvl + 1        

def countHighestLvLNesting(sublist): return countHighestLvLNestingInner(sublist) - 1

def findLeftMost4NestedIndex(sublist):
    for x in range(len(sublist)):
        if type(sublist[x]) == list:
            for y in range(len(sublist[x])):
                if type(sublist[x][y]) == list:
                    for z in range(len(sublist[x][y])):
                        if type(sublist[x][y][z]) == list:
                            for w in range(len(sublist[x][y][z])):
                                if type(sublist[x][y][z][w]) == list: return [x,y,z,w], True
    return None, False

def explode(sublist):
    if countHighestLvLNesting(sublist) < 4: return
    else:
        idx, b = findLeftMost4NestedIndex(sublist)
        if not b: return
        else:
            return

def splits(sublist): return

print(countHighestLvLNesting(l_eval('[[[[[9,8],1],2],3],4]')))