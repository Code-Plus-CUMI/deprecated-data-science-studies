"""
	************************
	** Character Encoding **
	************************

When you read a csv file that's not in 'UTF-8' charset,
you'll get an error like this one:

	/ UnicodeDecodeError: 'utf-8' codec can't decode byte 
	0x99 in position 7955: invalid start byte

To solve this, you gotta convert the file to UTF-8
following the steps bellow:

	1 - find out the file's charset;
	2 - read the file with the correct charset;
	3 - save the file with pandas (UTF-8 is the default
	charset to pandas)
"""

import pandas as pd
import chardet # library to guess the file's charset

# Guessing File's Charset #

with open('filepath', 'rb') as file:

	# read the first 10,000 bytes of the file
	# to guess the charset
	guessed_charset = chardet.detect(file.read(10000))

print(guessed_charset)
# > {'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}
# so there is 73% of chance of the charset be Windows-1252

# Reading the File with Correct Charset #
df = pd.read_csv('filepath', encoding='Windows-1252')

# Saving the File into UTF-8 #
df.to_csv('new_file_name')