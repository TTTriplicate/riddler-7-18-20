#!/usr/bin/python3

import math
import numpy as np
#LINEAR ALGEBRA -- MARKOV CHAIN

def markovHitStreak(battingAvg, seasonLength):
    streak = 57#the streak is 56, need one more row for matrix
    M = np.zeros((streak, streak))
    M[0, -1] = 1
    perGameHit = perGame(battingAvg)
    M[:-1, 0] = perGameHit
    for i in range(streak):
        M[i, i+1] = perGameHit
    np.linalg.matrix_power(M, seasonLength)

    return M[0, -1]

def perGame(battingAvg):
    result = math.factorial(4)/math.factorial(3)
    result *= battingAvg
    result *= (1 - battingAvg)**3
    return result

def hitStreak(battingAvg, seasonLength):
    '''
    take binomial distribution of getting 1 hit or more per game
    expotentiate to the the (streak) power
    odds of one in 4 with <battingAvg> chance of success per
    '''
    oddsPerGame = perGame(battingAvg)
    hitEveryGame = oddsPerGame**seasonLength
    result = 0

    return result
