txt = 'input'

with open(txt) as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        lines[idx] = line.split(' | ')
        lines[idx][0] = lines[idx][0].split()
        lines[idx][1] = lines[idx][1].split()

lines = lines

dU = {1:2, 4:4, 7:3, 8:7}

def checkUniqueOcc(dU, lines):
    count = 0
    for line in lines:
        for item in line[1]:
            if len(item) in dU.values():
                count += 1
    return count

print(checkUniqueOcc(dU, lines))