CREATE TABLE IF NOT EXISTS "clientes" (
    "Cod_Cliente" TEXT PRIMARY KEY,
    "Razon_Social" TEXT NOT NULL,
    "CUIT" TEXT,
    "Cod_IVA" TEXT,
    "LP" INTEGER,
    "Domicilio" TEXT,
    "Cod_Localidad" TEXT,
    "Cod_Provincia" TEXT,
    "Telefono" TEXT,
    "E_Mail" TEXT,
    "SitioWeb" TEXT,
    "Obs" TEXT,
    "Estado" INTEGER,
    "Fecha_Hora" TIMESTAMP,
    "Usuario" INTEGER,
    "Linked" INTEGER,
    "Saldo" DECIMAL(10, 2),
    "Anticipo" DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS "articulos" (
    "IdArt" TEXT PRIMARY KEY,
    "Codigo" TEXT,
    "IdRubro" TEXT,
    "UM" TEXT,
    "CodArtPro" TEXT,
    "Descripcion1" TEXT NOT NULL,
    "Descripcion2" TEXT,
    "IdFamilia" TEXT,
    "Actual" INTEGER,
    "Minimo" INTEGER,
    "PC" INTEGER,
    "PG" INTEGER,
    "Precio01" DECIMAL(10, 2),
    "Precio02" DECIMAL(10, 2),
    "Precio03" DECIMAL(10, 2),
    "Obs" TEXT,
    "Estado" INTEGER,
    "FechaHora" TIMESTAMP,
    "Usuario" INTEGER,
    "Linked" INTEGER,
    "IVA" DECIMAL(5, 2)
);            
      
CREATE TABLE IF NOT EXISTS "factura" (
    "IdFactura" SERIAL PRIMARY KEY,
    "NroDoc" TEXT NOT NULL,
    "TipoDoc" TEXT,
    "FechaFactura" TIMESTAMP NOT NULL,
    "IdCliente" TEXT NOT NULL,
    "IdFormaPago" TEXT,
    "LP" INTEGER,
    "TipoIVA" TEXT,
    "Total" DECIMAL(10, 2),
    "FechaHora" TIMESTAMP,
    "Usuario" INTEGER,
    "Estado" INTEGER,
    "Obs" TEXT,
    "Saldo" DECIMAL(10, 2),
    "Recargo" DECIMAL(10, 2),
    "TotalCC" DECIMAL(10, 2),
    "Efectivo1" DECIMAL(10, 2),
    "Tarjeta1" DECIMAL(10, 2),
    "TotalC" DECIMAL(10, 2),
    "Recargo1" DECIMAL(10, 2),
    "TotalR" DECIMAL(10, 2),
    "Costo" DECIMAL(10, 2),
    "IdEle" INTEGER,
    "Reparto" INTEGER,
    FOREIGN KEY ("IdCliente") REFERENCES "clientes" ("Cod_Cliente")
);
 
CREATE TABLE IF NOT EXISTS "facturaDetalle" (
    "IdFacturaDetalle" SERIAL PRIMARY KEY,
    "NroDoc" TEXT NOT NULL,
    "TipoDoc" TEXT,
    "IdArt" TEXT,
    "Codigo" TEXT,
    "Descripcion" TEXT,
    "Bulto" INTEGER,
    "Deci" TEXT,
    "UM" TEXT,
    "Cantidad" INTEGER,
    "PU" DECIMAL(10, 2),
    "Bonif" DECIMAL(10, 2),
    "Importe" DECIMAL(10, 2),
    "NroFactura" TEXT,
    "FechaVto" TIMESTAMP,
    "Deuda" DECIMAL(10, 2),
    "Saldo" DECIMAL(10, 2),
    "Tipo" TEXT,
    "FechaFactura" TIMESTAMP,
    "Monto1" DECIMAL(10, 2),
    "TotalDoc" DECIMAL(10, 2),
    "NroDocDet" INTEGER,
    "TipoDocDet" TEXT,
    "TipoDet" TEXT,
    "Cobro" TEXT,
    FOREIGN KEY ("NroDoc") REFERENCES "factura" ("NroDoc"),
    FOREIGN KEY ("IdArt") REFERENCES "articulos" ("IdArt")
);         

CREATE TABLE IF NOT EXISTS "unidadMedida" (
    "IdUM" TEXT PRIMARY KEY,
    "UM" TEXT,
    "Decimales" INTEGER,
    "Obs" TEXT,
    "Estado" INTEGER,
    "FechaHora" TIMESTAMP,
    "Usuario" INTEGER,
    "Linked" INTEGER
);

--
-- relationships: 
-- not needed for now
--

