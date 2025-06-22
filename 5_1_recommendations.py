import yfinance as yf
import pandas as pd
import os
from datetime import date
from utils import TICKERS_CSV_PATH, RECOMMENDATIONS_DIR

today = date.today()

df = pd.read_csv(TICKERS_CSV_PATH)

os.makedirs(RECOMMENDATIONS_DIR, exist_ok=True)

# Loop through each symbol
for index, row in df.iterrows():
    symbol = row['Symbol'].strip()
    try:
        stock = yf.Ticker(symbol)
        recommendations = stock.recommendations

        # Check if data exists
        if recommendations is not None and not recommendations.empty:
            file_path = os.path.join(RECOMMENDATIONS_DIR, f"{symbol}_recommendations_{today}.csv")
            recommendations.to_csv(file_path, index=False)
            print(f"✅ {symbol} recommendations saved to: {file_path}")
        else:
            print(f"⚠️ No recommendations found for: {symbol}")

    except Exception as e:
        print(f"❌ Error fetching recommendations for {symbol}: {e}")


