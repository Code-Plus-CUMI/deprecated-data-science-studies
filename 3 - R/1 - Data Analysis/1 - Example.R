# ---- Installing and Importing Libraries and Dataset ----
install.packages('tidyverse') # set of libraries
install.packages('dplyr')     # library to tidy datasets

library('tidyverse')
library('dplyr')

DATASET_TITLE <- 'Tooth Growth Dataset'
lockBinding('DATASET_TITLE', globalenv())
data('ToothGrowth') # loading native datasets
View(ToothGrowth, DATASET_TITLE)

# ---- Filtering and Sorting ----
# - Filter all rows with 'dose == 0.5'
# - Sort these rows per 'length' in ascending order
#
# - OBS.: 'arrange()' function always sorts the dataset in ascending order
# whereas 'sort()' can do it in ascending and descending order passing the
# 'decreasing = TRUE | FALSE' parameter
filtered_df <- ToothGrowth %>%
			   filter(dose == 0.5) %>%
			   arrange(len)
View(filtered_df)

# ---- Grouping ----
# - Group all filtered datas by 'supp' feature
# - After that, calculate the 'length mean' for each group
# - If there is any 'NA/Missing Values', remove them from the analysis
# - Add a column named 'group' with 'drop' value to the groups that had
# the missing values removed
grouped_df <- filtered_df %>%
			  group_by(supp) %>%
			  summarize(mean_len = mean(len, na.rm = 'T'), .group='drop')
View(grouped_df)

# ---- Selecting Features ----
# - Select all features except 'supp'
# - Select just 'supp' feature
df_without_supp <- filtered_df %>% select(-supp) # '-' excludes the features
df_with_only_supp <- filtered_df %>% select(supp)


# ---- Bias Function ----
install.packages('SimDesign')
library('SimDesign')

actual_temp <- c(68.3, 70, 72.4, 71, 67, 70)
predicted_temp <- c(67.9, 69, 71.5, 70, 67, 69)

bias(actual_temp, predicted_temp) # Output: 0.7167 (the predictions are not accurate)