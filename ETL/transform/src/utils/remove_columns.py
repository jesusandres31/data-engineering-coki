"""  
## CSV Column Removal Script

This script removes unnecessary columns from CSV files. 
It is designed to work with four CSV files: "Clientes.csv," "Factura.csv," "FacturaDetalle.csv," and "Articulos.csv." 
You can specify the columns to be removed for each file. 
"""

import csv 
import shutil

Factura_dir = "/app/datalake/Factura.csv"
FacturaDetalle_dir = "/app/datalake/FacturaDetalle.csv"
Articulos_dir = "/app/datalake/Articulos.csv"
Clientes_dir = "/app/datalake/Clientes.csv"
 
# List of columns to remove for each CSV file
columns_to_remove = {
    "Clientes": ["CUIT", "Cod_IVA", "LP", "Domicilio", "Cod_Localidad", "Cod_Provincia", "Telefono", "E_Mail", "SitioWeb", "Obs", "Fecha_Hora", "Usuario", "Linked", "Saldo", "Anticipo"],
    "Factura": ["TipoDoc", "IdFormaPago", "LP", "TipoIVA", "FechaHora", "Obs", "Saldo", "Usuario", "Recargo", "TotalCC", "Efectivo1", "Tarjeta1", "TotalC", "Recargo1", "TotalR", "Costo", "IdEle", "Reparto"],
    "FacturaDetalle": ["TipoDoc", "IdArt", "Deci", "NroFactura", "FechaVto", "Deuda", "Saldo", "Tipo", "FechaFactura", "Monto1", "TotalDoc", "NroDocDet", "TipoDocDet", "TipoDet", "Cobro"],
    "Articulos": ["IdArt", "IdRubro", "CodArtPro", "Descripcion2", "IdFamilia", "Minimo", "PC", "PG", "Obs", "FechaHora", "Usuario", "Linked", "IVA"]
}

def exec_remove_columns_from_csv(file_path, columns_to_remove):
    # Create a temporary file to store the modified content
    with open(file_path, "r") as input_file, open("temp.csv", "w", newline="") as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        header = next(csv_reader)
        new_header = [col for col in header if col not in columns_to_remove]
        csv_writer.writerow(new_header)  # Write the new header to the new file

        for row in csv_reader:
            # Filter out the columns to remove
            new_row = [row[header.index(col)] for col in header if col not in columns_to_remove]
            csv_writer.writerow(new_row)

    # Replace the original file with the modified content
    shutil.move("temp.csv", file_path)

def remove_columns():
    exec_remove_columns_from_csv(Clientes_dir, columns_to_remove["Clientes"])
    exec_remove_columns_from_csv(Factura_dir, columns_to_remove["Factura"])
    exec_remove_columns_from_csv(FacturaDetalle_dir, columns_to_remove["FacturaDetalle"])
    exec_remove_columns_from_csv(Articulos_dir, columns_to_remove["Articulos"])