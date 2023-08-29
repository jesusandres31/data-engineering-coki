import psycopg2


def create_tables(host, new_database, user, password):
    # Connect to the new_database
    conn = psycopg2.connect(
        host=host, database=new_database, user=user, password=password
    )

    # Execute SQL commands from a file
    cursor = conn.cursor()
    sql_file = "./tables.sql"

    with open(sql_file, "r") as file:
        cursor.execute(file.read())

    conn.commit()

    cursor.close()
    conn.close()

    print("SQL statement executed successfully!")
