#	**********************
#	** Chi-Squared Test **
#	**********************
#
# - Used with Categorical Features
#
# - P-Value < 5%: Rejects Null Hypothesis
#
# - P-Value > 5%: Accepts Null Hypothesis
#
import numpy as np
import pandas as pd
import scipy.stats as stats



# ---- Chi-Squared Goodness-Of-Fit Test ----
#
# - Checks out if the sample's mean differs from the population's mean
#
# - It tests whether the distribution of sample categorical data
# matches an expected distribution.
#
# - Null Hypothesis: the sample's mean does not differ so much from
# the population's mean, so the both have the same distribution
#
# - Example: you could use this test to check whether the race
# demographics of members at your church or school match that of the
# entire U.S. population

population = pd.DataFrame(
	['white']  * 100000 + ['hispanic'] * 60000 + \
	['black']  *  50000 + ['asian']    * 15000 + \
	['other']  *  3000
)

sample = pd.DataFrame(
	['white']  * 50000 + ['hispanic'] * 30000  + \
	['black']  * 10000 + ['asian']    * 7000 + \
	['other']  *  500
)

population_table = population.crosstab(index=population[0], columns='count')
sample_table = population.crosstab(index=sample[0], columns='count')

population_ratios = population_table / len(population)
observed = sample_table
expected = population_rate * len(sample)

stats.chisquare(
	f_obs=observed    # array of observed counts
	, f_exp=expected  # array of expected counts
)



# ---- Chi-Squared Test of Independence ----
#
# - Checks out whether two categorical features have correlation,
# that is, whether they are dependents or independents
#
# - Null Hypothesis: the two features are independent
#
# - Example: the month you were born probably does not tell you
# anything about what browser you use, so we would expect birth month
# and browser preference to be independent

voter_race = np.random.choice(
	a=['asian', 'black', 'hispanic', 'other', 'white']
	, p=[0.105, 0.15, 0.25, 0.05, 0.5]
	, size=1000
)

voter_party = np.random.choice(
	a=['democratic', 'independent', 'republican']
	, p=[0.4, 0.2, 0.4]
	, size=1000
)

voters = pd.DataFrame({ 'race': voter_race, 'party': voter_party })



voters_tab = pd.crosstab(voters.race, voters.party, margins=True)
voters_tab.index = ['asian', 'black', 'hispanic', 'other', 'white', 'col_totals']
voters_tab.columns = ['democratic', 'independent', 'republican', 'row_totals']



observed = voters_tab.iloc[0:5, 0:3] # excluding 'row_total' and 'col_total' variables
expected = pd.DataFrame(np.outer(voters_tab['row_totals'][0:5], voters_tab.loc['col_totals'][0:3]) / 1000)
expected.index = ['asian', 'black', 'hispanic', 'other', 'white', 'col_totals']
expected.columns = ['democratic', 'independent', 'republican']



stats.chi2_contingency(observed=observed) # Output: [T-Score, p-value, calcs]



# Other Example
crosstab = pd.crosstab(df['categorical_col1'], df['categorical_col2'])
chi2, p, dof, expected = chi2_contingency(crosstab)