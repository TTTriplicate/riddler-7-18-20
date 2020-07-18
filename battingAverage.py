#!/usr/bin/python3

import math

def battingFourHundred(realAvg, seasonLength):
    '''
    60 games, 4 at-bats each
    .35 chance of a hit each at-bat
    looking for hits >= (.4 * (60 * 4) )
    '''
    n = seasonLength * 4
    X = int(round(n * .4, 10))
    p = avg
    q = (1 - avg)
    #part 1
    result = (math.factorial(n) / (math.factorial(n - X) * math.factorial(X)))
    
    #part 2
    result *= p**X

    #part 3
    result *= q**(n - X)
    return result


avg = .350

print(battingFourHundred(avg, 60))
print(battingFourHundred(avg, 162))
