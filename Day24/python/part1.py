from pprint import pprint as pretty
from collections import deque as dq
from math import floor, ceil, inf
from copy import deepcopy as dp

# My first thought is to basically have a que and then just go through them one by one.
# The real problem is trying to figure out how to select the model numbers
# One idea would be to just start from the hihgest number and then go down until you find one that
# Works but that won't work probably because it will take to long
# Next idea is to try and figure out how these things work together. Like is there a reason a number higher than
# m doesn't work? Like can I try to figure it out somehow or what should I do? Should I look at my input?
# I think I am just going to try the naive approach with like binary search. So I just have to try to find
# But maybe just to get an idea I should try to do this for like the first 1000 numbers and the last 1000 and the middle 100
# Just to get a feeling of what it would be like
inp = input('What data set do you want? ')
with open('../data/'+inp) as f:
    lines = [line.strip().split(' ') for line in f.readlines()]
    instructions = [line[0] for line in lines]
    inputs = [line[1:] for line in lines]
    toDo = dq()
    for idx in range(len(inputs)):
        toDo.append((instructions[idx], inputs[idx]))
        
def generateNumbers(section: str, r: int):
    if section == 'All': return [i for i in range(10**14, 10**15) if '0' not in str(i)]
    elif section == 'Middle':
        lower = floor((10**14 + 10**15)/2-r/2); upper = ceil((10**14 + 10**15)/2+r/2)
        return [i for i in range(lower,upper) if '0' not in str(i)]
    elif section == 'Start':
        return [i for i in range(10**14,10**14+r) if '0' not in str(i)]
    elif section == 'End':
        return [i for i in range(10**15-r,10**15) if '0' not in str(i)]
    return []

def goThroughNumbers(toDo, numbers):
    for number in reversed(numbers):
        _, _, _, z = goThroughInstructions(dp(toDo), number)
        if z != 0: return number, numbers[-1]
    return 0, numbers[-1]
def goThroughInstructions(toDo, number):
    qNum = dq(); numStr = str(number)
    for c in numStr: qNum.append(int(c))
    wxyz = {'w':0, 'x':0, 'y':0, 'z':0}
    while toDo:
        do = toDo.popleft()
        if do == 'inp':
            wxyz[do[1][0]] = qNum.popleft()
        elif do == 'add':
            wxyz[do[1][0]] = qNum

# I think the it would be best to pick the numbers smarter
# Anyway I should start by trying to go through the instructions
numbers = generateNumbers('End', 100)
pretty(toDo)

# Apparently this whole thing is pointless I can just do this in my head like I did with day23 (or online)
# You can work this out just in your head. Thanks to dphilipson for his git. So below is my input basically and
# So I need to chop this up in 14 bits (one for every input)
#deque([('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),  <--- So I need to check this line
#       ('div', ['z', '1']),   <--- and this one
#       ('add', ['x', '11']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '1']),   <--- and this one, and then these ones for everyone of these parts which there are 14 of
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),  <---
#       ('div', ['z', '1']),   <---
#       ('add', ['x', '11']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '11']),  <---
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),  <---
#       ('div', ['z', '1']),   <---
#       ('add', ['x', '14']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '1']),  <---
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '1']),
#       ('add', ['x', '11']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '11']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '26']),
#       ('add', ['x', '-8']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '2']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '26']),
#       ('add', ['x', '-5']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '9']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '1']),
#       ('add', ['x', '11']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '7']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '26']),
#       ('add', ['x', '-13']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '11']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '1']),
#       ('add', ['x', '12']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '6']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '26']),
#       ('add', ['x', '-1']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '15']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '1']),
#       ('add', ['x', '14']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '7']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '26']),
#       ('add', ['x', '-5']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '1']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '26']),
#       ('add', ['x', '-4']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '8']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y']),
#       ('inp', ['w']),
#       ('mul', ['x', '0']),
#       ('add', ['x', 'z']),
#       ('mod', ['x', '26']),
#       ('div', ['z', '26']),
#       ('add', ['x', '-8']),
#       ('eql', ['x', 'w']),
#       ('eql', ['x', '0']),
#       ('mul', ['y', '0']),
#       ('add', ['y', '25']),
#       ('mul', ['y', 'x']),
#       ('add', ['y', '1']),
#       ('mul', ['z', 'y']),
#       ('mul', ['y', '0']),
#       ('add', ['y', 'w']),
#       ('add', ['y', '6']),
#       ('mul', ['y', 'x']),
#       ('add', ['z', 'y'])])

# So my values are something like (check, offset) = 
# [(11,1), (11,11), (14,1), (11,11), (-8,2), (-5,9), (11,7), (-13,11), (12,6), (-1,15), (14,7), (-5,1), (-4,8), (-8,6)]
#
# So apparently you are supposed to translate this into something like:
# if check is positive push(input + offset), if check is negative pop input from stack, then push(push input + offset) onto the stack
# We are successfull if the stack is empty in the end. So for me this would be something like
# Push input[0] + 1
# Push input[1] + 11
# Push input[2] + 1
# Push input[3] + 11
# Pop. Must have input[4] == popped_value - 8
# Pop. Must have input[5] == popped_value - 5
# Push input[6] + 7
# Pop. Must have input[7] == popped_value - 13
# Push input[8] + 6
# Pop. Must have input[9] == popped_value - 1
# Push input[10] + 7
# Pop. Must have input[11] == popped_value - 5
# Pop. Must have input[12] == popped_value - 4
# Pop. Must have input[13] == popped_value - 8
#
# And if we play these out we should get something like
# input[4] = input[3] + 3
# input[7] = input[6] - 6
# input[9] = input[8] + 5
# input[11] = input[10] + 2
# input[12] = input[1] + 7
# input[13] = input[0] - 7
# input[5] = input[2] - 4

# This somehow should give us the answer for all the categories
# So rule 1 would, in my mind mean
# 4 could be 9 but then 3 would be 6
# 6 could be 9 but then 7 would be 3
# 9 could be 9 but 8 would be 4
# 11 could be 9 but 10 would be 7
# 12 could be 9 but then 1 would be 2
# 0 could be 9 but then 13 would be 2
# 2 could be 9 but 5 would be 5
# So the highest possible would be something like 92969593497992
# Ok so I didn't really see that but apparently that works and the number above is the right one so thanks again dphilipson

# Now for the secnod