txt = 'input'
with open(txt) as f:
    lines = f.readlines()
    forward = 0
    down = 0
    for line in lines:
        line = line.strip()
        line = line.split()
        line[1] = int(line[1])
        if line[0] == 'forward':
            forward += line[1]
        elif line[0] == 'down':
            down += line[1]
        elif line[0] == 'up':
            down -= line[1]
        else:
            print('Something went wrong!')


print(forward)
print(down)

mult = forward * down

print(mult)