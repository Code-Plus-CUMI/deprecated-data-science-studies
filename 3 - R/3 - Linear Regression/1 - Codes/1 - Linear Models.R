# 0 - Residual Sum of Squares (RSS) #
#
# The Residuals are the Linear Regression's
# errors, which mean, they are the difference
# between the 'y value' and the 'predicted y
# value'. We also call the Residuals as Errors.
#
# When working with Linear Regressions, our goal
# is to minimize the Residuals to the minimum
# possible value.
#
# However, to make the job easier, we use an
# overall value - Residual Sum of Squares, being:
#
#	 RSS = sum((y - predicted_y)^2)
#   RSS = sum((y - (y_intercept + slope * x))^2)

RSS <- sum((E_per_game - predicted_E_per_game)^2)
RSS <- sum((E_per_game - (y_intercept + slope * W_per_game))^2)

# 1 - Linear Model #
#
# The 'lm' function literally calcs the Linear
# Regression's elements, like the 'y-intercept',
# 'slope', 'residuals/errors', 'Residual Sum of
# Squares (RSS)' and so on.
#
# The parameter 'E_per_game ~ W_per_game' means
# that we're trying to predict the Errors Per Game
# using the Wins Per Game variable.
#
fit <- lm(E_per_game ~ W_per_game, data=data) # returns the y-intercept and the slope
fit$coef[1] # y-intercept
fit$coef[2] # slope

summary(fit) # returns more statistical details
predict(fit) # makes predictions with the fitted model

#######

# Exercise: calculate the linear model of
# mothers' heights by daughters' heights

library(tidyverse)
library(HistData)
data(GaltonFamilies)
set.seed(1990)

female_heights <- GaltonFamilies %>% 
				  filter(gender=='female') %>%
				  group_by(family) %>%
				  sample_n(1) %>%
				  ungroup() %>%
				  select(mother, childHeight) %>%
				  rename(daughter=childHeight)

fit <- lm(mother ~ daughter, data=female_heights)
corr <- female_heights %>%
		summary(cor(mother, daughter))

corr # 0.325
summary(fit)
'''
Call:
lm(formula = mother ~ daughter, data = female_heights)

Residuals:
   Min     1Q Median     3Q    Max 
-6.659 -1.211 -0.211  1.496  7.176 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  44.1785     4.4105   10.02  < 2e-16 ***
daughter      0.3103     0.0686    4.53  1.1e-05 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 2.17 on 174 degrees of freedom
Multiple R-squared:  0.105, Adjusted R-squared:   0.1 
F-statistic: 20.5 on 1 and 174 DF,  p-value: 1.11e-05
'''