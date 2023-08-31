import os
import time

import psycopg2
from dotenv import load_dotenv
from utils.create_db import create_db
from utils.create_tables import create_tables
from utils.load_csv import load_csv

load_dotenv()

start_time = time.time()

# Retrieve environment variables
host = os.environ.get("DB_HOST")
database = os.environ.get("DB_NAME")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
new_database = os.environ.get("NEW_DB_NAME")


# Define a function to check database availability
def is_database_available():
    try:
        conn = psycopg2.connect(
            host=host, dbname=database, user=user, password=password
        )
        conn.close()
        return True
    except psycopg2.OperationalError:
        return False


# Wait for the database to start up
max_attempts = 30
attempts = 0

while not is_database_available() and attempts < max_attempts:
    attempts += 1
    print(
        f"Attempt {attempts}: Waiting for the database to become available...",
        flush=True,
    )
    time.sleep(2)

if attempts == max_attempts:
    print("Database didn't become available within the specified attempts.", flush=True)
else:
    print("Database is now available! Proceeding with the scripts.", flush=True)
    print("About to create database...", flush=True)
    create_db(host, database, user, password, new_database)
    print("About to create tables...", flush=True)
    create_tables(host, new_database, user, password)
    print("About to load data...", flush=True)
    load_csv(host, new_database, user, password)


# Display time
end_time = time.time()
execution_time_seconds = end_time - start_time
execution_minutes = int(execution_time_seconds // 60)
execution_seconds = int(execution_time_seconds % 60)
print(
    f"Script execution completed in {execution_minutes} minutes and {execution_seconds} seconds.",
    flush=True,
)
