import os
import snowflake.connector
from flask import Flask, render_template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app
app = Flask(__name__)

# Snowflake connection details
ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
USER = os.getenv('SNOWFLAKE_USER')
PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')
DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')

# Route to execute the Snowflake query
@app.route('/')
def execute_query():
    error_message = None
    try:
        # Connect to Snowflake
        conn = snowflake.connector.connect(
            account=ACCOUNT,
            user=USER,
            password=PASSWORD,
            warehouse=WAREHOUSE,
            database=DATABASE,
            schema=SCHEMA
        )
        
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
        success_message = f"Table '{table_name}' created successfully!"
        print(success_message)

    except Exception as e:
        error_message = f"Error: {e}"
        print(error_message)

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
    
    # Render the error message on a webpage
    return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
