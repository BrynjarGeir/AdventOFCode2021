import string
from collections import deque
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

txt = ['smallExample', 'mediumExample', 'largeExample', 'input']
#Setup up data
with open(txt[3]) as f:
    lines = f.readlines()
    lines = [line.strip().split('-') for line in lines]

connections = {}
for line in lines:
    connections[line[0]] = set()
    connections[line[1]] = set()

for line in lines:
    connections[line[0]].add(line[1])
    connections[line[1]].add(line[0])

keysConnections = connections.keys()
bigCave = set()
smallCave = set()
for key in keysConnections:
    if key in lowercase: smallCave.add(key)
    elif key in uppercase: bigCave.add(key)
#End of data setup

# Let's create
def trace(map, boo):
    ct = 0
    tracker = deque([('start',set(['start']), False)])
    while tracker:
        p, seen, visited = tracker.popleft()
        if p == 'end':
            ct += 1
            continue
        for c in map[p]:
            if c not in seen:
                seen_cp = set(seen)
                if c.islower():
                    seen_cp.add(c)
                tracker.append((c, seen_cp, visited))
            elif c in seen and not visited and c not in ['start', 'end'] and boo:
                tracker.append((c, seen, c))
    return ct

part2 = trace(connections, True)

print('The answer to part 2 is ', part2, '!')
