import psycopg2
from psycopg2 import sql
from datetime import date
from utils import INDICATORS_TABLE, DB_CONFIG_1, INDICATORS_CSV_PATH

def connect_db(dbname, user, password, host='localhost', port=5432):
    """Create and return a new PostgreSQL database connection."""
    return psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

def load_csv_to_postgres(csv_path, conn, table_name):
    """
    Load CSV data into PostgreSQL table using COPY command.

    Args:
        csv_path (str): Path to the CSV file.
        conn (psycopg2.connection): Active database connection.
        table_name (str): Target table with optional schema (e.g. public."table").
    """
    copy_sql = sql.SQL("""
        COPY {table}
        FROM STDIN WITH CSV HEADER DELIMITER ','
    """).format(table=sql.Identifier(*table_name.replace('"', '').split('.')))

    with conn.cursor() as cur, open(csv_path, 'r', encoding='utf-8') as f:
        cur.copy_expert(copy_sql, f)
    conn.commit()
    print(f"✅ Loaded CSV data into {table_name}")

def main():
    today = date.today().strftime("%Y-%m-%d")

    conn = connect_db(**DB_CONFIG_1)
    try:
        load_csv_to_postgres(INDICATORS_CSV_PATH, conn, INDICATORS_TABLE)
    except Exception as e:
        print(f"❌ Failed to load CSV: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
