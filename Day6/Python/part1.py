import numpy as np

txt = 'input'
with open(txt) as f:
    line = f.readline()
    line = line.split(',')
    for idx, item in enumerate(line):
        line[idx] = int(item)

fishes = np.array(line)

def oneDay(fishes):
    tmp = np.array([], dtype=int)
    for idx, val in enumerate(fishes):
        if val == 0:
            fishes[idx] = 6
            tmp = np.append(tmp, 8)
        else:
            fishes[idx] -= 1
    fishes = np.append(fishes,tmp)
    return fishes

def allDays(fishes, days):
    print('Initital state ',fishes)
    for _ in range(days):
        fishes = oneDay(fishes)
        #print('On day ',day+1,' fishes are ',fishes)
    return fishes

fishes = allDays(fishes, 256)

print('In the end there are ', len(fishes), ' fishes')
