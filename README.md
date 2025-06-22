# Overview

ETL pipeline that extracts historical pricing & financial indicators for all S&P 500 tickers from Yahoo Finance API to PostgreSQL DB via Python.

## Tech Stack

- Programming Language: **Python**
- API: **Yahoo Finance**
- Database: **PostgreSQL**
- Libraries: **BeautifulSoup, pandas, yfinance, psycopg2**
- S&P 500 Ticker List: [Wikipedia - List of S&P 500 Companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)

## Workflow

| Script                      | Description                                              | Data List (Schema Link)                                                                 | DB View (Screenshot)                                                                                              |
|-----------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `1_get_sp500_tickers.py`    | Scrapes S&P 500 ticker list from Wikipedia               | [`sp500_tickers.csv`](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/SP500_Tickers.csv) |                                                                                                                    |
| `2_1_get_sp500_prices.py`   | Extracts OHLCV pricing, splits, dividends                | [`pricing_data.csv`](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Schemas/Schemas_Pricing) | [Pricing Table](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Pricing.png)              |
| `3_1_get_sp500_indicators.py`| Extracts 180+ financial indicators                       | [`indicators.csv`](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Schemas/Schemas_Indicators) | [Indicators Table](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Indicators.png)          |
| `4_1_recommendations.py`    | Extracts analyst recommendations for tickers             | [`recommendations.csv`](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Schemas/Schemas_Recommendations) | [Recommendations](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Recommendations.png)      |
| `5_1_options.py`            | Extracts options chains data                             | [`options_chain.csv`](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Schemas/Schemas_Options) | [Options Chain](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Options_chains.png)          |
| `6_1_get_BS_IS_CF.py`       | Extracts Balance Sheet, Income Statement, Cash Flow data | [`financial_statements.csv`](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Schemas/Schemas_financial_statements) | [Financials](https://github.com/NPStraight2ThePoint/SP500_Yahoo_Finance__API_ETL_PostgreSQL/blob/Main/Database/Financial%20Statements.png)     |


### 🆔 Project Info

**Author:** *Nicholas Papadimitris *  
**Created on:** *01/03/2025 9:00 PM* (UTC)   
**Project ID:** `YF_ETL_01_Mar2025`
**GitHub**: [My GitHub](https://github.com/NPStraight2ThePoint)

📧 **Email:** nicholas.papadimitris@gmail.com  
💼 **LinkedIn:** [Nicholas Papadimitris](https://www.linkedin.com/in/nicholas-papadimitris/)
---
