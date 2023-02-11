#		***************************************
#		* Variables, Constants and Data Types *
#		***************************************

# - Integers: you have to put an 'L' at the end of the number to
# create integers variables. Else, even though you put just a '5'
# R will interpret it as a numerical/float variable.

# - Constants: to create constants, you have to put the value
# between 'c()'

var_1 <- 'String' # string
var_2 <- 5 # numerical (float)
var_3 <- 5.0 # numerical (float)
var_4 <- 5L # integer
var_5 <- TRUE # boolean/logical
var_6 <- FALSE # boolean/logical
var_7 <- NULL  # null

CONST_1 <- 'String'
CONST_2 <- 5
CONST_3 <- 5.0
CONST_4 <- 5L
CONST_5 <- TRUE
CONST_6 <- FALSE
CONST_7 <- NULL
lockBinding('CONST_1', globalenv())
lockBinding('CONST_2', globalenv())
lockBinding('CONST_3', globalenv())
lockBinding('CONST_4', globalenv())
lockBinding('CONST_5', globalenv())
lockBinding('CONST_6', globalenv())
lockBinding('CONST_7', globalenv())


#		**************
#		* Operations *
#		**************

1 + 1   # adiction
1 - 1   # subtraction
2 * 2   # multiplication
2 / 2   # division
3 %% 3  # modulus
3 // 3  # integer division (quocient)
4 ** 4  # power
4 ^ 4   # another way to make power

TRUE & TRUE     # AND
FALSE | FALSE   # OR
!TRUE           # NOT

#		**********
#		* Inputs *
#		**********

# - Input 1: always put 'stdin' as the argument
# - Input 2: all values are interpreted as strings and, if you desire
# to have a number for instance, you have to convert it
# - Input 3: also, you can access each line using the lists syntax (PS.:
# all vectors, matrices and lists start by 1 in R).

input <- readLines('stdin')

input[1] # gets the first line
input[2] # gets the second line

as.integer(input[1]) # converts to integer
as.numeric(input[1]) # converts to numerical/float
as.character(input[1]) # converts to character/string
as.logical(input[1]) # converts to logical/boolean



#		***********
#		* Outputs *
#		***********

# - Print: does not format the string
# - Cat: does format the string

string <- '"Hello World" - By Felix'

print(string)
# Output: [1] '/"Hello World/" - By Felix'

cat(string)
# Output: "Hello World" - By Felix