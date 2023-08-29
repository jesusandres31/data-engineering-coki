import os
import time

import psycopg2
from dotenv import load_dotenv
from utils.create_db import create_db
from utils.create_tables import create_tables

load_dotenv()

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


#
# Wait for the database to start up
#
max_attempts = 30
attempts = 0

while not is_database_available() and attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts}: Waiting for the database to become available...")
    time.sleep(2)

if attempts == max_attempts:
    print("Database didn't become available within the specified attempts.")
else:
    print("Database is now available! Proceeding with the scripts.")
    create_db(host, database, user, password, new_database)
    create_tables(host, new_database, user, password)
