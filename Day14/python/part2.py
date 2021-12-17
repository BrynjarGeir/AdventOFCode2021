from collections import Counter, deque

lines = open('input').readlines()
lines = [line.strip().split(' -> ') for line in lines]

template = deque(lines[0][0])
rules = {}
for line in lines[2:]:
    rules[line[0]] = line[1]

def solve(template, pairs, steps):
    for step in range(steps+1):
        if step == steps:
            letters = Counter()
            for pair in pairs:
                print(pairs[pair])
                letters[pair[0]] += pairs[pair]
            letters[template[-1]] += 1
            return max(letters.values()) - min(letters.values())
        new_pairs = Counter()
        for pair in rules:
            new_pairs[pair[0] + rules[pair]] += pairs[pair]
            new_pairs[rules[pair] + pair[1]] += pairs[pair]
        pairs = new_pairs 

steps = 40; pairs = Counter()
for i in range(len(template) - 1):
    pairs[template[i] + template[i+1]] += 1

diff = solve(template, pairs, steps)

print(diff)