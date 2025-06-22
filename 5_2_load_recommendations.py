import os
import glob
import pandas as pd
from datetime import date, timedelta
import psycopg2
from utils import DB_CONFIG_2, RECOMMENDATIONS_DIR, RECOMMENDATIONS_TABLE

# --- Date mapping ---
today = date.today()
date_mapping = {
    "0m": today,
    "-1m": today - timedelta(days=30),
    "-2m": today - timedelta(days=60),
    "-3m": today - timedelta(days=90),
}

# --- Process CSV files ---
all_files = glob.glob(os.path.join(RECOMMENDATIONS_DIR, "*.csv"))

for file in all_files:
    try:
        filename = os.path.basename(file)
        ticker = filename.split("recommendations_")[0]  # 'AAPLrecommendations_2025-01-14.csv' → 'AAPL'

        # Read CSV
        df = pd.read_csv(file)

        # Insert Ticker column
        df.insert(0, "Ticker", ticker)

        # Replace period with actual date
        df["period"] = df["period"].map(date_mapping)

        # Save transformed CSV (overwrite)
        df.to_csv(file, index=False)
        print(f"✅ Transformed and saved: {ticker}")

        # Load into PostgreSQL
        conn = psycopg2.connect(**DB_CONFIG_2)
        cursor = conn.cursor()

        # Optional: truncate table or append — here we append
        for _, row in df.iterrows():
            cursor.execute(
                f"""
                INSERT INTO {RECOMMENDATIONS_TABLE} (ticker, date, strongbuy, buy, hold, sell, strongsell)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    row["Ticker"],
                    row["period"],
                    row["strongBuy"],
                    row["buy"],
                    row["hold"],
                    row["sell"],
                    row["strongSell"],
                ),
            )
        conn.commit()
        cursor.close()
        conn.close()
        print(f"📥 Loaded into DB: {ticker}")

    except Exception as e:
        print(f"❌ Failed for {file}: {e}")
