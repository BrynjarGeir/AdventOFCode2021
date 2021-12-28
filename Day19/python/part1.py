#Did not do this, this is JimCasey from reddit/github
#I will change this, I will read through it and make it my own (kinda, can't unsee this)

from pprint import pprint as pretty

with open('../data/input') as file:
    scanners = [
        [tuple(map(int, line.split(','))) for line in group.split('\n')[1:]]
        for group in file.read().strip().split('\n\n')
    ]

def distance(beaconA, beaconB):
    xA,yA,zA = beaconA
    xB,yB,zB = beaconB
    dist = ((xA-xB)**2+(yA-yB)**2+(zA-zB)**2)**0.5
    return dist

def heron(m, n, o):
  a = distance(m,n); b = distance(n,o); c = distance(o,m)
  s = (a+b+c) / 2
  a = (s*(s-a)*(s-b)*(s-c))**0.5
  return a

def findNeighbors(beacon, beacons, unique):
  neighbors = {}
  for peer in beacons:
    if peer != beacon: neighbors[distance(beacon, peer)] = peer
  distanceA, distanceB = sorted(neighbors)[0:2]
  neighborA = neighbors[distanceA]; neighborB = neighbors[distanceB]
  area = (distanceA + distanceB) * distance(neighborA, neighborB)
  unique.add(area)
  return unique

def findUniqueBeacons(scanners):
  unique = set()
  for beacons in scanners:
    for beacon in beacons:
      unique = findNeighbors(beacon, beacons, unique)
  return unique

#unique = set()
# So basically the idea here is kinda similar to mine but much simpler
# You calculate the distance between any two points or rather you calculate
# The distance to all other points for any point and then take the two closest
# So you can create a triangle. But why do they use that formula? Like why
# (distA + distB)*dist(a,b)? I mean maybe it is as good as any, the only thing
# That matters is that it creates a unique area so that any that match, well the
# Set will take care of them. But wouldn't it be nicer to use Heron, so you actually
# Make triangles? Let's do that and let's use functions. So if I make distanceA, distanceB
# The second and third shortest distances I get almost double. From 479 to 907. Why does it
# Matter what length I use? I Mean like sure it might match but why this big a difference?
# And the bigger difference I take the more I get. Is it because I only have like a set number
# Of overlap? Like if I would have a lot more overlap it wouldn't matter? Well anywho, let's use the shortest
# Also why do I have to add distanceA and distanceB? Why Can't I simply multiply them together?
# I can subtract and be fine which makes sense, but why can I not multiply? I'm gonna check what happens if I
# Use heron for the key - does not work. I don't know what is so special about this final step. What in
# (distA + distB) * dist(a,b) makes it unique I guess I will just leave it. This at least is a bit more like I
# would probably do it than just straight copy/paste but still of course is just copy/paste
#for beacons in scanners:
#  for beacon in beacons:
#    neighbors = {}
#    for peer in beacons:
#      if peer != beacon:
#        neighbors[distance(beacon, peer)] = peer
#    distanceA, distanceB = sorted(neighbors)[0:2]
#    neighborA = neighbors[distanceA]
#    neighborB = neighbors[distanceB]
#    key = (distanceA - distanceB) * distance(neighborA, neighborB)
#    unique.add(key)

unique = findUniqueBeacons(scanners)

print(len(unique))

