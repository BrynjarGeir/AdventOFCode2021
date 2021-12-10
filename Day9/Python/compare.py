with open('setPart1') as f:
    p1 = f.readline()

with open('checkSet') as f:
    cS = f.readline()

p1 = list(eval(p1))
for idx, p in enumerate(p1):
    p1[idx] = tuple(reversed(p))

p1 = set(p1)
cS = set(eval(cS))

#print(p1.intersection(cS))
print(p1 - cS)
print(cS - p1)