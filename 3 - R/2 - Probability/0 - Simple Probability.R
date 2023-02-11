# 0 - Simple Probability #
beads <- rep(c('red', 'blue'), times=(2,3)) # red, red, blue, blue, blue
sample(beads, 1) # red or blue

repetitions <- 10000
events <- replicate(repetitions, sample(beads, 1))

events_tab <- table(events)
tab # returns the number of times each value was picked
prop.table(tab) # returns the pick's %

# One thing to have in mind is that the 'sample'
# function is 'Without Replacement' by default.
# If you wanna use 'With Replacement', set the
# 'replace' argument as TRUE
sample(beads, 1, replace=True)

# 1) Assets

# Seed: has the same function in Python
# (generate the same result of random generated
# numbers)
set.seed(2000)

# Mean: in probability, you can calculate the odds
# of an event like this
beads <- rep(c('red', 'blue'), times=(2,3))
beads # red, red, blue, blue, blue

mean(beads=='blue') # 0.6 (60%)

# 2) Probability Distribution
#
# It's the probability of each possible outcome.
mean(beads=='blue') # 0.6 (60%)
mean(beads=='red') # 0.4 (40%)

# 3) Rules: 'AND', 'OR'
#
# And: multiply *
# P(A and B) = P(A) * P(B)
blue_and_red <- mean(beads=='blue') * mean(beads=='red')

# Or (independent): sum +
# P(A or B) = P(A) + P(B)
blue_or_red <- mean(beads=='blue') + mean(beads=='red')

# Or (dependent): sum +
# P(A or B) = P(A) + P(B) - P(A and B)
blue_or_red <- mean(beads=='blue') + mean(beads=='red') - blue_and_red