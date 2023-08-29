"""
CSV Column Transformation Script
This script reads two CSV files: UnidadMedida.csv and Articulos.csv. 
It replaces the IdUM column in the Articulos.csv file with the corresponding Unit of Measure (UM) text from the UnidadMedida.csv file. 
The modified content is then written back to the Articulos.csv file, overwriting the original data.
"""

import csv
import shutil
import tempfile

UnidadMedida_dir = "/app/datalake/UnidadMedida.csv"
Articulos_dir = "/app/datalake/Articulos.csv"


def transform_um():
    # Create a dictionary to map IdUM to UM text
    um_mapping = {}

    with open(UnidadMedida_dir, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            um_id = row[0]
            um_text = row[1]
            um_mapping[um_id] = um_text

    # Create a temporary file to store the modified content of Articulos.csv
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        with open(Articulos_dir, "r") as archivo:
            csv_reader = csv.reader(archivo)
            header = next(csv_reader)
            header[3] = "UM"  # Rename the IdUM column header
            csv_writer = csv.writer(temp_file)
            csv_writer.writerow(header)

            # Iterate through each row in Articulos.csv and replace IdUM with corresponding UM text
            for fila in csv_reader:
                id_um = fila[3]  # Index of IdUM column
                if id_um in um_mapping:
                    fila[3] = um_mapping[id_um]
                csv_writer.writerow(fila)

    # Replace the original file with the modified content
    shutil.move(temp_file.name, Articulos_dir)
