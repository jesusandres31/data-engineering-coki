import { access } from './libs';
import { IProduct } from './types';

const main = async () => {
  const articulos: any[] = await access.query(
    `SELECT *
    FROM Articulos
    WHERE IdArt = 000001;`,
  );
  console.log(articulos[0]);

  const clientes: any[] = await access.query(
    `SELECT *
    FROM Clientes
    WHERE IdCliente = 000143;`,
  );
  console.log(clientes[0]);

  const factura: any[] = await access.query(
    `SELECT *
    FROM Factura
    WHERE IdFactura = 1;`,
  );
  console.log(factura[0]);

  const facturaDetalle: any[] = await access.query(
    `SELECT *
    FROM FacturaDetalle
    WHERE IdFacturaDetalle = 1;`,
  );
  console.log(facturaDetalle[0]);
};

main();
