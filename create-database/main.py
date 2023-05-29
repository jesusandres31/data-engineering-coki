import os
import psycopg2
import time

# Wait for the database to start up
# time.sleep(10) 

# Retrieve environment variables
host = os.environ.get("DB_HOST")
database = os.environ.get("DB_NAME")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
new_database = os.environ.get("NEW_DB_NAME")

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

# Check if the new_database database exists
cursor = conn.cursor()
cursor.execute(f'SELECT 1 FROM pg_catalog.pg_database WHERE datname = \'{new_database}\'')
exists = cursor.fetchone()

if not exists:
    # Create the new_database database
    cursor.execute(f'CREATE DATABASE {new_database};')
    print(f'Created {new_database} database.')
else:
    print(f'{new_database} database already exists.')

conn.commit()
cursor.close()
conn.close()

# Connect to the new_database
conn = psycopg2.connect(
    host=host,
    database=new_database,
    user=user,
    password=password 
)

# Execute SQL commands from a file
cursor = conn.cursor()
sql_file = "./tables.sql" 

with open(sql_file, "r") as file:
    cursor.execute(file.read())

conn.commit()

cursor.close()
conn.close()
