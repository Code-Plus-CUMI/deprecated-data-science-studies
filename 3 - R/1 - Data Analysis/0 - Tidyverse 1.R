# ---- Listing All Installed Packages ----
installed.packages()

# ---- Installing and Importing a Package ----
install.packages('palmerpenguins')
install.packages('tidyverse')

library('palmerpenguins')
library('tidyverse')

# ---- Displaying Summary Statistics ----
summary(penguins)

# ---- Displaying The Dataset ----
View(penguins, 'Palmer Penguins Dataset')

# ---- 'Dir' Function Like in Python ----
?View()

# ---- Removing a Variable ----
view_title <- 'Palmer Penguins Dataset'
rm(view_title)

# ---- Pipes ----
penguins_2008 <- penguins %>% filter(year == 2008)