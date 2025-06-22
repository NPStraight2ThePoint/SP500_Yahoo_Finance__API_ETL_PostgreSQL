import os
import glob
import psycopg2
from psycopg2 import sql
from utils import DB_CONFIG_1, PRICING_DIR, PRICING_TABLE, ROOT_DIR

def load_csv_to_postgres(file_path, conn, PRICING_TABLE):
    with conn.cursor() as cur:
        with open(file_path, 'r', encoding='utf-8') as f:
            copy_query = sql.SQL("""
                COPY {table} (date, ticker, open, high, low, close, adj_close, volume, dividends, stock_splits)
                FROM STDIN WITH CSV HEADER DELIMITER ','
            """).format(table=sql.Identifier(*PRICING_TABLE.replace('"', '').split('.')))
            cur.copy_expert(copy_query, f)
        conn.commit()
    print(f"✅ Loaded {os.path.basename(file_path)}")

def main():
    conn = psycopg2.connect(**DB_CONFIG_1)
    try:
        csv_files = glob.glob(os.path.join(PRICING_DIR, '*.csv'))
        print("CSV Files Found:", csv_files)
        for file_path in csv_files:
            try:
                load_csv_to_postgres(file_path, conn, PRICING_TABLE)
            except Exception as e:
                print(f"❌ Failed to load {os.path.basename(file_path)}: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    main()
