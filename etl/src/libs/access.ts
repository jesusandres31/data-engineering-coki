import ADODB from 'node-adodb';
import config from '../config';

const access = ADODB.open(
  `Provider=Microsoft.Jet.OLEDB.4.0;Data Source=${config.dbPath};`,
);

export default access;
