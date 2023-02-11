#	*************
#	** Z-Tests **
#	*************
#
# - Used with Numerical Features
#
# - P-Value < 5%: Rejects Null Hypothesis
#
# - P-Value > 5%: Accepts Null Hypothesis
#
#
# - T-Test VS Z-Test: use Z-Test when the sample size is more
# than 30.
#
# - ANOVA VS T/Z-Test: use ANOVA when you are comparing 3 or more
# groups.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest as ztest



# ---- One Sample Z-Test ----
#
# - Checks out if the sample's mean differs from the population's mean
#
# - Null Hypothesis: their means does not differ so much, so, both
# datas have the same distribution
#
# - Example: you could use this test to check whether the Demon Slayer
# manga got more solds than the others mangas in general. If that is so,
# the Null Hypothesis is reject and you can explore to find out why
# it happened
population_ages1 = stats.poisson.rvs(loc=18, mu=35, size=150000)
population_ages2 = stats.poisson.rvs(loc=18, mu=10, size=100000)
population_ages = np.concatenate((population_ages1, population_ages2))

sample_ages1 = stats.poisson.rvs(loc=18, mu=30, size=30)
sample_ages2 = stats.poisson.rvs(loc=18, mu=10, size=20)
sample_ages = np.concatenate((sample_ages1, sample_ages2))

ztest(
	sample_ages                # sample data
	, value=population.mean()  # population's mean
)



# ---- Two Sample Z-Test ----
#
# - Checks out whether two independents numerical features have
# correlation
#
# - Null Hypothesis: the two features does not have correlation
#
# - Example: you could use this test to check whether the public
# that reads mangas tells something about the number of volumes
# of the mangas
public_ages    = stats.poisson.rvs(loc=18, mu=13, size=500)
mangas_volumes = stats.poisson.rvs(loc=18, mu=35, size=500)

stats.ttest_ind(
	a=public_ages       # sample 1
	, b=mangas_volumes  # sample 2
	, equal_var=False   # assumes samples have the same variance
)

ztest(
	public_ages       # sample 1
	, manges_volumes  # sample 2
	, value=0         # assumes samples have the same variance (0 False, 1 True)
)


# Other Example
group1 = df[df['categorical_col'] == 'group1']['numerical_col']
group2 = df[df['categorical_col'] == 'group2']['numerical_col']

ztest(group1, group2, value=0)


# ---- Paired Z-Test ----
#
# - There is not a Paired Z-Test; uses Paired T-Test instead
#
# - Checks out whether two dependents numerical features have
# correlation. Like to analyse samples of the same groups at
# different points in time
#
# - Null Hypothesis: the two features does not have correlation
#
# - Example: a hospital might want to test whether a weight-loss
# drug works by checking the weights of the same group patients
# before and after treatment.
#
# - Example 2: a company might want to test whether their monthly
# incomes rates by checking the sells of the same products before
# and after using a recomendation system model with Machine Learning
before = stats.norm.rvs(scale=30, loc=250, size=100)
after = before + stats.norm.rvs(scale=5, loc=-1.25, size=100)

sells_df = pd.DataFrame({
	'sells_rate_before': before
	, 'sells_rate-after': after
	, 'sells_rate_change': after-before
})

stats.ttes_rel(
	a=before   # sample 1
	, b=after  # sample 2
)



# ---- Error Types ----
#
# - Type I (False Positives): the Null Hypothesis is rejected when
# it is true in reality
#
# - Type II (False Negatives): the Null Hypothesis is accepted when
# it is false in reality