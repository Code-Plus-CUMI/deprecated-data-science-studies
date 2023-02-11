pd.read_csv(file_path, index_col='Column Name')

# pandas automatically treats the dates columns
# when parse-dates is True
pd.read_csv(file_path, index_col='Column Name', parse-dates=True)

#############

# LINE PLOT #

# Simple One: with all of the variables
sns.lineplot(data=datas)

# Filtered One: with just a few variables
sns.lineplot(data=datas['column1'], label="label1")
sns.lineplot(data=datas['column2'], label="label2")

# BAR PLOT #
sns.barplot(x=x_data, y=y_data)

# HEATMAP PLOT #
sns.heatmap(data=datas, annot=True)

# SCATTER PLOT #

# a simple scatter plot
sns.scatterplot(x=x_data, y=y_data)

# a scatter plot with a classification variable
sns.scatterplot(x=x_data, y=y_data, hue=classification_variable)

# a simple scatter plot with the regression line
# and it shows the error edge of the reg line
sns.regplot(x=x_data, y=y_data)

# a simple scatter plot that uses a categorical variable
# and a numberical variable, instead of two numerical ones
sns.swarmplot(x=x_data, y=y_data)

# a scatter plot with a classification variable and
# regression lines for each classification possibility,
# and more! the reg line have the error edges too!!!!
sns.lmplot(x=x_data, y=y_data, hue=classification_variable, data=dataset)


#########

# HISTOGRAM PLOT #

# a simple histogram
sns.histplot(datas)

# a simple histogram with the fitting line
sns.histplot(datas, kde=True)

# a simple histogram with a classifier variabble
sns.histplot(data=dataset, x=x_data, hue=classifier)

# a simple density plot
sns.kdeplot(data=x_data, shade=True)

# a simple density plot with a classifier
sns.kdeplot(data=dataset, x=x_data, hue=classifier, shade=True)

# a simple density plot with two variables
sns.jointplot(x=x_data, y=y_data, kind='kde')

########

# STYLES/THEMES #

# darkgrid
# whitegrid
# dark
# white (default)
# ticks
sns.set_style('dark')