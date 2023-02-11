# Tibbles
#
# They are like data frames, but:
#
# \ never change the data types
# \ never change the feature names
# \ never create new rows
# \ never create new features
#

# ---- Data Frames Functions ----
library(ggplot2)
library(tidyverse)

data(diamonds)


# ---- Cleaning Data ----
install.packages('here')
install.packages('skimr')
install.packages('janitor')
install.packages('dplyr')
install.packages('palmerpenguins')
install.packages('Tmisc')

library('here')
library('skimr')
library('janitor')
library('dplyr')
library('palmerpenguins')
library('Tmisc')

View(diamonds)
head(diamonds) # the first 6 rows
str(diamonds)  # dataset's structure
colnames(diamonds) # dataset's features
mutate(diamonds, carat_2=carat*100) # adds a new feature
rename(name_new=name) # changes a feature name
rename_with(penguins, tolower) # 'tolwer/toupper' transforms features names
clean_names(penguins) # leaves just numbers, characters and underscores on the features names
skim_without_charts(penguins) # dataset's summary
glimpse(penguins) # dataset's structure
head(penguins) # first 6 rows


# ---- Tidying Data ----
penguins2 <- penguins %>%
				arrange(-bill_length_mm)
View(penguins2)

penguins %>% 
	group_by(species, island) %>% 
	drop_na() %>% 
	summarize(max_bl=max(bill_length_mm), mean_bl=mean(bill_length_mm))

penguins %>%
	filter(species=='Adelie')


# ---- Transforming Data ----
id <- c(1:3)
name <- c('Son Goku', 'Prince Vegeta', 'Legendary Broly')
job_title <- c('Web Developer', 'Data Scientist', 'Designer')

employees <- data.frame(id, name, job_title)
View(employees, 'Sayan Employees')

separate(employees, name, into=c('first name', 'last name'), sep=' ') # split features
unite(employees, 'name', first_name, last_name, sep=' ') # join features

penguins %>% mutate(body_mass_kg=body_mass_g/100, flipper_length_m=flipper_length_mm/1000)




# ---- Tmisc ----
install.packages('Tmisc')
install.packages('ggplot2')
install.packages('tidyverse')
install.packages('datasauRus')

library('Tmisc')
library('ggplot2')
library('tidyverse')
library('datasauRus')

data(quartet)
View(quartet)

# - mean >>  arithmetic average
# - sd   >>  standard deviation
# - cor  >>  correlation
quartet %>%
	group_by(set) %>%
	summarize(mean(x), sd(x), mean(y), sd(y), cor(x,y))

ggplot(quartet, aes(x,y)) + geom_point() + geom_smooth(method=lm, se=FALSE) + facet_wrap(~set)

ggplot(datasaurus_dozen, aes(x=x, y=y, colour=dataset)) + geom_point() + theme_void() + theme(legend.position='none') + facet_wrap(~dataset)