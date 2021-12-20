data = bin(int('1'+open('input').read(),16))[3:]

def part1(startBit):
    currentBit = startBit
    sumVersions = int(data[currentBit:currentBit+3], 2)
    typeID = int(data[currentBit+3:currentBit+6], 2)
    currentBit += 6

    if typeID == 4:
        while True:
            currentBit += 5
            if data[currentBit-5] == '0': break
    else:
        if data[currentBit] == '0':
            lastCurrent = currentBit + 16 + int(data[currentBit+1:currentBit+16],2)
            currentBit += 16
            while currentBit < lastCurrent:
                currentBit, version = part1(currentBit)
                sumVersions += version
        else:
            length = int(data[currentBit+1:currentBit+12],2)
            currentBit += 12
            for _ in range(length):
                currentBit, version = part1(currentBit)
                sumVersions += version
    return currentBit, sumVersions


print('The answer to part 1, the total sum of versions, is:',part1(0)[1])

import math

op = [sum, math.prod, min, max, 
    lambda ls: ls[0],
    lambda ls: 1 if ls[0] > ls[1] else 0,
    lambda ls: 1 if ls[0] < ls[1] else 0,
    lambda ls: 1 if ls[0] == ls[1] else 0]
'''
def part2(startBit):
    currentBit = startBit
    typeID = int(data[currentBit+3:currentBit+6],2)
    currentBit += 6
    if typeID == 4:
        vals = [0]
        while True:
            vals[0] = 16*vals[0] + int(data[currentBit+1:currentBit+5],2)
            currentBit += 5
            if data[currentBit-5] == '0': break
    else:
        vals = []
        if data[currentBit] == '0':
            lastBit = currentBit + 16 + int(data[currentBit+1:currentBit+16],2)
            currentBit += 1
            while currentBit < lastBit:
                currentBit, version = part2(currentBit)
                vals.append(version)
        else:
            length = int(data[currentBit+1:currentBit+12],2)
            currentBit += 12
            for _ in range(length):
                currentBit, version = part2(currentBit)
                vals.append(version)
    return currentBit, op[typeID](vals)
'''


def part2(startBit):
    currentBit= startBit # index into data
    typeID = int(data[currentBit+3:currentBit+6],2) # packet type typeID
    currentBit+= 6
    if typeID == 4: #literal value
        versions = [0]
        while True:
            versions[0] = 16*versions[0] + int(data[currentBit+1:currentBit+5],2)
            currentBit+= 5
            if data[currentBit-5] == '0': break
    else:
        versions = []
        if data[currentBit] == '0': # subpacket length in bits
            endBit= currentBit+ 16 + int(data[currentBit+1:currentBit+16],2)
            currentBit+= 16
            while currentBit< endBit:
                currentBit,version = part2(currentBit)
                versions.append(version)
        else:
            length = int(data[currentBit+1:currentBit+12],2) # number of subpackets
            currentBit+= 12
            for _ in range(length):
                currentBit,version = part2(currentBit)
                versions.append(version)

    return currentBit,op[typeID](versions)

print('The answer to part 2, the total value of the outermost packet, is', part2(0)[1])
