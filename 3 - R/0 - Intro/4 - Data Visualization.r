#		************************
#		* Data - Visualization *
#		************************
#
x1 <- mtcars$wt
x2 <- mtcars$gears
y <- mtcars$drat

png(file = "chart.png")

# 0) Dot Chart
#
# - main: chart's title (common to all charts)
# - xlab: x-axis name (common to all charts)
# - ylab: y-axis name (common to all charts)
plot(x1, y, main='My Chart', xlab='The x-axis', ylab='The y-axis')
plot(1:15, main="My Chart", xlab="The x-axis", ylab="The y-axis")

# 1) Line Plot
#
# - You just have to add "type='l'" to create a line plot
# - If you desire to add more lines, use 'lines' function
plot(
	x1, y
	, main='My Chart'
	, xlab='The x-axis'
	, ylab='The y-axis'
	, type='l'
	, col='blue'
)

lines(
	x2, y
	, type='l'
	, col='red'
)

# 2) Bar Plot
#
# - names.arg: the bars labels
# - label: it is the same as 'names.arg'
# - horiz: horizontal (TRUE) or vertical plot (FALSE)
# - col: colors
barplot(
	mtcars$hp
	, names.arg = rownames(mtcars)
	, horiz=TRUE
	, col=c('blue', 'red')
)

# 3) Pie Plots
pie(x1, label=y, main='My Pie Chart')

# 4) Box Plots and Histograms
#
# - Box Plots: represent how the datas are distributed
# (min, max, median, quartiles)
#
# - Histograms: represent the frequencies in buckets
boxplot(mtcars$mpg)
hist(mtcars$hp)