########## Imports and other setup ############

########## Preparing data ##############

target = open('../data/example').read().split(': ')[1].split(', ')

xTarget = target[0]; yTarget = target[1]

xTarget = xTarget.split('=')[1].split('..'); yTarget = yTarget.split('=')[1].split('..')

xTarget = [int(x) for x in xTarget]; yTarget = [int(y) for y in yTarget]

position = {'x':0, 'y':0}
velocity = {'x':0, 'y':0}

########### Functions that update the positions and check if a certain position matches target area############

def applyVelocity(): position['x'] += velocity['x']; position['y'] += velocity['y']

def applyDrag(): 
    if velocity['x'] > 0: velocity['x'] -=1

def applyGravity(): velocity['y'] -= 1

def matchesTargetArea():
    if xTarget[0] <= position['x'] <= xTarget[1] and yTarget[0] <= position['y'] <= yTarget[1]: return True
    return False

def neverGonnaMatchArea():
    if velocity['x'] == xTarget[0] and position['y'] < yTarget[0] and velocity['y'] < 0:  return True
    return False

############ Actual solution ###############
## We are going to try a lot of different velocities but let's pick our values carefully
## Like we can't select an x value for velocity that is higher than the x value of target area
## We can say this because the x seeks 0, y on the other hand will just continue to get more negative
## Thus we know the initial y value can not be more negative than the target area. So some limit on y
## Also the problem is to find the highest y value. We also know that y/x is the 
## So we have at least some initial thoughts on what values we should try. Let's try them.

def doesItHitTheTarget(vel):
    velocity['x'] = vel[0]; velocity['y'] = vel[1]
    while True:
        if matchesTargetArea(): position['x'] = 0; position['y'] = 0; velocity['x'] = 0; velocity['y'] = 0; return vel, True
        elif neverGonnaMatchArea(): position['x'] = 0; position['y'] = 0; velocity['x'] = 0; velocity['y'] = 0; return vel, False
        applyVelocity(); applyDrag(); applyGravity()

def doesRangeHitTarget(x_max = 10, y_min = -10, y_max = 10):
    velsThatHitTarget = []
    for y in range(y_min, y_max):
        for x in range(1,x_max):
            vel, b = doesItHitTheTarget((x,y))
            if b: velsThatHitTarget.append(vel)
    return velsThatHitTarget

def getHighestYValue(vel):
    velocity['x'] = vel[0]; velocity['y'] = vel[1]
    while True:
        if velocity['y'] <= 0:
            x,y = position['x'], position['y']
            position['x'] = 0; position['y'] = 0; velocity['x'] = 0; velocity['y'] = 0
            return vel, (x,y)
        applyVelocity(); applyDrag(); applyGravity()
        
def getAllHighestValues(hits):
    topVelOPoint = {}
    for hit in hits:
        vel, pos = getHighestYValue(hit)
        topVelOPoint[vel] = pos
    return topVelOPoint

pointsThatHitTarget = doesRangeHitTarget(x_max=xTarget[1], y_min=yTarget[1])
allHighestValues = getAllHighestValues(pointsThatHitTarget)