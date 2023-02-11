#	**********************
#	** Frequence Tables **
#	**********************
import numpy as np
import pandas as pd



# ---- One-Way/Dimensional Frequence Table ----

# Simple Frequencies
freq = pd.crosstab(
	index=df['Categorical Feature']
	, columns='count'
)
freq

# Proportions Frequencies (%)
freq / freq.sum()

# Other way to do both things
df['Categorical Feature'].value_counts()
df['Categorical Feature'].value_counts() / df['Categorical Feature'].sum()



# ---- Two-Way/Dimensional Frequence Table ----
# - It's useful to explore relationship between variables

# Simple Frequencies (Without Margin Counts)
freq = pd.crosstab(
	index=df['Categorical Feature 1']
	, columns=df['Categorical Feature 2']
)

freq.columns = ['col1', 'col2', 'col3'] # cat 2 values
freq.index = ['index1', 'index2']       # cat 1 values

freq

# Simple Frequencies (With Margin Counts)
freq = pd.crosstab(
	index=df['Categorical Feature 1']
	, columns=df['Categorical Feature 2']
	, margins=True
)

# Proportions Frequencies (%) - Margin Counts are needed to be included

# - Proportion in General
freq / freq.loc['coltotal', 'rowtotal']

# - Proportion by Columns
freq / freq.loc['coltotal']

# - Proportion by Rows (there are two ways to do that)
freq.div(
	freq['rowtotal']
	, axis=0
)

freq.T / freq['rowtotal']



# ---- Higher-Way/Dimensional Frequencie Tables ----

# - Simple Frequence Table
freq = pd.crosstab(
	index=df['Categorical Feature 1']
	, columns=[df['Categorical Feature 2'], df['Categorical Feature 3']]
	, margins=True
)

# - Proportion by Columns
freq / freq.loc['All']