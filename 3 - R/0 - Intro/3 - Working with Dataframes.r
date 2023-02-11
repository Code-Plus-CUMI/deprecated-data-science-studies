#		************************
#		* Dataframes - Working *
#		************************
#

# ---- GETTING DATASETS ----
df1 <- read.csv('my_file.csv') # reading a csv file
df2 <- mtcars # accessing a built-in dataset from R

# ---- STATS INFO ----
df_summary <- summary(df2)
df_sd <- sd(df2)
df_mean <- mean(df2)
df_median <- median(df2)
df_hp_sum <- sum(df2$hp)
df_correlation <- round(corr(df2), 2)

# ---- FILTERING ----
filter_hp_greather_than_5 <- df2[df2$hp > 5, ]

# ---- GROUPING ----
#
# - first parameter: the column/feature that will be grouped
# - second paremeter: the column/feature that will group the data
# - third parameter: the function that we will apply to the first parameter

# Returns an object that can be converted to a list
hp_grouped_by_am_calculating_mean <- by(df2$hp, df2$am, mean)

# Returns a matrice
hp_grouped_by_am_calculating_mean <- tapply(df2$hp, df2$am, mean)