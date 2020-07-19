#!/usr/bin/python3

import battingAverage
import consecutiveHits

def both(odds1, odds2):
    return (odds1 * odds2)

seasonLength = [60, 162]
battingAvg = .350 

battingOdds = []
battingOdds.append(battingAverage.battingFourHundred(battingAvg, seasonLength[0]))
battingOdds.append(battingAverage.battingFourHundred(battingAvg, seasonLength[1]))

print("Odds of batting a .400 in a short season:", battingOdds[0])
print("Odds of batting .400 in a regular season:", battingOdds[1])

#print(consecutiveHits.hitStreak(battingAvg, seasonLength[0]))
#print(consecutiveHits.hitStreak(battingAvg, seasonLength[1]))
streakChance = []
streakChance.append(consecutiveHits.markovHitStreak(battingAvg, seasonLength[0]))
streakChance.append(consecutiveHits.markovHitStreak(battingAvg, seasonLength[1]))
#this one is for both
streakChance.append(consecutiveHits.markovHitStreak(.400, seasonLength[0]))

print("Odds of matching or breaking the 56 game streak in a short season:", streakChance[0])
print("Odds of matching or breaking the 56 game streak in a regular season:", streakChance[1])

print("Chances of both batting .400 and having a 56 or longer streak in a short season:", battingOdds[0] * streakChance[2])
