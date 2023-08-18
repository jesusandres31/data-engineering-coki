CREATE TABLE IF NOT EXISTS "clientes" (
    "Cod_Cliente" VARCHAR(255) PRIMARY KEY,
    "Razon_Social" VARCHAR(255) NOT NULL,
    "CUIT" VARCHAR(14),
    "Cod_IVA" VARCHAR(255),
    "LP" INTEGER,
    "Domicilio" VARCHAR(255),
    "Cod_Localidad" VARCHAR(255),
    "Cod_Provincia" VARCHAR(255),
    "Telefono" VARCHAR(255),
    "E_Mail" VARCHAR(255),
    "SitioWeb" VARCHAR(255),
    "Obs" TEXT,
    "Estado" INTEGER,
    "Fecha_Hora" TIMESTAMP,
    "Usuario" INTEGER,
    "Linked" INTEGER,
    "Saldo" DECIMAL(10, 2),
    "Anticipo" DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS "articulos" (
    "IdArt" VARCHAR(255) PRIMARY KEY,
    "Codigo" VARCHAR(255),
    "IdRubro" VARCHAR(255),
    "IdUM" VARCHAR(255),
    "CodArtPro" VARCHAR(255),
    "Descripcion1" VARCHAR(255) NOT NULL,
    "Descripcion2" VARCHAR(255),
    "IdFamilia" VARCHAR(255),
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
    "NroDoc" VARCHAR(255) NOT NULL,
    "TipoDoc" VARCHAR(255),
    "FechaFactura" TIMESTAMP NOT NULL,
    "IdCliente" VARCHAR(255) NOT NULL,
    "IdFormaPago" VARCHAR(255),
    "LP" INTEGER,
    "TipoIVA" VARCHAR(255),
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
    "NroDoc" VARCHAR(255) NOT NULL,
    "TipoDoc" VARCHAR(255),
    "IdArt" VARCHAR(255),
    "Codigo" VARCHAR(255),
    "Descripcion" VARCHAR(255),
    "Bulto" INTEGER,
    "Deci" VARCHAR(255),
    "UM" VARCHAR(255),
    "Cantidad" INTEGER,
    "PU" DECIMAL(10, 2),
    "Bonif" DECIMAL(10, 2),
    "Importe" DECIMAL(10, 2),
    "NroFactura" VARCHAR(255),
    "FechaVto" TIMESTAMP,
    "Deuda" DECIMAL(10, 2),
    "Saldo" DECIMAL(10, 2),
    "Tipo" VARCHAR(255),
    "FechaFactura" TIMESTAMP,
    "Monto1" DECIMAL(10, 2),
    "TotalDoc" DECIMAL(10, 2),
    "NroDocDet" INTEGER,
    "TipoDocDet" VARCHAR(255),
    "TipoDet" VARCHAR(255),
    "Cobro" VARCHAR(255),
    FOREIGN KEY ("NroDoc") REFERENCES "factura" ("NroDoc"),
    FOREIGN KEY ("IdArt") REFERENCES "articulos" ("IdArt")
);         

CREATE TABLE IF NOT EXISTS "unidadMedida" (
    "IdUM" VARCHAR(255) PRIMARY KEY,
    "UM" VARCHAR(255),
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

