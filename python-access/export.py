import subprocess

# Tablas que deseas exportar
tables = ['clientes', 'articulos', 'factura', 'facturaDetalle']

# Exportar cada tabla a un archivo CSV
for table in tables:
    subprocess.call(['mdb-export', 'path_to_your_base.mdb', table, '>', f'{table}.csv'])
    print(f'{table} exportado a {table}.csv')