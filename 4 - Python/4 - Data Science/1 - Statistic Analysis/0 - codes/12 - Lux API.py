#	*************
#	** Lux API **
#	*************
#
# Lux API is a library that helps you to visualize your datas with less lines
# of code, effortless, quickier and simple.
#
# Simple Tutorial: https://towardsdatascience.com/intelligent-visual-data-discovery-with-lux-a-python-library-dc36a5742b2f
#



# ---- Installing on Jupyter Notebook and Jupyter Lab ----
pip install lux-api



# ---- Activating Extension for Jupyter Notebook ----
jupyter nbextension install --py luxwidget
jupyter nbextension enable --py luxwidget



# ---- Activating Extension for Jupyter Lab ----
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install luxwidget



# ---- Using the Library ----
import pandas as pd
import lux

df = pd.read_csv('dataset.csv')

# data transformations and stuff like that...

df
# when you print your dataframe like the code above, a toogle button
# for Lux API will be available and, when you hit it, you'll have access
# to a tons of visualizations of your dataset!