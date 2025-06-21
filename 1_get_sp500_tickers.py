import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import os

def scrape_sp500_tickers(output_dir: str = './data', save_csv: bool = True) -> list:
    """
    Scrapes the list of S&P 500 tickers from Wikipedia and saves to CSV.

    Args:
        output_dir (str): Directory to save the CSV file.
        save_csv (bool): Whether to save the CSV file.

    Returns:
        List[str]: List of ticker symbols.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

    response = requests.get(url)
    response.raise_for_status()  # Raise error if request failed

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'constituents'})

    df = pd.read_html(str(table))[0]
    tickers = df['Symbol'].tolist()

    if save_csv:
        today_str = date.today().isoformat()
        output_path = os.path.join(output_dir, f'SP500_Tickers_{today_str}.csv')
        df.to_csv(output_path, index=False)
        print(f'Saved S&P 500 tickers CSV to: {output_path}')

    return tickers

if __name__ == '__main__':
    tickers = scrape_sp500_tickers()
    print(f'Total tickers scraped: {len(tickers)}')
