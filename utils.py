import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import date

today_str = date.today().isoformat()  # '2025-06-22'

load_dotenv()

def get_repo_root_from_marker(marker_filename="URI_102852.txt") -> Path:
    """
    Finds the parent directory where the marker file (e.g. 'URI_102852.txt') exists.
    """
    current = Path(__file__).resolve()
    for parent in current.parents:
        marker_path = parent / marker_filename
        if marker_path.exists():
            return parent
    raise FileNotFoundError(f"❌ Could not find '{marker_filename}' in any parent directory.")

# Usage
ROOT_DIR = get_repo_root_from_marker()
print("📁 ROOT DIR:", ROOT_DIR)

STATIC_DIR = os.path.join(ROOT_DIR, "Static Data")
PRICING_DIR = os.path.join(ROOT_DIR, "SP_500_Pricing")
INDICATORS_DIR = os.path.join(ROOT_DIR, "SP_500_Company_Info")
FINANCIALS_DIR = os.path.join(ROOT_DIR, "Financial Statements")
RECOMMENDATIONS_DIR = os.path.join(ROOT_DIR, "Recommendations")
OPTIONS_DIR = os.path.join(ROOT_DIR, "Options")
ARCHIVE_DIR = os.path.join(ROOT_DIR, "Archive")
TICKERS_CSV_PATH = os.path.join(STATIC_DIR, "SP500_Tickers.csv")
INDICATORS_CSV_PATH = os.path.join(INDICATORS_DIR, f"company_info_flat_{today_str}.csv")

# --- DB Config from .env ---
DB_CONFIG_1 = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
}

DB_CONFIG_2 = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

PRICING_TABLE = 'public.sp_500_pricing'
INDICATORS_TABLE = 'public.sp_500_indicators'
FINANCIALS_A_TABLE = "sp500_financial_statements_annual"
FINANCIALS_Q_TABLE = "sp500_financial_statements_quarterly"
RECOMMENDATIONS_TABLE = "recommendations"
OPTIONS_TABLE = "options_chains"


cats = ["52WeekChange", "SandP52WeekChange", "address1", "ask", "askSize", "auditRisk", "averageAnalystRating",
                "averageDailyVolume10Day", "averageDailyVolume3Month", "averageVolume", "averageVolume10days", "beta",
                "bid", "bidSize", "boardRisk", "bookValue", "city", "companyOfficers", "compensationAsOfEpochDate",
                "compensationRisk", "corporateActions", "country", "cryptoTradeable", "currency", "currentPrice",
                "currentRatio", "customPriceAlertConfidence", "dateShortInterest", "dayHigh", "dayLow", "debtToEquity",
                "displayName", "dividendDate", "dividendRate", "dividendYield", "earningsCallTimestampEnd",
                "earningsCallTimestampStart", "earningsGrowth", "earningsQuarterlyGrowth", "earningsTimestamp",
                "earningsTimestampEnd", "earningsTimestampStart", "ebitda", "ebitdaMargins", "enterpriseToEbitda",
                "enterpriseToRevenue", "enterpriseValue", "epsCurrentYear", "epsForward", "epsTrailingTwelveMonths",
                "esgPopulated", "exDividendDate", "exchange", "exchangeDataDelayedBy", "exchangeTimezoneName",
                "exchangeTimezoneShortName", "executiveTeam", "fiftyDayAverage", "fiftyDayAverageChange",
                "fiftyDayAverageChangePercent", "fiftyTwoWeekChangePercent", "fiftyTwoWeekHigh",
                "fiftyTwoWeekHighChange", "fiftyTwoWeekHighChangePercent", "fiftyTwoWeekLow", "fiftyTwoWeekLowChange",
                "fiftyTwoWeekLowChangePercent", "fiftyTwoWeekRange", "financialCurrency", "firstTradeDateMilliseconds",
                "fiveYearAvgDividendYield", "floatShares", "forwardEps", "forwardPE", "freeCashflow",
                "fullExchangeName", "fullTimeEmployees", "gmtOffSetMilliseconds", "governanceEpochDate", "grossMargins",
                "grossProfits", "hasPrePostMarketData", "heldPercentInsiders", "heldPercentInstitutions",
                "impliedSharesOutstanding", "industry", "industryDisp", "industryKey", "irWebsite",
                "isEarningsDateEstimate", "language", "lastDividendDate", "lastDividendValue", "lastFiscalYearEnd",
                "lastSplitDate", "lastSplitFactor", "longBusinessSummary", "longName", "market", "marketCap",
                "marketState", "maxAge", "messageBoardId", "mostRecentQuarter", "netIncomeToCommon",
                "nextFiscalYearEnd", "numberOfAnalystOpinions", "open", "operatingCashflow", "operatingMargins",
                "overallRisk", "payoutRatio", "phone", "postMarketChange", "postMarketChangePercent", "postMarketPrice",
                "postMarketTime", "previousClose", "priceEpsCurrentYear", "priceHint", "priceToBook",
                "priceToSalesTrailing12Months", "profitMargins", "quickRatio", "quoteSourceName", "quoteType",
                "recommendationKey", "recommendationMean", "region", "regularMarketChange",
                "regularMarketChangePercent", "regularMarketDayHigh", "regularMarketDayLow", "regularMarketDayRange",
                "regularMarketOpen", "regularMarketPreviousClose", "regularMarketPrice", "regularMarketTime",
                "regularMarketVolume", "returnOnAssets", "returnOnEquity", "revenueGrowth", "revenuePerShare", "sector",
                "sectorDisp", "sectorKey", "shareHolderRightsRisk", "sharesOutstanding", "sharesPercentSharesOut",
                "sharesShort", "sharesShortPreviousMonthDate", "sharesShortPriorMonth", "shortName",
                "shortPercentOfFloat", "shortRatio", "sourceInterval", "state", "symbol", "targetHighPrice",
                "targetLowPrice", "targetMeanPrice", "targetMedianPrice", "totalCash", "totalCashPerShare", "totalDebt",
                "totalRevenue", "tradeable", "trailingAnnualDividendRate", "trailingAnnualDividendYield", "trailingEps",
                "trailingPE", "trailingPegRatio", "triggerable", "twoHundredDayAverage", "twoHundredDayAverageChange",
                "twoHundredDayAverageChangePercent", "typeDisp", "volume", "website", "zip"]

# Step 1: Define your list of allowed columns
financial_statements_columns = [
    "ticker","date","balancesheet_accounts_payable","balancesheet_accounts_receivable","balancesheet_accumulated_depreciation",
    "balancesheet_additional_paid_in_capital","balancesheet_buildings_and_improvements","balancesheet_capital_stock",
    "balancesheet_cash_and_cash_equivalents","balancesheet_cash_cash_equivalents_and_short_term_investments","balancesheet_commercial_paper",
    "balancesheet_common_stock","balancesheet_common_stock_equity","balancesheet_current_accrued_expenses","balancesheet_current_assets",
    "balancesheet_current_debt","balancesheet_current_debt_and_capital_lease_obligation","balancesheet_current_deferred_liabilities",
    "balancesheet_current_deferred_revenue","balancesheet_current_liabilities","balancesheet_employee_benefits","balancesheet_finished_goods",
    "balancesheet_gains_losses_not_affecting_retained_earnings","balancesheet_goodwill","balancesheet_goodwill_and_other_intangible_assets","balancesheet_gross_ppe",
    "balancesheet_inventory","balancesheet_invested_capital","balancesheet_investments_and_advances","balancesheet_land_and_improvements",
    "balancesheet_long_term_debt","balancesheet_long_term_debt_and_capital_lease_obligation","balancesheet_machinery_furniture_equipment",
    "balancesheet_net_debt","balancesheet_net_ppe","balancesheet_net_tangible_assets","balancesheet_non_current_pension_and_other_postretirement_benef",
    "balancesheet_ordinary_shares_number","balancesheet_other_current_assets","balancesheet_other_equity_adjustments","balancesheet_other_intangible_assets",
    "balancesheet_other_non_current_assets","balancesheet_other_non_current_liabilities","balancesheet_other_short_term_investments","balancesheet_payables",
    "balancesheet_payables_and_accrued_expenses","balancesheet_pensionand_other_post_retirement_benefit_plans_cur","balancesheet_preferred_stock",
    "balancesheet_properties","balancesheet_raw_materials","balancesheet_receivables","balancesheet_retained_earnings","balancesheet_share_issued",
    "balancesheet_stockholders_equity","balancesheet_tangible_book_value","balancesheet_total_assets","balancesheet_total_capitalization",
    "balancesheet_total_debt","balancesheet_total_equity_gross_minority_interest","balancesheet_total_liabilities_net_minority_interest",
    "balancesheet_total_non_current_assets","balancesheet_total_non_current_liabilities_net_minority_interes","balancesheet_working_capital",
    "cashflow_asset_impairment_charge","cashflow_beginning_cash_position","cashflow_capital_expenditure","cashflow_cash_dividends_paid",
    "cashflow_cash_flow_from_continuing_financing_activities","cashflow_cash_flow_from_continuing_investing_activities",
    "cashflow_cash_flow_from_continuing_operating_activities","cashflow_change_in_account_payable","cashflow_change_in_inventory",
    "cashflow_change_in_other_working_capital","cashflow_change_in_payable","cashflow_change_in_payables_and_accrued_expense",
    "cashflow_change_in_receivables","cashflow_change_in_working_capital","cashflow_changes_in_account_receivables","cashflow_changes_in_cash",
    "cashflow_common_stock_dividend_paid","cashflow_common_stock_payments","cashflow_deferred_income_tax","cashflow_deferred_tax",
    "cashflow_depreciation_amortization_depletion","cashflow_depreciation_and_amortization","cashflow_effect_of_exchange_rate_changes",
    "cashflow_end_cash_position","cashflow_financing_cash_flow","cashflow_free_cash_flow","cashflow_gain_loss_on_investment_securities",
    "cashflow_gain_loss_on_sale_of_business","cashflow_income_tax_paid_supplemental_data","cashflow_interest_paid_supplemental_data",
    "cashflow_investing_cash_flow","cashflow_issuance_of_debt","cashflow_long_term_debt_issuance","cashflow_long_term_debt_payments",
    "cashflow_net_business_purchase_and_sale","cashflow_net_common_stock_issuance","cashflow_net_income_from_continuing_operations",
    "cashflow_net_intangibles_purchase_and_sale","cashflow_net_investment_purchase_and_sale","cashflow_net_issuance_payments_of_debt",
    "cashflow_net_long_term_debt_issuance","cashflow_net_other_financing_charges","cashflow_net_other_investing_changes","cashflow_net_ppe_purchase_and_sale",
    "cashflow_net_short_term_debt_issuance","cashflow_operating_cash_flow","cashflow_operating_gains_losses","cashflow_other_non_cash_items",
    "cashflow_proceeds_from_stock_option_exercised","cashflow_provisionand_write_offof_assets","cashflow_purchase_of_business",
    "cashflow_purchase_of_intangibles","cashflow_purchase_of_investment","cashflow_purchase_of_ppe","cashflow_repayment_of_debt",
    "cashflow_repurchase_of_capital_stock","cashflow_sale_of_business","cashflow_sale_of_investment","cashflow_sale_of_ppe",
    "cashflow_short_term_debt_issuance","cashflow_short_term_debt_payments","cashflow_stock_based_compensation",
    "cashflow_unrealized_gain_loss_on_investment_securities","incomestatement_basic_average_shares","incomestatement_basic_eps",
    "incomestatement_cost_of_revenue","incomestatement_diluted_average_shares","incomestatement_diluted_eps",
    "incomestatement_diluted_ni_availto_com_stockholders","incomestatement_ebit","incomestatement_ebitda","incomestatement_gross_profit",
    "incomestatement_interest_expense","incomestatement_interest_expense_non_operating","incomestatement_interest_income",
    "incomestatement_interest_income_non_operating","incomestatement_net_income","incomestatement_net_income_common_stockholders",
    "incomestatement_net_income_continuous_operations","incomestatement_net_income_from_continuing_and_discontinued_ope",
    "incomestatement_net_income_from_continuing_operation_net_minori","incomestatement_net_income_including_noncontrolling_interests",
    "incomestatement_net_interest_income","incomestatement_net_non_operating_interest_income_expense","incomestatement_normalized_ebitda",
    "incomestatement_normalized_income","incomestatement_operating_expense","incomestatement_operating_income","incomestatement_operating_revenue",
    "incomestatement_other_income_expense","incomestatement_other_non_operating_income_expenses","incomestatement_pretax_income",
    "incomestatement_reconciled_cost_of_revenue","incomestatement_reconciled_depreciation","incomestatement_research_and_development",
    "incomestatement_selling_general_and_administration","incomestatement_tax_effect_of_unusual_items","incomestatement_tax_provision",
    "incomestatement_tax_rate_for_calcs","incomestatement_total_expenses","incomestatement_total_operating_income_as_reported","incomestatement_total_revenue"
]
