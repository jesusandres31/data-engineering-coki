"""
Fix data inconsistencies in CSV files.

The change from product code "5" to "755" in FacturaDetalle.csv is being made because it appears that 
at some point the product identifier was changed, resulting in an inconsistency. 
However, both product code "5" and "755" refer to the same product, 
and this change aims to ensure uniformity and accuracy in the data.

The same happened with product code "41" and "455".
"""

import csv
import shutil
import tempfile

FacturaDetalle_dir = "/app/datalake/FacturaDetalle.csv"


def transform_cod():
    # Fix FacturaDetalle.csv
    with open(FacturaDetalle_dir, "r") as archivo:
        csv_reader = csv.reader(archivo)
        header = next(csv_reader)
        new_rows = [header]

        for fila in csv_reader:
            codigo = fila[4]  # Index of Codigo column
            if codigo == "5":
                fila[4] = "755"  # Change "5" to "755"
            if codigo == "41":
                fila[4] = "455"  # Change "5" to "755"
            new_rows.append(fila)

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        csv_writer = csv.writer(temp_file)
        csv_writer.writerows(new_rows)

    shutil.move(temp_file.name, FacturaDetalle_dir)
