import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas

USER      = "BEPRATHAP"
PASSWORD  = os.getenv("SNOW_PASSWORD")
ACCOUNT   = "yi43251.us-east-2.aws"
WAREHOUSE = "COMPUTE_WH"
DATABASE  = "PROD"
SCHEMA    = "DBT_RAW"
ROLE      = "ACCOUNTADMIN"

TITLES_CSV  = r"/Users/beprathap/workspace/netflix-dataset/netflix/datasets/titles.csv"
CREDITS_CSV = r"/Users/beprathap/workspace/netflix-dataset/netflix/datasets/credits.csv"

# Create Snowflake connection
def create_connection():
    conn = snow.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA,
        role=ROLE,
        ocsp_fail_open=True,
        insecure_mode=True,
    )
    print("SQL Connection Created")
    return conn

def truncate_tables(conn):
    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE IF EXISTS TITLES")
        cur.execute("TRUNCATE TABLE IF EXISTS CREDITS")
    print("Tables truncated")

def load_data(conn):
    titles_df  = pd.read_csv(TITLES_CSV)
    print("Titles file read")
    credits_df = pd.read_csv(CREDITS_CSV)
    print("Credits file read")

    write_pandas(conn, titles_df,  "TITLES",  auto_create_table=True)
    print("Titles file loaded")
    write_pandas(conn, credits_df, "CREDITS", auto_create_table=True)
    print("Credits file loaded")

def main():
    print("Starting Script")
    conn = None
    try:
        conn = create_connection()
        truncate_tables(conn)
        load_data(conn)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()