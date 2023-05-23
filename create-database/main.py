import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="tu_usuario",
    password="tu_contraseña"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE zini_system;")
conn.commit()
cursor.close()
conn.close()

conn = psycopg2.connect(
    host="localhost",
    database="zini_system",
    user="tu_usuario",
    password="tu_contraseña"
)

cursor = conn.cursor()
sql_file = "./tables.sql" 

with open(sql_file, "r") as file:
    cursor.execute(file.read())

conn.commit()

cursor.close()
conn.close()
