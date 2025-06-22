import os
import glob
import pandas as pd
import psycopg2
from utils import DB_CONFIG_1, FINANCIALS_DIR, FINANCIALS_A_TABLE, FINANCIALS_Q_TABLE, financial_statements_columns

os.makedirs(FINANCIALS_DIR, exist_ok=True)

# --- Helpers ---
def transpose_financial_csv(file_path: str, ticker: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df_long = df.melt(id_vars=["Statement", "index"], var_name="Date", value_name="Value")
    df_long.rename(columns={"index": "Metric"}, inplace=True)
    df_long["MetricLabel"] = df_long["Statement"].str.replace(" ", "") + "_" + df_long["Metric"].str.replace(" ", "_")
    df_pivot = df_long.pivot(index="Date", columns="MetricLabel", values="Value").reset_index()
    df_pivot.insert(0, "Ticker", ticker)
    return df_pivot

def truncate_pg_identifier(name: str) -> str:
    return name[:63]

def process_and_load(suffix: str, table_name: str):
    print(f"\n🔄 Processing {suffix} files for table: {table_name}")
    pattern = f"*_Financial_statements_{suffix}_*.csv"
    all_files = glob.glob(os.path.join(FINANCIALS_DIR, pattern))
    all_transposed = []

    for file_path in all_files:
        ticker = os.path.basename(file_path).split("_")[0]
        try:
            df_trans = transpose_financial_csv(file_path, ticker)
            all_transposed.append(df_trans)
            print(f"✅ Transposed {ticker}")
        except Exception as e:
            print(f"❌ Failed for {ticker}: {e}")

    if not all_transposed:
        print(f"⚠️ No data for {suffix}")
        return

    df_final = pd.concat(all_transposed, ignore_index=True)

    # Truncate headers
    df_final.columns = [truncate_pg_identifier(col) for col in df_final.columns]
    output_csv = os.path.join(FINANCIALS_DIR, f"SP500_Financials_Transposed_Truncated_{suffix}.csv")

    # df_final = df_final.loc[:, df_final.columns.isin(financial_statements_columns)]
    df_final.to_csv(output_csv, index=False)

    print(f"📁 CSV saved to {output_csv}")

    # Load to PostgreSQL
    try:
        with psycopg2.connect(**DB_CONFIG_1) as conn:
            with conn.cursor() as cur:
                print(f"🧹 Truncating {table_name}...")
                cur.execute(f'TRUNCATE TABLE {table_name};')

                print(f"📥 Loading into {table_name}...")
                with open(output_csv, 'r', encoding='utf-8') as f:
                    next(f)  # skip header
                    cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", f)

        print(f"✅ Data loaded into {table_name}")
    except Exception as e:
        print(f"❌ Failed to load into {table_name}: {e}")

# --- Run for both Annual (A) and Quarterly (Q) ---
process_and_load("A", FINANCIALS_A_TABLE)
process_and_load("Q", FINANCIALS_Q_TABLE)
