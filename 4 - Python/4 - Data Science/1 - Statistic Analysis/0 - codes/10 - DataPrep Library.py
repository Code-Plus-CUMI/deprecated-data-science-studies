# pip install dataprep
from dataprep.eda import create_report
from dataprep.eda import plot
from dataprep.eda import plot_correlation
from dataprep.eda import plot_missing

# Full Report
create_report(df)

# Plots
plot(df)

# Correlations
plot_correlation(df)

# Missing Values
plot_missing(df)