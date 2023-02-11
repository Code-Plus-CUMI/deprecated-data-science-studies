#		****************
#		* Web Scraping *
#		****************
#
import pandas as pd
import requests # when the URL requires a header

url_link = 'some_random_url'

# 'deceiving' the web site to simulate that a common device is trying to access
# the URL and not a Python Script
r = requests.get(
	url_link
	, headers={'User-Agent': 'Mozzila/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
)

datas = pd.read_html(r.text)
df = datas[1] # getting the second table present on URL