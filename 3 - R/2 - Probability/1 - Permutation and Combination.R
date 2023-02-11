library(gtools) # permutation and combination functions

numbers <- c('Ace', 'Deuce', 'Three', 'Four', 'Five'
			, 'Six', 'Seven', 'Eight', 'Nine', 'Ten'
			, 'Jack', 'Queen', 'King')
suits   <- c('Diamonds', 'Hearts', 'Clubs', 'Spades')

# 0) Sample, Paste, Expand.Grid, Permutations
# and Combinations #
#
# \ Sample: gets a sample
# \ Paste: joins elements from vectors
# \ Expand.Grid: joins elements from vectors in
# a grid/table format
#
# \ Permutation: order matters
# \ Combination: order doesn't matter

deck <- expand.grid(number=numbers, suit=suits)
deck <- paste(deck$numbers, deck$suits)

kings <- paste('King', suits)
aces <- paste('Ace', suits)
mean(kings %in% deck) # probability of King be drawn in a deck

####

permutations(3, 2) # [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
combinations(3, 2) # [[1, 2], [1, 3], [2, 3]]

hands <- combination(52, 2, v=deck)
mean((hands[,1] %in% aces & hands[,2] %in% kings) 
   | (hands[,1] %in% kings & hands[,2] %in% aces))

# 1) Duplicated
#
# \ Duplicated: returns TRUE if the element appeared
# before in the vector
#
# Code: checks out the probability of getting two
# people (at least) with the same birthday
people      <- 50
repetitions <- 10000

results <- replicate(repetitions, {
	bdays <- sample(1:365, people, replace=TRUE)
	any(duplicated(bdays))
})

mean(results)

# The proce to repeat the same experiment X times
# is known as 'Monte Carlo Experiment' and, as 
# higher the number of repetitions, as better
# and approximate to the reality will be the results