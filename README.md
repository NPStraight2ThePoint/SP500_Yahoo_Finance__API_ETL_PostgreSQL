# Overview

ETL pipeline that extracts historical pricing & financial indicators for all S&P 500 tickers from Yahoo Finance API to PostgreSQL DB via Python.

## Tech Stack

- Programming Language: **Python**
- API: **Yahoo Finance**
- Database: **PostgreSQL**
- Libraries: **BeautifulSoup, pandas, yfinance, psycopg2**

## Workflow

- `1_get_sp500_tickers.py`  
  → Scrape all S&P 500 tickers from Wikipedia.

- `2_1_get_sp500_prices_ITD.py`  
  → Retrieve inception-to-date historical pricing (Open, Close, High, Low, Adj. Close, Volume, Dividends, Stock Splits) for all S&P 500 tickers.

- `2_2_prices_compile_load.py`  
  → Load pricing data into the database.

- `3_1_get_sp500_indicators.py`  
  → Retrieve 180+ indicators for all S&P 500 tickers.  
  [Yahoo Finance Indicators](https://github.com/NPStraight2ThePoint/Yahoo_Finance_API_ETL_PostgreSQL/blob/Main/yahoo_finance_indicators)

- `3_2_indicators_compile_load.py`  
  → Load indicator data into the database.

- `4_adj_closes_ITD_merged.py`  
  → Merge all Adj. Close pricing into one CSV.

## Database

 - [Pricing](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/DB_S%26P%20500%20Pricing%20Table.png)
 - [Indicators](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/DB_S%26P%20500%20Indicators%20Table.png)
 

### 🆔 Project Info

**Author:** *Nicholas Papadimitris *  
**Created on:** *01/03/2025 9:00 PM* (UTC)   
**Project ID:** `YF_ETL_01_Mar2025`
**GitHub**: [My GitHub](https://github.com/NPStraight2ThePoint)

📧 **Email:** nicholas.papadimitris@gmail.com  
💼 **LinkedIn:** [Nicholas Papadimitris](https://www.linkedin.com/in/nicholas-papadimitris/)
---
