###FiveThirtyEight Riddler 07-18-2020

#Chances of batting .400 in a short season when actually batting .350

For this part I used a binomial distribution. I ran a loop, and returned the summation of the chances of all possible batting averages from .400 to 1.000, only out to three decimal places.

#Chances of beating Lou Gehrig's hit streak

For this part, I started by trying to use a binomial distribution, and quickly realizing that was wrong.  From there I did some research and settled on a Markov Chain, using NumPy to model it with a matrix.

Essentially, I made a diagonalized matrix representing the possible outcomes at each stage of the hit-streak, and raised it to the (Number of games) power to represent that many possible games.  I calculated the per-game hit chance using another binomial ditribution.

#Chance of both

Being two seperate events, I just multiplied them together.  I think this is wrong; having the higher batting average would make the streak more likely, for one thing, but not necessarily the inverse.  Coule fold the .400 into the markov chain and use that instead of the chance based on batting .350.
