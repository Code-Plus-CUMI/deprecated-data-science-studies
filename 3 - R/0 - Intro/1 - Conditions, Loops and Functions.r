#		**************
#		* Conditions *
#		**************

# If-Else Block
condition_1 <- TRUE
condition_2 <- FALSE

if (condition) {
	# code
} else if (condition_2) {
	# code
} else {
	# code
}


# Switch Block
#
# - Returns the index (first parameter)
# - You can also use the abbreviation form
index = 2
switch(index, 'Goku', 'Vegeta', 'Broly') # Output: 'Vegeta'

abbr = 'BR'
switch(abbr, 'GO' = 'Goku', 'VE' = 'Vegeta', 'BR' = 'Broly') # Output: 'Broly'



#		*********
#		* Loops *
#		*********
#
# - break: it's like 'break' statement in Python
# - next: it's like 'continue' statement in Python

# For Loop
for (x in 1:50) {
	if (x %% 2 == 1) { next }

	print(x)
}

# While Loop
while(True) {
	for (x in 50:1) {
		if (x == 15) { break }
	}
}



#		*************
#		* Functions *
#		*************
power <- function(x, y=2) {
	return (x**y)
}

print(power(5))       # Output: 10
print(power(5, 3))   # Output: 125



#		**********************
#		* Built-in Functions *
#		**********************
min(7, 10, 3) # Output: 3  >> returns the minimum number
max(7, 10, 3) # Output: 10 >> returns the maximum number
sqrt(16)      # Output: 4  >> returns the square root


str_1 = 'Hello'
str_2 = ' World'
str_3 = '!'
paste(str_1, str_2, str_3, sep='') # Output: Hello World! >> concatenates strings
nchar(str_1) # Output: 5 >> returns the string length
substr(str_1, 4, 5) # Output: lo >> returns substring


vector <- c(5, 2, 3, 7)
length(vector) 					 # Output: 4 >> returns the number of elements
sum(vector)    					 # Output: 17 >> returns the sum
sort(vector, decreasing=FALSE)   # Output: c(2, 3, 5, 7) >> sorts the vector, list....
mean(vector)					 # returns the arithmetic mean
median(vector)					 # returns the median
sd(vector)						 # returns the Standard Deviation

2:10 			 # Output: 2, 3, 4, 5, 6, 7, 8, 9, 10 >> sequences without steps
seq(2, 10, by=2) # Output: 2, 4, 6, 8, 10 >> sequences by steps

t(my_matrix)                 # tranposes a matrix
summary(my_dataframe)        # returns stats info about a dataframe
factor(c('Male', 'Female'))  # converts strings into categorical/factor features
levels(factos)               # returns all possible values for a factor feature