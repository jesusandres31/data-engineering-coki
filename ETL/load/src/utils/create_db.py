import psycopg2


def create_db(host, database, user, password, new_database):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)

    # Check if the new_database database exists
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{new_database}'"
    )
    exists = cursor.fetchone()

    if not exists:
        cursor.close()
        conn.close()

        # Create a new connection without a transaction
        conn_new = psycopg2.connect(
            host=host, user=user, password=password, dbname=database
        )
        conn_new.autocommit = True  # Set autocommit to True
        cursor_new = conn_new.cursor()

        # Create the new_database database
        cursor_new.execute(f"CREATE DATABASE {new_database}")
        print(f"Created {new_database} database.")

        cursor_new.close()
        conn_new.close()
    else:
        print(f"{new_database} database already exists.")

    cursor.close()
    conn.close()
