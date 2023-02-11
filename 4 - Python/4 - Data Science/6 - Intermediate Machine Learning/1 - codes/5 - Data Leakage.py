"""
Data Leakage has two types:

1 - Target Leakage: some features (X) have their value defined AFTER
the target variable (y) is defined, for example:

	/ y: got pneumonia >> True, False
	/ X: took antibiotic medicine >> True False

People take antibiotic medicines after getting pneumonia in order to 
recover. So the raw data shows a strong relationship between those 
columns. But "took_antibiotic_medicine" is frequently changed after the 
value for "got_pneumonia" is determined. This is target leakage.

To prevent this type of data leakage, any variable updated (or created) 
after the target value is realized should be EXCLUDED. Because when 
we use this model to make new predictions, that data won't be 
available to the model.

####

2 - Train-Test Contamination: a much different type of leak occurs 
when you aren't careful  distinguishing training data from validation 
data. 

For example, this happens if you run preprocessing (like fitting the 
Imputer for missing values) before calling "train_test_split". 
Validation is meant to be a measure of how the model does on data it 
hasn't considered before. You can corrupt this process in subtle ways 
if the validation data affects the preprocessing behaviour. The end 
result? Your model will get very good validation scores, giving you 
great confidence in it, but perform poorly when you deploy it to make
decisions.

######

- Problem when you use the AVG Sales of the houses in a neighborhood
to predict the price of a house in this same neighborhood:

This poses a risk of both target leakage and train-test contamination 
(though you may be able to avoid both if you are careful).

-*-*-*-*

You have target leakage if a given patient's outcome contributes to 
the infection rate for his surgeon, which is then plugged back into 
the prediction model for whether that patient becomes infected. 
You can avoid target leakage if you calculate the surgeon's infection 
rate by using only the surgeries before the patient we are predicting 
for. Calculating this for each surgery in your training data may be a 
little tricky.

You also have a train-test contamination problem if you calculate 
this using all surgeries a surgeon performed, including those from 
the test-set. The result would be that your model could look very 
accurate on the test set, even if it wouldn't generalize well to new 
patients after the model is deployed. This would happen because the 
surgeon-risk feature accounts for data in the test set. Test sets 
exist to estimate how the model will do when seeing new data. 
So this contamination defeats the purpose of the test set.
"""