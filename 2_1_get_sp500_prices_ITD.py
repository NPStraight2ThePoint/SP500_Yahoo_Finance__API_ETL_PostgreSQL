import pandas as pd
import csv
import yfinance as yf
import os
from datetime import date
from datetime import datetime, timedelta

# Define your start and end dates
start_date = datetime(1900, 1, 1) # Input 1900-01-01 to get since inception data .
#end_date = datetime(2024, 10, 2) # Input date.today() to get up until today's data.
end_date = date.today()

today = date.today()

df = pd.read_csv('SP500_Tickers.csv')

rows = []

# Loop through each row in the DataFrame
for index, row in df.iterrows():

    row['Symbol'] = row['Symbol'].replace('.', '-')

    stock = yf.Ticker(row['Symbol'])
    data = stock.history(period="max", interval="1d", auto_adjust=False)

    # Ensure the Date index is in the correct datetime format and remove timezone
    data.index = pd.to_datetime(data.index).tz_localize(None)

    # Add a new column with the ticker symbol for all rows
    data['Ticker'] = row['Symbol']

    # Reorder columns to ensure 'Ticker' is after the Date column
    data = data[['Ticker'] + [col for col in data.columns if col != 'Ticker']]

    df = pd.DataFrame(data)
    df.to_csv(f'{row['Symbol']}.csv', index=True)

    print(f'Saved {row['Symbol']}.csv')

    rows.append({'Ticker': row['Symbol'], 'Date': end_date})
    df2 = pd.DataFrame(rows)
    #df2.to_csv("Last_Updated_Prices.csv", index=False)

    if {row['Symbol']} is None:
        break
