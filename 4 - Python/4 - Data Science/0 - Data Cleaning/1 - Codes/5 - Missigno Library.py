"""
1 - Missingno

- Description:
	Library to plot missing values in a dataframe. Can be used
with `df.isnull().sum()` command

- Install:
	!pip install missingno
"""

import missingno as msno
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("any_file.csv")

# Plots
msno.matrix(df)
msno.bar(df)
msno.heatmap(df)
msno.dendogram(df)

# Advanced Plots
msno.matrix(
	df
	, figsize=(25, 7)
	fontsize=30
	, sort='descending'
	, color=(0.494, 0.184, 0.556)
	, width_ratios=(10, 1)
	, inline=False
)
plt.title('Whatever Title')
plt.show()