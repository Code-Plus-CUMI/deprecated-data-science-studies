library(Lahman) # baseball dataset (Teams)
library(tidyverse) # %>%, %in% operators and mutate/filter/select functions
library(ggplot2) # plots and data visualization!!

# 0 - Scatter Plots #
#
# We use scatter plots when we're willing to check
# out the relatioonship between two variables.
#
# In this example, we're checking out the relationship
# between 'Wins Per Game' with 'Errors Per Game'.
#
# - Spoiler: if you plot the relationship, you'll
# realize that as many errors a team commit, less
# will be the chances of winnning the match
data <- Teams %>% filter(yearID %in% 1961:2001) %>%
                  mutate(W_per_game=W/G, E_per_game=E/G) %>%
                  ggplot(aes(W_per_game, E_per_game)) +
                  geom_point(alpha=0.5)

# 1 - Correlation Coefficient #
#
# The Correlation Coefficient is an efficient variable
# to shows the relationship between two variables.
#
# It varies from -1 to 1 being:
#
#	\ close to -1: negative relationship (X increases and y decreases)
#	\ close to 1: positive relationship (x increases and y increases)
#	\ close to 0: no relationship at all
corr_W_E_per_game <- data %>% summarize(cor(W_per_game, E_per_game))

# 2 - Slope and Y-Intercept #
#
# The Linear Regression equation is:
#       y = m * x + b
#
# \ y >> result
# \ m >> slope
# \ x >> variable
# \ b >> y-intercept
#
# The 'slope' is the regreession's step, that is,
# how many values the y-axis increases/decreases
# for each value of x-axis. While the 'y-intercept'
# is the y value when x == 0
#
#   slope        =  cor(x,y) * sd(y) / sd(x)
#   y-intercept  =  slope * mean(x) - mean(y)
slope        <- cor(W_per_game, E_per_game) * sd(E_per_game) / sd(W_per_game)
y_intercept  <- slope * mean(W_per_game) - mean(E_per_game)

# 3 - Stratification #
#
# Sometimes, just using the Correlation Coefficient
# with the whole dataset is not approprieted when
# the values are not 'equally distributed'. Which
# means we gotta split the values into groups and
# analyse their Correlation Coefficients separately.
#
# Stratification is applied when the datas should
# be split in different groups. These groups are
# not explicit in the dataset, so you gotta study
# the dataset and be able to find them (or you can
# just apply Non-Supervisioned MMachine Learn
# Algorithm like K-Means)
#
# Often, the groups will be something like this:
# day/night, weekday/weekend, female/male,
# department_1/department_2/department_3, and so on
#
# To do this (in Python), we have two options:
#
# 1) Stratifying The Target (y):
#
#	train_test_split(X, y, train_size=0.80
#                        , test_size=0.20
#                        , random_state=0
#                        , stratify=y)
#
# 2) Stratifying the Features (X):
#
#	Create new columns accordingly to the groups:
#
#	groups = []
#	
#	for row in dataset:
#		if row['column']   <= 5:  groups.append(1)
#		elif row['column'] <= 10: groups.append(2)
#		else:                     groups.append(3)
#
#	dataset['Groups'] = groups
#
# After that, we can calculate the Correlation
# Coefficients as well as plot the Scatter Plot
# of each group
#
#	df.groupby('Groups')[['variable_1','variable_2']].corr()
#												     .unstack()
#													 .iloc[:,1]