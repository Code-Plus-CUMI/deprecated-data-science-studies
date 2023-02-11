#		***********
#		* Vectors *
#		***********
#
# Can only storage datas with the same type!
#
my_vector_1 = c(4, 5, 6, 7, 8) # like lists in Python
my_vector_2 = c('Goku': 1, 'Vegeta': 2, 'Broly': 3) # like dicts in Python

my_vector_1[1] # Output: 4

# - To return just the value, use two brakets '[[]]'
my_vector_2[1] # Output: 'Goku': 1
my_vector_2['Goku'] # Output: 'Goku': 1
my_vector_2[[1]] # Output: 1
my_vector_2[['Goku']] # Output: 1

# - Also, you can exclude an element using '-'
# - And make a range using ':'
my_vector_1[-2] # Output: 4, 6, 7, 8
my_vector_1[2:4] # Output: 5, 6, 7

# Filters
my_vector_1[my_vector_1 > 6]




#		*********
#		* Lists *
#		*********
#
# They are like vectors, but can stora datas with different data types
#
my_list = list(TRUE, 'Felix', 5L, NULL, 5.0, 3i)
my_dict = list('name'='Felix', 'age'=22, 'country'='Brazil')

my_dict['name']    # Output: [1] 'name' 'Felix'
my_dict[['name']]  # Output: 'Felix'
my_dict$name       # Output: 'Felix' >> this is the preferred form to access lists elements

my_vector <- unlist(my_list) # this is a way to convert a list into a vector




#		************
#		* Matrices *
#		************
#
# Store datas in more than one dimension, but they (datas) must be on the same type
#
my_matrix <- matrix(c(1, 2, 3, 4, 5, 6), nrow=2, ncol=3)

# If one of the parameters 'nrow' or 'ncol' is not informed
# R calculates it!
my_matrix_2 <- matrix(c(1, 2, 3, 4, 5, 6), nrow=2)

# To access an element, you can do like this
my_matrix[1, 3] # element at row 1 and column 3
my_matrix[1, ]  # elements at row 1
my_matrix[ ,3]  # elements at column 3

t(my_matrix) # tranposes a matrix




#		***************
#		* Data Frames *
#		***************
#
# The most important data type in R. They are like the data frames in Python
# To access datas, you do on the same way to lists, vectors and matrices
df1 <- data.frame('id'=1:2, 'names'=c('Gabriel', 'Felix'), 'age'=c(22, 23))