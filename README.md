# Overview

ETL pipeline that extracts historical pricing & financial indicators for all S&P 500 tickers from Yahoo Finance API to PostgreSQL DB via Python.

## Tech Stack

- Programming Language: **Python**
- API: **Yahoo Finance**
- Database: **PostgreSQL**
- Libraries: **BeautifulSoup, pandas, yfinance, psycopg2**

## Workflow

| Script                      | Description                                              | Data List (File)           | DB View (Screenshot)                                                                                              |
|-----------------------------|----------------------------------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------|
| `1_get_sp500_tickers.py`    | Scrapes S&P 500 ticker list from Wikipedia               | `sp500_tickers.csv`         |                                                                                                                  |
| `2_1_get_sp500_prices.py`   | Extracts OHLCV pricing, splits, dividends                | `pricing_data.csv`          | [Pricing Table](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Pricing.png)             |
| `3_1_get_sp500_indicators.py`| Extracts 180+ financial indicators                       | `indicators.csv`            | [Indicators Table](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Indicators.png)           |
| `4_1_recommendations.py`    | Extracts analyst recommendations for tickers             | `recommendations.csv`       | [Recommendations](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Recommendations.png)       |
| `5_1_options.py`            | Extracts options chains data                              | `options_chain.csv`         | [Options Chain](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Options_chains.png)           |
| `6_1_get_BS_IS_CF.py`       | Extracts Balance Sheet, Income Statement, Cash Flow data | `financial_statements.csv`  | [Financials](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Financial%20Statements.png)      |




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
