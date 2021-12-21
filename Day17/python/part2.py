########## Imports and other setup ############

########## Preparing data ##############

target = open('../data/input').read().split(': ')[1].split(', ')

xTarget = target[0]; yTarget = target[1]

xTarget = xTarget.split('=')[1].split('..'); yTarget = yTarget.split('=')[1].split('..')

xTarget = [int(x) for x in xTarget]; yTarget = [int(y) for y in yTarget]

position = {'x':0, 'y':0}
velocity = {'x':0, 'y':0}

########### Functions that update the positions and check if a certain position matches target area ############

def applyVelocity(): position['x'] += velocity['x']; position['y'] += velocity['y']

def applyDrag(): 
    if velocity['x'] > 0: velocity['x'] -= 1
    elif velocity['x'] < 0: velocity['x'] += 1

def applyGravity(): velocity['y'] -= 1

def matchesTargetArea():
    if xTarget[0] <= position['x'] <= xTarget[1] and yTarget[0] <= position['y'] <= yTarget[1]: return True
    return False

def neverGonnaMatchArea():
    if velocity['x'] == 0 and position['y'] < yTarget[0] and velocity['y'] < 0:  return True
    return False

################### Actually trying to solve the thing ###########################

def checkIfVelWorks(vel):
    velocity['x'] = vel[0]; velocity['y'] = vel[1]
    while True:
        if matchesTargetArea(): velocity['x'] = 0; velocity['y'] = 0; position['x'] = 0; position['y'] = 0; return vel, True
        elif neverGonnaMatchArea(): velocity['x'] = 0; velocity['y'] = 0; position['x'] = 0; position['y'] = 0; return vel, False
        applyVelocity(); applyDrag(); applyGravity()

def checkForRangesOfVels():
    doVelWork = []
    for y in range(-400,400):
        for x in range(1,400):
            currVel, b = checkIfVelWorks((x,y))
            if b: doVelWork.append(currVel)
    return doVelWork

velsWork = checkForRangesOfVels()

print(len(velsWork))