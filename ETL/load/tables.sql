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
-- create constraints
--
DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.constraint_column_usage WHERE constraint_name = 'factura-nro-doc') THEN
        ALTER TABLE factura ADD CONSTRAINT "factura-nro-doc" UNIQUE ("NroDoc");
    END IF;
END $$;

DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.table_constraints WHERE constraint_name = 'factura_detalle-factura') THEN
        ALTER TABLE "facturaDetalle"
        ADD CONSTRAINT "factura_detalle-factura"
        FOREIGN KEY ("NroDoc")
        REFERENCES factura("NroDoc");
    END IF;
END $$;

DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.constraint_column_usage WHERE constraint_name = 'articulos-codigo') THEN
        ALTER TABLE articulos ADD CONSTRAINT "articulos-codigo" UNIQUE ("Codigo");
    END IF;
END $$;

DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.table_constraints WHERE constraint_name = 'factura_detalle-articulos') THEN
        ALTER TABLE "facturaDetalle"  
        ADD CONSTRAINT "factura_detalle-articulos" 
        FOREIGN KEY ("Codigo") 
        REFERENCES articulos("Codigo");
    END IF;
END $$;

DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.constraint_column_usage WHERE constraint_name = 'clientes-cod-cliente') THEN
        ALTER TABLE clientes ADD CONSTRAINT "clientes-cod-cliente" UNIQUE ("Cod_Cliente");
    END IF;
END $$;

DO $$ BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.table_constraints WHERE constraint_name = 'factura-clientes') THEN
        ALTER TABLE "factura"  
        ADD CONSTRAINT "factura-clientes" 
        FOREIGN KEY ("IdCliente") 
        REFERENCES clientes("Cod_Cliente");
    END IF;
END $$;







 