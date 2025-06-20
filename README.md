# Overview

ETL pipeline that extracts historical pricing & financial indicators for all S&P 500 tickers from Yahoo Finance API to PostgreSQL DB via python.

## Tech Stack
- Programming Language: **Python**
- API: **Yahoo Finance**
- Database: **PostgreSQL**
- Libraries: **BeautifulSoup, pandas, yfinance, psycopg2**

## Workflow

1_get_sp500_tickers.py   -> Scraoe all S&P 500 Tickers from wikipedia.
2_1_get_sp500_prices_ITD.py -> Retreive inception to date historical pricing (Open,Close,High,Low,Adj.Close,Volume) for all S&P 500 tickers.
2_2_prices_compile_load -> Load pricing data in DB.
3_1_get_sp500_indicators -> Retreive 180+ indicators for all S&P 500 tickers.     
