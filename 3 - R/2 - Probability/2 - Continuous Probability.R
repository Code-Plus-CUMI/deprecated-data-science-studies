library(tidyverse)
library(dslabs)
data(heights)

x <- heights$height

# 0) Cumulative Distribution Function (CDF)
#
# It's the probability of a value greather than
# or equals OR smaller than or equals a certain
# value
#
# 'Pnorm' calculates the Theorical CDF, which means
# the CDF is calculated considering that the
# distribution is a normal one (Gaussian-Distribution)
mean(x <= 70.5)

pnorm(70.5, mean(x), sd(x))

# Also, we can generate random normal distributed
# datas using the 'rnorm' function. For instance:
y <- rnorm(length(x), mean(x), sd(x))
ggplot(aes(y)) + geom_histogram()

# 1) Density Distribution #
#
# It calculates the 'Gaussian-Distribution Plot'
# using the y-axis as probabilities to each possible
# value
dnorm(x)

ggplot(aes(x, dnorm(x))) + geom_line()