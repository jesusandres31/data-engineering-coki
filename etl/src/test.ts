import { open } from 'node-adodb';
import { Client } from 'pg';
import 'dotenv/config';

/**
 * config
 */
const config = {
  dbPath: process.env.ACCES_DB_PATH || '',
  host: process.env.PG_HOST || '',
  user: process.env.PG_USER || '',
  password: process.env.PG_PSSWD || '',
  database: process.env.PG_DB_NAME || '',
};

/* const pgClient = new Client({
  host: config.host,
  user: config.user,
  password: config.password,
  database: config.database,
}); */

const accessDB = open(
  `Provider=Microsoft.ACE.OLEDB.12.0;
   Data Source=${config.dbPath};
   Persist Security Info=False;`,
);

/**
 * main
 */
(async function main() {
  try {
    /* await pgClient.connect(); */
    console.log('Conectado a PostgreSQL');

    const tablesToTransfer = [
      'clientes',
      'articulos',
      'factura',
      'facturaDetalle',
    ];

    for (const tableName of tablesToTransfer) {
      console.log(`Procesando tabla: ${tableName}`);

      // Crear tabla en PostgreSQL
      /* await createTableInPostgreSQL(tableName); */

      // Leer datos de MS Access
      const records = await readDataFromAccessDB(tableName);
      console.log(records);

      // Insertar datos en PostgreSQL
      /* await insertDataIntoPostgreSQL(tableName, records); */

      console.log(`Tabla procesada: ${tableName}`);
    }
  } catch (error) {
    console.error('Error:', error);
  } finally {
    /* await pgClient.end(); */
    console.log('Desconectado de PostgreSQL');
  }
})();

/**
 *
 */
async function readDataFromAccessDB(tableName: string) {
  const query = `SELECT * FROM ${tableName}`;
  const records = await accessDB.query(query);
  return records;
}
/* async function readDataFromAccessDB(tableName: string, batchSize = 1000) {
  const primaryKeyColumns = {
    clientes: 'Cod_Cliente',
    articulos: 'IdArt',
    factura: 'IdFactura',
    facturaDetalle: 'IdFacturaDetalle',
  };

  const primaryKeyColumn = (primaryKeyColumns as any)[tableName];
  if (!primaryKeyColumn) {
    throw new Error(
      `No se encontró la columna de clave primaria para la tabla: ${tableName}`,
    );
  }

  let records: any = [];
  let hasMore = true;
  let lastPrimaryKey = null;

  while (hasMore) {
    let query = `SELECT TOP ${batchSize} * FROM ${tableName}`;

    if (lastPrimaryKey) {
      query += ` WHERE ${primaryKeyColumn} > '${lastPrimaryKey}'`; // Cambia esto
    }

    query += ` ORDER BY ${primaryKeyColumn} ASC`;

    const batch: any = await accessDB.query(query);
    if (batch.length > 0) {
      records = records.concat(batch);
      lastPrimaryKey = batch[batch.length - 1][primaryKeyColumn];
    } else {
      hasMore = false;
    }
  }

  return records;
} */

/**
 *
 */
async function insertDataIntoPostgreSQL(tableName: string, records: any[]) {
  const columnNames = Object.keys(records[0]);

  for (const record of records) {
    const values = Object.values(record).map(value => {
      if (typeof value === 'string') {
        return `'${value.replace(/'/g, "''")}'`;
      }
      if (value instanceof Date) {
        return `'${value.toISOString()}'`;
      }
      if (value === null) {
        return 'NULL';
      }
      return value;
    });

    const insertQuery = `
            INSERT INTO "${tableName}" (${columnNames
      .map(name => `"${name}"`)
      .join(', ')})
            VALUES (${values.join(', ')})
          `;

    try {
      /* await pgClient.query(insertQuery); */
    } catch (error) {
      console.error(
        `Error al insertar el registro en la tabla "${tableName}":`,
        record,
        error,
      );
    }
  }
}

/**
 *
 */
async function createTableInPostgreSQL(tableName: string) {
  let createTableQuery = '';

  switch (tableName) {
    case 'clientes':
      createTableQuery = `
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
            `;
      break;

    case 'articulos':
      createTableQuery = `
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
            `;
      break;

    case 'factura':
      createTableQuery = `
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
                `;
      break;

    case 'facturaDetalle':
      createTableQuery = `
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
                `;
      break;

    default:
      throw new Error(`Tabla desconocida: ${tableName}`);
  }

  /* await pgClient.query(createTableQuery); */
}
