###FiveThirtyEight Riddler 07-18-2020

#Chances of batting .400 in a short season when actually batting .350

For this part I used a binomial distribution. I ran a loop, and returned the summation of the chances of all possible batting averages from .400 to 1.000, only out to three decimal places.

#Chances of beating Lou Gehrig's hit streak

For this part, I started by trying to use a binomial distribution, and quickly realizing that was wrong.  From there I did some research and settled on a Markov Chain, using NumPy to model it with a matrix.

Essentially, I made a diagonalized matrix representing the possible outcomes at each stage of the hit-streak, and raised it to the (Number of games) power to represent that many possible games.  I calculated the per-game hit chance using another binomial ditribution.

#Chance of both

Because batting .400 would make the streak more likely, I recalculated the chances of the streak based on that batting average.  Then I multiplied the chances of batting .400 or better by the chances of getting the streak with an average of .400; trying to get the chances at higher batting averages would almost certainly bias my answer as too likely.
