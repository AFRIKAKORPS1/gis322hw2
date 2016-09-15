"""
Author: Trevor Walker
Work: Assignment 2
date: 9/14/2016
"""
import random
import math
import itertools
import scipy
from scipy import spatial

count = 1  #count for basic loop control
pairs = []
finalPairs = []  #lists to store random numbers and pairs

#while loop to create random numbers, and then form pairs stored into proper list
while count <= 4:
    points1 = random.randint(-180, 180)
    points2 = random.randint(-90, 90)
    pairs = points1, points2
    finalPairs.append(pairs)
    count += 1

#euclidean formula for distance, used in min_pair to find least distance
def distance(points):
        p0, p1 = points
        return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

#test function to determine minimum distance
min_pair = min(itertools.combinations(finalPairs, 2), key=distance)
min_distance = distance(min_pair)

#initial class declaration
class PointCalc:
    def __init__(self):
       print '\nX and Y coordinate pairs: '
       print finalPairs

    def allCoords(self, x):
        print '\nThe shortest distance between coordinate pairs is: '
        listDist = scipy.spatial.distance.pdist(finalPairs, 'euclidean') #scipy method to find calculated distance
        print listDist

        print '\nThe smallest coordinate is: '
        print min(finalPairs)

        print '\nAnd the smallest distance is: '
        print min_distance

#test
test = PointCalc()
test.allCoords(finalPairs)
print test




