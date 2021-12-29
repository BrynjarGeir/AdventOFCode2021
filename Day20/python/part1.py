from pprint import pprint as pretty
from operator import itemgetter as ig
import sys
inp = input('Data source? ')
with open('../data/'+inp) as f:
    data = f.readlines()
    data = [d.strip() for d in data]
    enhanceAlgo = data[0]
    imageMap = data[2:]
# Just instead of having a line with .# I have a dict with idx and .# just seems to make more sense
def fromLineToDictAlgo(enhanceAlgo):
    algo = {}
    for i,v in enumerate(enhanceAlgo): algo[i] = v
    return algo
# I think it makes more sense to just keep track of all the points that are # rather than have a total map
# So from the imageMap I am going to create a set of the points that are # and every point that isn't in that
# Set will just be . Like if it isn't in the set then it will just be .
def fromImageMapToSet(imageMap):
    imageSet = set()
    for idx, value in enumerate(imageMap):
        for i,v in enumerate(value):
            if v == '#' and (i, idx) not in imageSet: imageSet.add((i, idx))
    return imageSet
if enhanceAlgo[0] == enhanceAlgo[-1] == '#': print('Infinity'); sys.exit()
enhanceAlgo = fromLineToDictAlgo(enhanceAlgo)
imageSet = fromImageMapToSet(imageMap)
# Now let's try to find all the neighbors for some point in the image set and any point that is within a dist of 1 from a #
# This is because if all 9 points are . then we get . and nothing changes (even if 1 is # then nothing would change put whatever)
def boundaryPoints(imageSet):
    maxX = max(imageSet, key=ig(0))[0]; maxY = max(imageSet, key=ig(1))[1]
    minX = min(imageSet, key=ig(0))[0]; minY = min(imageSet, key=ig(1))[1]
    return minX-1, maxX+1, minY-1, maxY+1
# This one is just a helper funuction for the one below
def getCurrentImage(point, imageSet, bPoints, infinite_bit):
    xN, xX, yN, yX = bPoints; x,y = point
    index = 0
    for dy in range(y - 1, y + 2):
        for dx in range(x - 1, x + 2):
            index = index << 1 | (
                int((dx, dy) in imageSet)
                if (xN < dx < xX and yN < dy < yX)
                else infinite_bit
            )
    return index

# After we have gotten the current boundary we should look at something like traversing every point in that boundary and if that point
# is at the boundary then we just know that the points outside the area are . or 0. But only points within these boundary points can be 
# anything other than . We calculate the new values for any point can be affected by # and after we calculate all the new points that are
# # then we update the original set. We need two different functions I think based on the first element in the algo (.#)
# This one deals with the situation if the algo starts with # I'm still assuming that if it starts with # it ends with . (which with my input is true)
# Just need the one, used Bruception on github to help me: Thanks Bruce!
def calculateAlgoIndex(bPoints, imageSet, enhanceAlgo, infinite_bit):
    xN, xX, yN, yX = bPoints
    aImages = set()
    for x in range(xN, xX+1):
        for y in range(yN, yX+1):
            currImage = getCurrentImage((x,y), imageSet, bPoints, infinite_bit)
            newValue = enhanceAlgo[currImage]
            if newValue == '#': aImages.add((x,y))
    return aImages
# So now in the solution we are asked to calulate the new image twice or rather apply the algorithm twice so lets create a function that 
# Calculates the new image n times and returns the imageSet, that is the points that are not . The answer for part 1 only relies on how many points
# are lighted (#) so we just need the length of the set
def calcAlgoIndexes(imageSet, enhanceAlgo, iterations):
    for i in range(iterations):
            bPoints = boundaryPoints(imageSet); infinite_bit =  i & 1 & int(enhanceAlgo[0] == '#')
            imageSet = calculateAlgoIndex(bPoints, imageSet, enhanceAlgo, infinite_bit)
    return imageSet
# I get the right answer for the example but a little to high for the input. So what I want to do now is to create a map that shows the imageSet
# Like in the advent of code site and compare them together. It wont be too larg so it should be fine. Probably going to use numpy
# I know what I was doing wrong. I was trying to update the previous set but I should just create a new one and override the original ones

iterations = int(input('How many enhancements? '))
imageSet = calcAlgoIndexes(imageSet, enhanceAlgo, iterations)
pretty(len(imageSet))
x1, x2, y1, y2 = boundaryPoints(imageSet)
