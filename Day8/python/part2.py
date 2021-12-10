import pprint

txt = 'input'
with open(txt) as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        lines[idx] = line.split(' | ')
        lines[idx][0] = lines[idx][0].split()
        lines[idx][1] = lines[idx][1].split()

lines = lines

dA = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
dU = {1:2, 4:4, 7:3, 8:7}
pos = {0:None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None}

def getLen(line):
    return [len(item) for item in line]

def decipherNumbers(line):
    numbers = {0:None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}
    lengths = [len(item) for item in line[0]]
    for key in dU:
        if dU[key] in lengths:
            numbers[key] = set(line[0][lengths.index(dU[key])])
    pos[0] = (numbers[7] - numbers[1]).pop()
    idx = [i for i,d in enumerate(lengths) if d==6]
    for i in idx:
        curr = set(line[0][i]) - numbers[7] - numbers[4]
        if len(curr) == 1:
            tmp = idx.index(i)
            idx.pop(tmp) 
            pos[3] = curr.pop()
    curr = set(line[0][idx[0]]) - numbers[7] - numbers[4]
    pos[4] = (curr - set(pos[3])).pop()
    #Should now be able to make 0,6,9
    numbers[9] = numbers[8] - set(pos[4])
    if numbers[1].issubset(set(line[0][idx[0]])):
        numbers[0] = set(line[0][idx[0]])
        numbers[6] = set(line[0][idx[1]])
    else:
        numbers[0] = set(line[0][idx[1]])
        numbers[6] = set(line[0][idx[0]])
    pos[1] = (numbers[0] - numbers[6]).pop()
    pos[2] = (numbers[1] - set(pos[1])).pop()
    pos[5] = (numbers[8] - numbers[0]).pop()
    numbers[2] = set(pos[0]+pos[1]+pos[5]+pos[4]+pos[3])
    pos[6] = (numbers[8] - numbers[2] - numbers[1]).pop()
    numbers[3] = set(pos[0]+pos[1]+pos[2]+pos[3]+pos[5])
    numbers[5] = set(pos[0]+pos[2]+pos[3]+pos[5]+pos[6])
    #All numbers should be ok
    return numbers

def decipherTarget(line, numbers):
    target = [set(item) for item in line[1]]
    keys = []
    for item in target:
        for key in numbers.keys():
            if item == numbers[key]:
                keys.append(key)
    return keys

def getCurrentSum(keys):
    val = ''
    for key in keys:
        val += str(key)
    return int(val)

def getTotalSum(lines):
    totalSum = 0
    for line in lines:
        numbers = decipherNumbers(line)
        keys = decipherTarget(line, numbers)
        totalSum += getCurrentSum(keys)
    return totalSum

print(getTotalSum(lines))
