import os
import snowflake.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Snowflake connection details
ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
USER = os.getenv('SNOWFLAKE_USER')
PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')
DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')

# Connect to Snowflake
conn = snowflake.connector.connect(
    account=ACCOUNT,
    user=USER,
    password=PASSWORD,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
)

try:
    # Create a cursor
    cur = conn.cursor()

    # Table creation SQL statement
    table_name = 'sample_table'
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT,
        name STRING,
        age INT,
        created_at TIMESTAMP
    )
    """
    # Execute the query
    cur.execute(create_table_query)
    print(f"Table '{table_name}' created successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    cur.close()
    conn.close()
