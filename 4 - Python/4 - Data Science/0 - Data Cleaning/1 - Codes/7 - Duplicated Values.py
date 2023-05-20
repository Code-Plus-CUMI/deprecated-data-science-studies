#	************************************
#	** Dealing with Duplicated Values **
#	************************************

import pandas as pd
import numpy as np
np.random.seed(0)

df = pd.read_csv('file_path.csv')



# ---- Checking Existence of Duplicated Values ----
#
#	\ False >> there are no duplicated values
#	\ True  >> there are duplicated values
#
df.duplicated('feature').any()



# ---- Getting Duplicated Values Indexes ----
duplicated_df = df[df.duplicated('feature')]
duplicated_df