# ---- Simple Visualization ----
install.packages('tidyverse')
install.packages('ggplot2')
install.packages('palmerpenguins')

library('tidyverse')
library('ggplot2')
library('palmerpenguins')

ggplot(data=penguins) + geom_point(mapping=aes(x=flipper_length_mm, y=body_mass_g))



# ---- Aesthetics ----
#
# - x >> x-axis data
# - y >> y-axis data
# - color >> hue color
# - shape >> hue shape
# - size >> hue size
# - alpha >> hue alpha
ggplot(data=penguins) +
	geom_point(mapping=aes(
		x=flipper_length_mm
		, y=body_mass_g
		, color=species # 'purple, red, blue...'
		, shape=species
		#, size=species
		, alpha=species
	))



# ---- Geoms -----
geom_point() # scatter plot
geom_jitter() # scatter plot that adds noise to make easier to read the overlapping points (not good for big datasets)
geom_smooth() # line/regression plot
geom_bar() # bar plot (uses 'fill' aesthetic rather than 'color')



# ---- Facet ----
#
# - facet_wrap() >> displays plots for each possible outcome for the feature
# assigned to itself
# - facet_grid() >> displays plots for each possible outcome for the features
# assigned to itself
ggplot(data=penguins, aes(x=flipper_length_mm, y=body_mass_g)) +
	geom_point(aes(color=species, shape=species)) +
	geom_smooth(line=species) +
	facet_wrap(~island)

ggplot(data=penguins, aes(x=flipper_length_mm, y=body_mass_g)) +
	geom_point(aes(color=species, shape=species)) +
	facet_grid(sex~island)



# ---- Annotations ----
# - labs >> adds title, subtitle and caption to the plot
# - annotate >> adds simple annotations
p <- ggplot(data=penguins, aes(x=flipper_length_mm, y=body_mass_g)) +
    	geom_point(aes(color=species, shape=species)) +
    	facet_grid(sex~island) +
    labs(title='Penguins Distribution Over The Islands By Sex', subtitle='Analysing Flipper Length (in mm) With Body Mass (in g)', caption='Plot Made By Felix')

p + annotate(
    	'text'
    	, x=203
    	, y=6000
    	, label='It is a simple annotation'
    	, color='purple'
    	#, fontface='bold'
    	#, fontsize=4.5
)



# ---- Saving Plots ----
ggsave('My Plot')