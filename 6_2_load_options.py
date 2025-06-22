import os
import glob
import psycopg2
import pandas as pd
from io import StringIO
from utils import DB_CONFIG_2, OPTIONS_TABLE, OPTIONS_DIR

# List integer columns in your options_chains table
int_columns = [
    "volume", "openInterest"
    # add other integer columns here if any
]

# List boolean columns in your options_chains table
bool_columns = [
    "inTheMoney"
    # add others if you have
]

def connect_db():
    return psycopg2.connect(**DB_CONFIG_2)

def clean_integer_columns(df, int_cols):
    for col in int_cols:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: int(float(x)) if pd.notnull(x) else None)
    return df

def clean_boolean_columns(df, bool_cols):
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].map({
                'TRUE': True, 'True': True, True: True, 1: True, 1.0: True,
                'FALSE': False, 'False': False, False: False, 0: False, 0.0: False
            }).astype('boolean')
    return df

def load_csv_copy(file_path, conn, table_name):
    df = pd.read_csv(file_path)

    df = clean_integer_columns(df, int_columns)
    df = clean_boolean_columns(df, bool_columns)

    # Convert DataFrame back to CSV string in memory
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    with conn.cursor() as cur:
        cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", csv_buffer)
    conn.commit()

def main():

    csv_files = glob.glob(os.path.join(OPTIONS_DIR, "*.csv"))

    conn = connect_db()

    for file_path in csv_files:
        try:
            load_csv_copy(file_path, conn, OPTIONS_TABLE)
            print(f"✅ Loaded {os.path.basename(file_path)}")
        except Exception as e:
            print(f"❌ Failed to load {os.path.basename(file_path)}: {e}")

    conn.close()

if __name__ == "__main__":
    main()