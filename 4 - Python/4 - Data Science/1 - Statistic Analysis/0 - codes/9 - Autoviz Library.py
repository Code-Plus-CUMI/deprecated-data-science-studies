"""
3 - Autoviz

- Description:
	Library to display plots about the dataset. It can be used over
the Data Exploration section

- Install:
	!pip install autoviz

- Documentation:
	https://openbase.com/python/autoviz/documentation
"""

from autoviz.AutoViz_Class import AutoViz_Class
import pandas as pd
import matplotlib.pyplot as plt

df = AutoViz_Class()
filename = 'any_file.csv'
sep = ','

graph = df.AutoViz(
	filename
	, sep=','
	, depVar=''
	, dfte=None
	, header=0
	, verbose=0
	, lowess=False
	, chart_format='svg'
	, max_rows_analyzed=150000
	, max_cols_analyzed=30
)