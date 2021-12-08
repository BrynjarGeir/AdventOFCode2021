txt = 'input'
with open(txt) as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())

prev = None
count = 0
while lines:
    if prev == None:
        prev = lines.pop(0)
    else:
        tmp = lines.pop(0)
        if tmp > prev:
            count += 1
        prev = tmp


print(count)