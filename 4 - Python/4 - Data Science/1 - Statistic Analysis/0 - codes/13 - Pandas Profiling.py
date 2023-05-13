#	**********************
#	** Pandas Profiling **
#	**********************
#
# 	Pandas Profiling is another super library, that Lux API, that helps you
# to analise datasets faster, effortless and with just a few lines of code.
#
# 	While Lux API is focused on Data Visualization, Pandas Profiling focuses
# on Statistical Info.
#

import pandas_profiling
import pandas as pd

df = pd.read_csv('dataset.csv')
df.profile_report()