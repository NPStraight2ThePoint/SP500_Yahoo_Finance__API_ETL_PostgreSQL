import os
import pandas as pd
import yfinance as yf
from datetime import date, datetime
from utils import PRICING_DIR, TICKERS_CSV_PATH

os.makedirs(PRICING_DIR, exist_ok=True)

def download_sp500_prices(
    tickers_csv_path: str,
    output_dir: str,
    start_date: datetime = datetime(1900, 1, 1),
    end_date: date = date.today(),
    interval: str = "1d",
    auto_adjust: bool = False,
):
    df = pd.read_csv(tickers_csv_path)
    tickers = df['Symbol'].tolist()
    last_updated = []

    for ticker in tickers:
        ticker = ticker.replace('.', '-')  # Fix Yahoo format
        print(f"⬇️ Downloading: {ticker}")

        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="max", interval=interval, auto_adjust=auto_adjust)

            data.index = pd.to_datetime(data.index).tz_localize(None)
            data['Ticker'] = ticker
            data = data[['Ticker'] + [col for col in data.columns if col != 'Ticker']]

            output_path = os.path.join(output_dir, f"{ticker}.csv")
            data.to_csv(output_path)
            print(f"✅ Saved: {output_path}")

            last_updated.append({'Ticker': ticker, 'LastDownloaded': date.today().isoformat()})

        except Exception as e:
            print(f"❌ Failed {ticker}: {e}")

if __name__ == "__main__":
    download_sp500_prices(
        tickers_csv_path=TICKERS_CSV_PATH,
        output_dir=PRICING_DIR,
        interval="1d",
        auto_adjust=False
    )

