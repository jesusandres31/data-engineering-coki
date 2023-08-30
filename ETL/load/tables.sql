--
-- create table
--
CREATE TABLE IF NOT EXISTS "clientes" (
    "Cod_Cliente" TEXT PRIMARY KEY,
    "Razon_Social" TEXT,
    "CUIT" TEXT,
    "Cod_IVA" TEXT,
    "LP" NUMERIC,
    "Domicilio" TEXT,
    "Cod_Localidad" TEXT,
    "Cod_Provincia" TEXT,
    "Telefono" TEXT,
    "E_Mail" TEXT,
    "SitioWeb" TEXT,
    "Obs" TEXT,
    "Estado" NUMERIC,
    "Fecha_Hora" TIMESTAMP,
    "Usuario" NUMERIC,
    "Linked" NUMERIC,
    "Saldo" NUMERIC,
    "Anticipo" NUMERIC
);

CREATE TABLE IF NOT EXISTS "articulos" (
    "IdArt" TEXT PRIMARY KEY,
    "Codigo" TEXT,
    "IdRubro" TEXT,
    "UM" TEXT,
    "CodArtPro" TEXT,
    "Descripcion1" TEXT,
    "Descripcion2" TEXT,
    "IdFamilia" TEXT,
    "Actual" NUMERIC,
    "Minimo" NUMERIC,
    "PC" NUMERIC,
    "PG" NUMERIC,
    "Precio01" NUMERIC,
    "Precio02" NUMERIC,
    "Precio03" NUMERIC,
    "Obs" TEXT,
    "Estado" NUMERIC,
    "FechaHora" TIMESTAMP,
    "Usuario" NUMERIC,
    "Linked" NUMERIC,
    "IVA" NUMERIC
);            
      
CREATE TABLE IF NOT EXISTS "factura" (
    "IdFactura" TEXT PRIMARY KEY,
    "NroDoc" TEXT,
    "TipoDoc" TEXT,
    "FechaFactura" TIMESTAMP,
    "IdCliente" TEXT,
    "IdFormaPago" TEXT,
    "LP" NUMERIC,
    "TipoIVA" TEXT,
    "Total" NUMERIC,
    "FechaHora" TIMESTAMP,
    "Usuario" NUMERIC,
    "Estado" NUMERIC,
    "Obs" TEXT,
    "Saldo" NUMERIC,
    "Recargo" NUMERIC,
    "TotalCC" NUMERIC,
    "Efectivo1" NUMERIC,
    "Tarjeta1" NUMERIC,
    "TotalC" NUMERIC,
    "Recargo1" NUMERIC,
    "TotalR" NUMERIC,
    "Costo" NUMERIC,
    "IdEle" TEXT,
    "Reparto" NUMERIC
);
 
CREATE TABLE IF NOT EXISTS "facturaDetalle" (
    "IdFacturaDetalle" TEXT PRIMARY KEY,
    "NroDoc" TEXT,
    "TipoDoc" TEXT,
    "IdArt" TEXT,
    "Codigo" TEXT,
    "Descripcion" TEXT,
    "Bulto" NUMERIC,
    "Deci" TEXT,
    "UM" TEXT,
    "Cantidad" NUMERIC,
    "PU" NUMERIC,
    "Bonif" NUMERIC,
    "Importe" NUMERIC,
    "NroFactura" TEXT,
    "FechaVto" TEXT,
    "Deuda" NUMERIC,
    "Saldo" NUMERIC,
    "Tipo" TEXT,
    "FechaFactura" TEXT,
    "Monto1" NUMERIC,
    "TotalDoc" NUMERIC,
    "NroDocDet" TEXT,
    "TipoDocDet" TEXT,
    "TipoDet" TEXT,
    "Cobro" TEXT
);         

--
-- remove constraints
--
ALTER TABLE factura DROP CONSTRAINT IF EXISTS "factura-NroDoc";

ALTER TABLE "facturaDetalle" DROP CONSTRAINT IF EXISTS "facturaDetalle-factura";

ALTER TABLE articulos DROP CONSTRAINT IF EXISTS "articulos-Codigo";

ALTER TABLE "facturaDetalle" DROP CONSTRAINT IF EXISTS "facturaDetalle-articulos";

ALTER TABLE clientes DROP CONSTRAINT IF EXISTS "clientes-Cod_Cliente";

ALTER TABLE "factura" DROP CONSTRAINT IF EXISTS "factura-clientes";


--
-- create constraints
--
ALTER TABLE factura ADD CONSTRAINT "factura-NroDoc" UNIQUE ("NroDoc");

ALTER TABLE "facturaDetalle"  
    ADD CONSTRAINT "facturaDetalle-factura" 
    FOREIGN KEY ("NroDoc") 
    REFERENCES factura("NroDoc");

ALTER TABLE articulos ADD CONSTRAINT "articulos-Codigo" UNIQUE ("Codigo");
 
ALTER TABLE "facturaDetalle"  
    ADD CONSTRAINT "facturaDetalle-articulos" 
    FOREIGN KEY ("Codigo") 
    REFERENCES articulos("Codigo");

ALTER TABLE clientes ADD CONSTRAINT "clientes-Cod_Cliente" UNIQUE ("Cod_Cliente");

ALTER TABLE "factura"  
    ADD CONSTRAINT "factura-clientes" 
    FOREIGN KEY ("IdCliente") 
    REFERENCES clientes("Cod_Cliente");
