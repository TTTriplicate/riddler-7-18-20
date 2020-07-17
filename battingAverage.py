#!/usr/bin/python3

import math

def shortSeason(realAvg):
    '''
    60 games, 4 at-bats each
    .35 chance of a hit each at-bat
    looking for hits >= (.4 * (60 * 4) )
    '''
    n = float(60 * 4)
    X = n * .4
    p = avg
    q = (1 - avg)
    print(math.factorial(n))
    #part 1
    result = (math.factorial(n) / (math.factorial(n - X) * math.factorial(X)))
    return result

def normalSeason(realAvg):


    return result

avg = .350

print(shortSeason(avg))
#print(normalSeason(avg))
