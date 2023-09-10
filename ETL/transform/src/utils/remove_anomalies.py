"""
Remove Anomalous Values Greater Than 100 and Address Data Inconsistencies.

This script reads a CSV file named "FacturaDetalle.csv" and removes records 
where the "Cantidad" column has values greater than or equal to 100, 
as these values are considered anomalies and should be excluded for data quality.
"""

import csv
import shutil
import tempfile

FacturaDetalle_dir = "/app/datalake/FacturaDetalle.csv"


def remove_anomalies():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        csv_writer = csv.writer(temp_file)

        with open(FacturaDetalle_dir, "r") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            csv_writer.writerow(header)  # Write the header to the new file

            for row in csv_reader:
                cantidad = float(row[9])
                if cantidad < 100:  # keep okly rows where Cantidad < 100
                    csv_writer.writerow(row)

        shutil.move(temp_file.name, FacturaDetalle_dir)
