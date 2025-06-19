import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import date

today = date.today() # Get today's date

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

response = requests.get(url) # Send a GET request to the URL

soup = BeautifulSoup(response.text, 'html.parser') # Parse the HTML content

table = soup.find('table', {'id': 'constituents'}) # Find the table containing the S&P 500 companies

df = pd.read_html(str(table))[0] # Read the table into a pandas DataFrame

tickers = df['Symbol'].tolist() # Extract the ticker symbols

print(tickers) # Print the tickers

df.to_csv('SP500_Tickers.csv', index=False)
