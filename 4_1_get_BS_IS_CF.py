import os
from datetime import date
import yfinance as yf
import pandas as pd
from utils import TICKERS_CSV_PATH, FINANCIALS_DIR

# Get today's date
today = date.today()

df = pd.read_csv(TICKERS_CSV_PATH)

os.makedirs(FINANCIALS_DIR, exist_ok=True)

# Loop through each ticker
for index, row in df.iterrows():
    symbol = row['Symbol'].strip()
    try:
        ticker = yf.Ticker(symbol)

        # Get financial statements
        income_annual = ticker.financials
        income_quarterly = ticker.quarterly_financials
        balance_annual = ticker.balance_sheet
        balance_quarterly = ticker.quarterly_balance_sheet
        cash_annual = ticker.cashflow
        cash_quarterly = ticker.quarterly_cashflow
        print(ticker.financials)
        # Reset index (convert to tidy format)
        dfs_annual = [
            income_annual.reset_index(),
            balance_annual.reset_index(),
            cash_annual.reset_index()
        ]
        dfs_quarterly = [
            income_quarterly.reset_index(),
            balance_quarterly.reset_index(),
            cash_quarterly.reset_index()
        ]

        # Label each statement
        for df_, label in zip(dfs_annual, ['Income Statement', 'Balance Sheet', 'Cash Flow']):
            df_['Statement'] = label
        for df_, label in zip(dfs_quarterly, ['Income Statement', 'Balance Sheet', 'Cash Flow']):
            df_['Statement'] = label

        # Combine
        combined_annual = pd.concat(dfs_annual, ignore_index=True)
        combined_quarterly = pd.concat(dfs_quarterly, ignore_index=True)

        # Reorder columns
        cols_annual = ['Statement'] + [col for col in combined_annual.columns if col != 'Statement']
        cols_quarterly = ['Statement'] + [col for col in combined_quarterly.columns if col != 'Statement']
        combined_annual = combined_annual[cols_annual]
        combined_quarterly = combined_quarterly[cols_quarterly]

        # Save to CSVs
        annual_file = os.path.join(FINANCIALS_DIR, f"{symbol}_Financial_statements_A_{today}.csv")
        quarterly_file = os.path.join(FINANCIALS_DIR, f"{symbol}_Financial_statements_Q_{today}.csv")

        combined_annual.to_csv(annual_file, index=False)
        combined_quarterly.to_csv(quarterly_file, index=False)

        print(f"✅ {symbol} - Annual saved to {annual_file}")
        print(f"✅ {symbol} - Quarterly saved to {quarterly_file}")

    except Exception as e:
        print(f"❌ Failed for {symbol}: {e}")


import pandas as pd

def transform_financial_csv(file_path: str, ticker: str) -> pd.DataFrame:
    """
    Transform raw wide-format financial statement CSV into long tidy format.
    """
    df = pd.read_csv(file_path)

    # Melt wide format to long
    df_melted = df.melt(id_vars=["Statement", "index"], var_name="Date", value_name="Value")

    # Rename for clarity
    df_melted.rename(columns={"index": "Metric"}, inplace=True)

    # Add ticker column
    df_melted["Ticker"] = ticker

    # Optional: reorder columns
    df_melted = df_melted[["Ticker", "Statement", "Metric", "Date", "Value"]]

    return df_melted

import glob

all_files = glob.glob(os.path.join(FINANCIALS_DIR, "*_Financial_statements_A_*.csv"))

all_transformed = []

for file_path in all_files:
    filename = os.path.basename(file_path)
    ticker = filename.split("_")[0]  # Get ticker from filename
    try:
        df_transformed = transform_financial_csv(file_path, ticker)
        all_transformed.append(df_transformed)
        print(f"✅ Processed {ticker}")
    except Exception as e:
        print(f"❌ Failed for {ticker}: {e}")

all_files_q = glob.glob(os.path.join(FINANCIALS_DIR, "*_Financial_statements_Q_*.csv"))

all_transformed_q = []

for file_path in all_files_q:
    filename = os.path.basename(file_path)
    ticker = filename.split("_")[0]  # Get ticker from filename
    try:
        df_transformed = transform_financial_csv(file_path, ticker)
        all_transformed.append(df_transformed)
        print(f"✅ Processed {ticker}")
    except Exception as e:
        print(f"❌ Failed for {ticker}: {e}")