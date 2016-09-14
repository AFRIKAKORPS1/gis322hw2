import random
import math
import itertools

count = 1 #count for basic loop control
pairs = []
finalPairs = [] #lists to store random numbers and pairs

#while loop to create random numbers, and then form pairs stored into proper list
while (count <= 4):
    points1 = random.randint(-180, 180)
    points2 = random.randint(-90, 90)
    pairs = points1, points2
    finalPairs.append(pairs)
    count = count + 1

print finalPairs
print len(finalPairs)

def distance(points):
    p0, p1 = points
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

min_pair = min(itertools.combinations(finalPairs, 2), key=distance)
min_distance = distance(min_pair)
print min_distance

class PointCalc():
    def __init__(self):
        pair1 = 1