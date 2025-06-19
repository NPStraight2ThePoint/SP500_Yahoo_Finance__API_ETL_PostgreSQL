import pandas as pd
import csv
import yfinance as yf
import os
from datetime import date
from datetime import datetime, timedelta

# Get today's date
today = date.today()

# Read the CSV file into a DataFrame

df = pd.read_csv('C:/.../SP500_Tickers.csv')
# List to store rows
rows = []

# Loop through each row in the DataFrame
for index, row in df.iterrows():

    stock = yf.Ticker(row['Symbol'])
    data = stock.history(period="max", interval="1d", auto_adjust=False)

    df = pd.DataFrame(data)
    df.to_csv(f'{row['Symbol']}.csv', index=True)

    print(f'Saved {row['Symbol']}.csv')

    if {row['Symbol']} is None:
        break
