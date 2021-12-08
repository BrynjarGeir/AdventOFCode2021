txt = 'example'
with open(txt) as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())

prev = None
idx = 0
count = 0
while idx < len(lines) - 3:
    if prev == None:
        prev = sum(lines[idx:idx+3])
    else:
        tmp = sum(lines[idx+1:idx+4])
        if tmp > prev:
            count += 1
        prev = tmp
        idx += 1


print(count)