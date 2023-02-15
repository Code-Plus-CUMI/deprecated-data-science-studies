# Libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud # pip install wordcloud
import numpy as np

# Function to generate word clouds
def generate_wordcloud(df, column, max_font_size=60, mask, collocations=False):
		text = df[column].values
		return WordCloud(
			max_font_size=max_font_size
			, collocations=collocations).generate(str(text)
			, mask=mask
		)

# Generating and Plotting Word Cloud
mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))
wordcloud = generate_wordcloud(df, 'video_title') # or any string feature
plt.imshow(wordcloud)
plt.axis('off')
plt.show()