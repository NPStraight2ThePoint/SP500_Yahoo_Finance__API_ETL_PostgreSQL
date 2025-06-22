import os
import pandas as pd
import yfinance as yf
from datetime import date
import json
from utils import cats, TICKERS_CSV_PATH, INDICATORS_CSV_PATH

def scrape_and_flatten_company_info(tickers_csv, output_csv, cats=None):
    today = date.today().strftime("%Y-%m-%d")
    df_tickers = pd.read_csv(tickers_csv)

    # Full list of indicators (only used if cats is None)
    if cats is None:
        all_data = []

    for _, row in df_tickers.iterrows():
        symbol = row['Symbol'].strip().replace('.', '-')
        print(f"Fetching info for {symbol}...")

        try:
            stock = yf.Ticker(symbol)
            info_dict = stock.get_info()
        except Exception as e:
            print(f"[WARN] Failed to fetch info for {symbol}: {e}")
            continue

        row_data = {'date': today, 'ticker': symbol}
        for indicator in cats:
            val = info_dict.get(indicator, 'NA')

            if isinstance(val, (dict, list)):
                try:
                    val = json.dumps(val)
                except Exception:
                    val = 'null'

            row_data[indicator] = val

        all_data.append(row_data)
        print(f"✅ Processed {symbol}")

    # Create final DataFrame
    df_final = pd.DataFrame(all_data)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    # Save to CSV
    df_final.to_csv(output_csv, index=False)
    print(f"\n✅ Saved combined company info to:\n{output_csv}")

# ------------------------------
# 🔽 Run script if standalone
# ------------------------------
if __name__ == "__main__":
    scrape_and_flatten_company_info(
        tickers_csv=TICKERS_CSV_PATH,
        output_csv=INDICATORS_CSV_PATH,
        cats=None  # Pass a list if you want custom subset
    )
