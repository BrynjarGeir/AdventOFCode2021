target = open('../data/input').read().split(': ')[1].split(', ')

xTarget = target[0]; yTarget = target[1]

xTarget = xTarget.split('=')[1].split('..'); yTarget = yTarget.split('=')[1].split('..')

xTarget = [int(x) for x in xTarget]; yTarget = [int(y) for y in yTarget]

n = -yTarget[0]-1

answer = int(n*(n+1)/2)

print('The fucking incredible easy answer to part 1 after I spent a day trying to figure it out is',answer)