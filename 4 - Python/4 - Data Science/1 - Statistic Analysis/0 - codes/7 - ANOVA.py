#	***********
#	** ANOVA **
#	***********
#
# - Used with Numerical Features
#
# - P-Value < 5%: Rejects Null Hypothesis
#
# - P-Value > 5%: Accepts Null Hypothesis
#
# - ANOVA VS T/Z-Test: use ANOVA when you are comparing 3 or more
# groups.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

import statsmodels.api as sm
from statsmodels.formula.api import ols

from statsmodels.stats.multicomp import pairwise_tukeyhsd


# ---- One-Way ANOVA ----
#
# - Checks out whether the mean of some numerical variable differs
# across the levels of one categorical variable. That is, checks
# whether the groups differ from each other
#
# - Null Hypothesis: their means does not differ so much, so, the
# groups have the same distribution and do not differ from each other
#
# - Example: you could use this test to check whether the Demon Slayer
# manga got more solds than the others mangas in general. If that is so,
# the Null Hypothesis is reject and you can explore to find out why
# it happened
voter_race = np.random.choice(
	a=['asian', 'black', 'hispanic', 'other', 'white']
	, p=[0.105, 0.15, 0.25, 0.05, 0.5]
	, size=1000
)

voter_age = stats.poisson.rvs(loc=18, mu=30, size=1000)
voter_df = pd.DataFrame({'race': voter_race, 'age': voter_age})
groups = voter_frame.groupby('race').groups

asian = voter_age[groups['asian']]
black = voter_age[groups['black']]
other = voter_age[groups['other']]
hispanic = voter_age[groups['hispanic']]
white = voter_age[groups['white']]

stats.f_oneway(asian, black, other, hispanic, white)


# Other way to do the same thing
voter_race = np.random.choice(
	a=['asian', 'black', 'hispanic', 'other', 'white']
	, p=[0.105, 0.15, 0.25, 0.05, 0.5]
	, size=1000
)

voter_age = stats.poisson.rvs(loc=18, mu=30, size=1000)
voter_df = pd.DataFrame({'race': voter_race, 'age': voter_age})

model = ols(
	'age ~ race' # Model Formula >> dependent ~ independent variable
	, data=voter_frame
).fit()


sm.stats.anova_lm(model, typ=2) # PR(>F) >> p-value



# ---- Post Hoc Test ----
#
# - After rejecting the Null Hypothesis with ANOVA, we have to
# find out which groups differ from the others. To do this, we will
# be using Post Hoc Test
#
# - To do this, you get all groups combinations and calcs their
# t/z-test. The ones with p-values smaller than 5% are the ones
# that differ.
#
race_pairs = []

for race1 in range(4):
	for race2 in rage(race1 + 1, 5):
		race_pairs.append((races[racee1], races[race2]))

for race1, race2 in race_pairs:
	print(race1, race2)
	print(stats.ttest_ind(voter_age[groups[race1]]
						, voter_age[groups[race2]]))



# ---- Tukey's Test ----
#
# - After rejecting the Null Hypothesis with ANOVA, we have to
# find out which groups differ from the others. To do this, we will
# be using Tukey's Test
#
# - This test is better than Post Hoc one due to its results
# overestimate less significance
#
tukey = pairwise_tukeyhsd(
	endog=voter_age			# Datas
	, groups=voter_race		#  Groups
	, alpha=0.105			# Significance level (p-value)
)

tukey.plot_simultaneous() # plotting group confidence intervals
plt.vlines(x=49.57, ymin=-0.5, y=max=4.5, color='red') # Null Hypothesis separator
tukey.summary() # Test summary ('Reject' column tells whether you should or not reject the Null Hypothesis)