from collections import Counter, deque

lines = open('example').readlines()
lines = [line.strip().split(' -> ') for line in lines]

template = deque(lines[0][0])
rules = {}
for line in lines[2:]:
    rules[line[0]] = line[1]

steps = 15

for i in range(steps):
    tmpTemplate = deque()
    for idx, value in enumerate(template):
        if idx + 1 == len(template): break
        pair = value + template[idx+1]
        insertElement = rules[pair]
        tmpTemplate.append([idx+1, insertElement])
    for idx, item in enumerate(tmpTemplate):
        template.insert(item[0]+idx, item[1])

count = Counter(template)
most_common = count.most_common(1)[0]
least_common = count.most_common()[-1]

print('The lengt of the template is',len(template),'after',steps,'steps')
print('The most common element, and it\'s count is',most_common)
print('The least common element, and it\'s count is',least_common)
print('The difference in the count of these two is',most_common[1]-least_common[1])