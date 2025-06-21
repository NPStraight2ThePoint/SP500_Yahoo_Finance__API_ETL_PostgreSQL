import pandas as pd
import yfinance as yf
import os
from datetime import date, datetime

def download_sp500_prices(
    tickers_csv_path: str,
    output_dir: str = './data/SP_500_Pricing',
    start_date: datetime = datetime(1900, 1, 1),
    end_date: date = date.today(),
    interval: str = "1d",
    auto_adjust: bool = False,
):
    """
    Download historical price data for S&P 500 tickers from Yahoo Finance.

    Args:
        tickers_csv_path (str): Path to CSV file with a 'Symbol' column of tickers.
        output_dir (str): Directory to save CSV files for each ticker.
        start_date (datetime): Starting date for historical data.
        end_date (date): Ending date for historical data.
        interval (str): Data interval, e.g. '1d', '1wk', '1mo'.
        auto_adjust (bool): Whether to adjust prices for splits/dividends.

    Saves:
        One CSV file per ticker in the output directory.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load tickers from CSV
    df = pd.read_csv(tickers_csv_path)
    tickers = df['Symbol'].tolist()

    # Track last updated date for each ticker
    last_updated = []

    for ticker in tickers:
        ticker = ticker.replace('.', '-')  # Convert Yahoo ticker format
        print(f"Downloading data for {ticker} ...")

        try:
            stock = yf.Ticker(ticker)
            data = stock.history(start=start_date, end=end_date, interval=interval, auto_adjust=auto_adjust)

            # Ensure datetime index without timezone
            data.index = pd.to_datetime(data.index).tz_localize(None)

            # Add ticker column
            data['Ticker'] = ticker

            # Reorder columns
            data = data[['Ticker'] + [col for col in data.columns if col != 'Ticker']]

            # Save to CSV
            output_path = os.path.join(output_dir, f"{ticker}.csv")
            data.to_csv(output_path, index=True)
            print(f"Saved {output_path}")

            last_updated.append({'Ticker': ticker, 'LastDownloaded': date.today().isoformat()})

        except Exception as e:
            print(f"Failed to download {ticker}: {e}")

    # Save last updated info
    last_updated_df = pd.DataFrame(last_updated)
    last_updated_path = os.path.join(output_dir, "Last_Updated_Prices.csv")
    last_updated_df.to_csv(last_updated_path, index=False)
    print(f"Saved last updated info to {last_updated_path}")

if __name__ == '__main__':
    # Example usage: update paths as needed
    TICKERS_CSV_PATH = './data/SP500_Tickers_{end_date}.csv'
    OUTPUT_DIR = './data/SP_500_Pricing'

    download_sp500_prices(
        tickers_csv_path=TICKERS_CSV_PATH,
        output_dir=OUTPUT_DIR,
        start_date=datetime(1900, 1, 1),
        end_date=date.today(),
        interval="1d",
        auto_adjust=False
    )
