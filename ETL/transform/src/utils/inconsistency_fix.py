"""
## Inconsistency Fix Script for CSV Data

This script performs data consistency fixes on two CSV files: FacturaDetalle.csv and Articulos.csv.

### Articulos.csv Fixes:
- Leading zeros are removed from the Codigo column, resulting in a cleaner representation of the data.

### FacturaDetalle.csv Fixes:
- Leading zeros are removed from the Codigo column, improving the consistency and readability of the data.

After processing, the script writes the modified content back to their respective files, overwriting the original data.

**Note:** This script assumes that the CSV files maintain a consistent structure, and the column indices mentioned in the script correspond to the appropriate columns in the files. If the CSV file structure differs, adjustments to the script's column indices may be necessary.
"""

import csv
import shutil
import tempfile

FacturaDetalle_dir = "/app/datalake/FacturaDetalle.csv"
Articulos_dir = "/app/datalake/Articulos.csv"


def inconsistency_fix():
    # Fix Articulos.csv
    with open(Articulos_dir, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        new_rows = [header]

        for fila in csv_reader:
            codigo = fila[1]  # Index of Codigo column
            codigo = codigo.lstrip("0")  # Remove leading zeros
            fila[1] = codigo  # Update Codigo column
            new_rows.append(fila)

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        csv_writer = csv.writer(temp_file)
        csv_writer.writerows(new_rows)

    shutil.move(temp_file.name, Articulos_dir)

    # Fix FacturaDetalle.csv
    with open(FacturaDetalle_dir, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        new_rows = [header]

        for fila in csv_reader:
            codigo = fila[4]  # Index of Codigo column
            codigo = codigo.lstrip("0")  # Remove leading zeros
            fila[4] = codigo  # Update Codigo column
            new_rows.append(fila)

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        csv_writer = csv.writer(temp_file)
        csv_writer.writerows(new_rows)

    shutil.move(temp_file.name, FacturaDetalle_dir)
