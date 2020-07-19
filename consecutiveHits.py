#!/usr/bin/python3

import math
import numpy as np
#LINEAR ALGEBRA -- MARKOV CHAIN

def markovHitStreak(battingAvg, seasonLength):
    streak = 57#the streak is 56, need one more row for matrix
    M = np.zeros((streak, streak))
    M[-1, -1] = 1
    perGameHit = perGame(battingAvg)
    print("per game hit odds =", perGameHit)
    M[:-1, 0] = (1 -perGameHit)
    for i in range(streak-1):
        M[i, i+1] = perGameHit
    result = np.linalg.matrix_power(M, seasonLength)

    return result[0, -1]

def perGame(battingAvg):
    total = 0.0
    for i in range(1, 5):
        result = (math.factorial(4)/(math.factorial(4 - i) * math.factorial(i)))
        result *= battingAvg**i
        result *= (1 - battingAvg)**(4 - i)
        total += result
        print("Chances of ", i, "Hits:", result)
    return total
