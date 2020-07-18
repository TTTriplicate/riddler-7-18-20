#!/usr/bin/python3

import math

def hitStreak(battingAvg, seasonLength):
    '''
    take binomial distribution of getting 1 hit or more per game
    expotentiate to the the (streak) power
    odds of one in 4 with <battingAvg> chance of success per
    '''
    result = math.factorial(4)/math.factorial(3)
    result *= battingAvg
    result *= (1 - battingAvg)**3
    return result

