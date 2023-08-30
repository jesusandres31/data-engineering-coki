import csv

import psycopg2
from psycopg2 import sql

csv_dir = "/app/data"

csv_files = ["clientes.csv", "articulos.csv", "factura.csv", "facturaDetalle.csv"]

table_names = ["clientes", "articulos", "factura", "facturaDetalle"]


def load_csv(host, new_database, user, password):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=host, database=new_database, user=user, password=password
    )

    # Load CSV files
    cursor = conn.cursor()

    for i, csv_file in enumerate(csv_files):
        table_name = table_names[i]
        csv_path = f"{csv_dir}/{csv_file}"
        with open(csv_path, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip the first row (headers)
            for row in reader:
                # Create the INSERT query
                placeholders = ", ".join(["%s"] * len(row))
                query = sql.SQL(
                    "INSERT INTO {} VALUES ({}) ON CONFLICT DO NOTHING"
                ).format(sql.Identifier(table_name), sql.SQL(placeholders))
                cursor.execute(query, row)
                conn.commit()

    cursor.close()
    conn.close()

    print("CSV files successfully uploaded to tables!")
