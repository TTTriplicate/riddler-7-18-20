#!/usr/bin/python3

import math
import numpy as np
#LINEAR ALGEBRA -- MARKOV CHAIN

def markovHitStreak(battingAvg, seasonLength):
    M = np.zeros((56, 56))
    print(M.shape)

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
