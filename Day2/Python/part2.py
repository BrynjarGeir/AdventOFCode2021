txt = 'input'
with open(txt) as f:
    lines = f.readlines()
    aim = 0
    depth = 0
    horPos = 0
    for line in lines:
        line = line.strip()
        line = line.split()
        line[1] = int(line[1])
        if line[0] == 'forward':
            horPos += line[1]
            depth += aim * line[1]
        elif line[0] == 'down':
            aim += line[1]
        elif line[0] == 'up':
            aim -= line[1]
        else:
            print('Something went wrong!')


print(aim)
print(depth)
print(horPos)

mult = horPos * depth

print('Answer is: ',mult)
