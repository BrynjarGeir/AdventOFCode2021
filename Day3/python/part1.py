import numpy as np

txt = 'input'
with open(txt) as f:
    lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        tmp = []
        for item in lines[i]:
            tmp.append(int(item))
        lines[i] = tmp

arr = np.array(lines)

arr = np.transpose(arr)

gamma = []
epsilon = []

for row in arr:
    curr = np.count_nonzero(row) - len(row)/2 > 0
    if curr:
        gamma.append('1'), epsilon.append('0')
    else:
        gamma.append('0'), epsilon.append('1')

gammaI = int(''.join(gamma),2)
epsilonI = int(''.join(epsilon),2)

print('gamma: ', gammaI)
print('epsilon: ', epsilonI)

consumption = gammaI * epsilonI

print('consumption: ', consumption)