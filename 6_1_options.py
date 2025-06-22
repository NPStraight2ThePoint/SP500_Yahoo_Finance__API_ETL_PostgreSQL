import yfinance as yf
import pandas as pd
import os
from datetime import date
from utils import TICKERS_CSV_PATH, OPTIONS_DIR

# Get today's date
today = date.today()

# Create output directory if it doesn't exist
os.makedirs(OPTIONS_DIR, exist_ok=True)

# Load tickers
df = pd.read_csv(TICKERS_CSV_PATH)

# Loop through tickers
for index, row in df.iterrows():
    ticker_symbol = row['Symbol'].strip().replace('.', '-')  # Adjust ticker if needed (e.g., BRK.B → BRK-B)
    try:
        ticker = yf.Ticker(ticker_symbol)
        expiration_dates = ticker.options

        if not expiration_dates:
            print(f"⚠️ No options data for {ticker_symbol}")
            continue

        all_options = []

        for expiration in expiration_dates:
            try:
                option_chain = ticker.option_chain(expiration)
                calls = option_chain.calls.copy()
                puts = option_chain.puts.copy()

                # Add expiration and type
                calls['expirationDate'] = expiration
                calls['optionType'] = 'call'
                puts['expirationDate'] = expiration
                puts['optionType'] = 'put'

                # Add mid price and intrinsic value
                calls['mid_price'] = (calls['bid'] + calls['ask']) / 2
                calls['intrinsicValue'] = calls['lastPrice'] - calls['strike']

                puts['mid_price'] = (puts['bid'] + puts['ask']) / 2
                puts['intrinsicValue'] = puts['strike'] - puts['lastPrice']  # Correct for puts

                all_options.append(pd.concat([calls, puts], ignore_index=True))
            except Exception as e:
                print(f"❌ Failed to fetch options for {ticker_symbol} on {expiration}: {e}")
                continue

        if all_options:
            final_df = pd.concat(all_options, ignore_index=True)
            output_path = os.path.join(OPTIONS_DIR, f"{ticker_symbol}_options_chain_{today}.csv")
            final_df.to_csv(output_path, index=False)
            print(f"✅ Options chain saved for {ticker_symbol} → {output_path}")
        else:
            print(f"⚠️ No options chain fetched for {ticker_symbol}")

    except Exception as e:
        print(f"❌ Error with ticker {ticker_symbol}: {e}")
