import { readFileSync } from "fs";
import MDBReader from "mdb-reader";

const buffer = readFileSync("db/base.mdb");
const reader = new MDBReader(buffer);

console.log(reader.getTableNames());

const table = reader.getTable("Articulos");
console.log(table.getColumnNames());

console.log(table.getData());
