"""
	*****************************
	** Inconsistent Data Entry **
	*****************************
"""

import pandas as pd

professors = pd.read_csv('filepath')
countries = professors['Country'].unique()
countries.sort()
countries
"""
array([' Germany', ' New Zealand', ' Sweden', ' USA', 'Australia',
       'Austria', 'Canada', 'China', 'Finland', 'France', 'Greece',
       'HongKong', 'Ireland', 'Italy', 'Japan', 'Macau', 'Malaysia',
       'Mauritius', 'Netherland', 'New Zealand', 'Norway', 'Pakistan',
       'Portugal', 'Russian Federation', 'Saudi Arabia', 'Scotland',
       'Singapore', 'South Korea', 'SouthKorea', 'Spain', 'Sweden',
       'Thailand', 'Turkey', 'UK', 'USA', 'USofA', 'Urbana', 'germany'],
      dtype=object)

Notice that we have 'New Zealand' and ' New Zealand';
'Germany' and 'germany'; 'USA', ' USA' and 'USofA';
'South Korea' and 'SouthKorea'.

We gotta solve this data entries problem.
"""

# Converting all datas in the column into
# lower case and removing the spaces at the
# beggining and ending of the data
professors['Country'] = professors['Country'].str.lower()
professors['Country'] = professors['Country'].str.strip()

countries = professors['Country']
countries.sort()
countries
"""
array(['australia', 'austria', 'canada', 'china', 'finland', 'france',
       'germany', 'greece', 'hongkong', 'ireland', 'italy', 'japan',
       'macau', 'malaysia', 'mauritius', 'netherland', 'new zealand',
       'norway', 'pakistan', 'portugal', 'russian federation',
       'saudi arabia', 'scotland', 'singapore', 'south korea',
       'southkorea', 'spain', 'sweden', 'thailand', 'turkey', 'uk',
       'urbana', 'usa', 'usofa'], dtype=object)

Now, we gotta a few problemms like: 'south korea' and 
'southkorea', 'usa' and 'usofa'. 
"""

########

import fuzzywuzzy
from fuzzywuzzy import process

"""
Fuzzy matching: The process of automatically finding 
text strings that are very similar to the target string. 

In general, a string is considered "closer" to another 
one the fewer characters you'd need to change if you 
were transforming one string into another. 

So "apple" and "snapple" are two changes away from each 
other (add "s" and "n") while "in" and "on" and one 
change away (replace "i" with "o"). 

You won't always be able to rely on fuzzy matching 100%, 
but it will usually end up saving you at least a little 
time.
"""

# Finding Countries Names that are similar to 'south korea' #
matches = fuzzywuzzy.process.extract('south korea'
					, countries
					, limit=10
		                     , scorer=fuzzywuzzy.fuzz.token_sort_ratio)
matches
"""
[('south korea', 100)     >> 100%
 ('southkorea', 48),      >> 48%
 ('saudi arabia', 43),    >> 43%
 ('norway', 35),          >> 35%
 ('austria', 33),         >> 33%
 ('ireland', 33),         >> 33%
 ('pakistan', 32),        >> 32%
 ('portugal', 32),        >> 32%
 ('scotland', 32),        >> 32%
 ('australia', 30)]       >> 30%

 We just need the first two ones (from 48% to 100%)
"""	

# Creating function to replace the similar countries' names #

def replace_matches_in_column(df, column
				, string_to_match
				, min_ratio=47):

    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 47
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
    # let us know the function's done
    print("All done!")

replace_matches_in_column(df=professors, column='Country'
			    , string_to_match='south korea'
			    , min_ratio=47)

###########

matches = fuzzywuzzy.process.extract('usa'
                                   , countries
                                   , limit=2
                                   , scorer=fuzzywuzzy.fuzz.token_sort_ratio)

matches
"""
[ (usa, 100)  >> 100%
, (usofa, 50) >> 50%]
"""

replace_matches_in_column(df=professors, column='Country'
                        , string_to_match='usa'
                        , min_ratio=50)

#########

countries = professors['Country'].unique()
countries.sort()
countries
"""
array(['australia', 'austria', 'canada', 'china', 'finland', 'france',
       'germany', 'greece', 'hongkong', 'ireland', 'italy', 'japan',
       'macau', 'malaysia', 'mauritius', 'netherland', 'new zealand',
       'norway', 'pakistan', 'portugal', 'russian federation',
       'saudi arabia', 'scotland', 'singapore', 'south korea', 
       'spain', 'sweden', 'thailand', 'turkey', 'uk', 'urbana', 'usa']
       , dtype=object)

Well done!! No problems anymore!!
"""