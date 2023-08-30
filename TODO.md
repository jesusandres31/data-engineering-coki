load-database-1 | 2023-08-30 21:12:42.524 UTC [31] STATEMENT: INSERT INTO "facturaDetalle" VALUES ('46175', '00007000', 'FAC', '', '2000', 'TOMATE TRITURADO EN LATA X 8 K LADOMI', '1.0000', '', 'Uni', '1.0000', '70.0000', '0.0000', '70.0000', '', '', '0.0000', '0.0000', '', '', '0.0000', '0.0000', '', '', '', '') ON CONFLICT DO NOTHING
load-app-1 | Traceback (most recent call last):
load-app-1 | File "/app/main.py", line 55, in <module>
load-app-1 | load_csv(host, new_database, user, password)
load-app-1 | File "/app/utils/load_csv.py", line 34, in load_csv
load-app-1 | cursor.execute(query, row)
load-app-1 | psycopg2.errors.ForeignKeyViolation: insert or update on table "facturaDetalle" violates foreign key constraint "facturaDetalle-articulos"
load-app-1 | DETAIL: Key (Codigo)=(2000) is not present in table "articulos".
load-app-1 |

###

power bi

airflow
