"""
## CSV Column Denormalize Script

This script denormalizes a CSV file by replacing numeric values in a specific column with their corresponding text labels.
The script is designed to work with multiple CSV files that contain a column named "Estado" with values of 1 or 2, 
which represent "ACTIVE" and "INACTIVE" states, respectively.
"""

import csv 
import shutil

Factura_dir = "/app/datalake/Factura.csv"
Articulos_dir = "/app/datalake/Articulos.csv"
Clientes_dir = "/app/datalake/Clientes.csv"

def exec_denormalize_state(file_path):
    # Define a mapping for values 1 and 2
    state_mapping = {"1": "ACTIVE", "2": "INACTIVE"}

    # Create a temporary file to store the modified content
    with open(file_path, "r") as input_file, open("temp.csv", "w", newline="") as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        header = next(csv_reader)
        csv_writer.writerow(header)  # Write the header to the new file

        for row in csv_reader:
            # Replace the value in the "Estado" column
            if row[header.index("Estado")] in state_mapping:
                row[header.index("Estado")] = state_mapping[row[header.index("Estado")]]
            csv_writer.writerow(row)

    # Replace the original file with the modified content
    shutil.move("temp.csv", file_path)

def denormalize_state(): 
    exec_denormalize_state(Factura_dir)  
    exec_denormalize_state(Articulos_dir)  
    exec_denormalize_state(Clientes_dir)
