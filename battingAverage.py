#!/usr/bin/python3

import math

def battingFourHundred(realAvg, seasonLength):
    '''
    60 games, 4 at-bats each
    realAvg chance of a hit each at-bat
    looking for hits >= (.4 * (60 * 4) )
    math.factorial didn't like X being a float, had to round and cast
    ((N!) / (N - X)! * (X!)) * p**X * (1 - p)**(N - X)
    '''
    total = 0.0

    for i in range(400, 1001):
        n = seasonLength * 4
        X = int(round(n * (i / 1000), 0))
        p = realAvg
        q = (1 - realAvg)
        #part 1
        result = (math.factorial(n) / (math.factorial(n - X) * math.factorial(X)))
        #part 2
        result *= p**X
        #part 3
        result *= q**(n - X)
        total += result
    return total


