#	*******************************
#	** Probability Distributions **
#	*******************************
#
# 	Probability Distributions is used to check out the values'
# distributions of a random variable, turning easy to guess
# which values are more likely to expect than others.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


# ---- Uniform Distribution ----
#
# - The values are equally distributed. So all of them are more likely
# to be expected.
#
# - Its distribution plot is flat!
#
# - Methods:
#		\ stats.uniform.rvs: generates a uniform number array
#		\ stats.uniform.cdf: calcs the probability distribution of 
# a given quantile (x)
#		\ stats.uniform.ppf: calcs the maximum value of a given probability
# distribution (x)
uniform_data = stats.uniform.rvs(
	size=10000  # generates 10000 random, uniform numbers
	, loc=0     # being 0 the min value
	, scale=10  # and 10 the max one
)

stats.uniform.cdf(
	x=2.5        # quantile (25th quantile)
	, loc=0      # minimum value 
	, scale=10   # maximum value
)

stats.uniform.ppf(
	x=0.4        # probability
	, loc=0      # minimum value
	, scale=10   # maximum value
)




# ---- Normal Distribution ----
#
# - The values are around the mean/median
#
# - It is like a parabola, it is a simetric Bell Shape Curve
#
# - Methods:
#	\ stats.norm.cdf: calcs the probability distribution of 
# a given quantile (x)
#   \ stats.norm.ppf: calcs the maximum value of a given probability
# distribution (x)

stats.norm.cdf(q=0.025) # find the quantile for the 2.5% cutoff
stats.norm.cdf(q=0.9975) # find the quantile for the 99.75% cutoff

stats.norm.ppf(x=3)  # how much data is above 3 std over the mean
stats.norm.ppf(x=-3) # how much data is bellow 3 std under the mean



# ---- Binomial Distribution ----
#
# - It's like the Normal Distribution, but with just two parameters:
# the success and the fail
flip_coin = stats.binom.rvs(
	n=10         # number of trials
	, p=0.5      # probability
	, size=10000 # number of experiments
)



# ---- Geometric and Exponencial Distribution ----
#
# - The distribution is skewed to the right or to the left
#
# - Methods:
#	\ stats.geom.rvs: calcs the probability to get x successes in a row
stats.geom.rvs(
	size=10000 # number of experiments
	, p=0.5    # with success probability of 50%
)