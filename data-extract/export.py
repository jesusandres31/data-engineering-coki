import subprocess

# Specify the tables to extract
tables = ['Clientes', 'Articulos', 'Factura', 'FacturaDetalle'] 

# Extract each table as a CSV file
for table in tables:
    # Prepare the command
    mdb_export_command = f'mdb-export /app/db/base.mdb {table}'

    print(mdb_export_command)

    # Execute the command and capture the output
    process = subprocess.Popen(mdb_export_command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()

    # Prepare the CSV file path
    csv_file = f'/app/output/{table}.csv'

    # Write the output to the CSV file
    with open(csv_file, 'w') as file:
        file.write(output.decode('utf-8'))

    print(f'{table} exported to {csv_file}')