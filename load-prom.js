// Needs npm: enigma.js, ws

const enigma = require('enigma.js');
const schema = require('enigma.js/schemas/12.20.0.json');
const WebSocket = require('ws');

async function _run() {
  const session = enigma.create({
    url: 'ws://localhost:9076/app/',
    schema,
    createSocket: url => new WebSocket(url),
  });
  session.on('traffic:*', console.log);
  const global = await session.open();
  const doc = await global.createSessionApp();
  const connId = await doc.createConnection({
      qType: 'prometheus-connector',
      qName: 'prom',
      qConnectionString: 'CUSTOM CONNECT TO "provider=prometheus-connector;hostname=prom-connector"',
      qUserName: 'test',
      qPassword: 'test',
    });
    const script = `
//LOAD * FROM promdata.qvd;
LIB CONNECT TO "prom";
Buffer (Incremental) SQL *;
STORE * INTO promdata.qvd;
`;
    await doc.setScript(script);
    const reload = doc.doReload();
    await reload;
    const progress = await global.getProgress(reload.requestId);
    console.log(JSON.stringify(progress));
    const data = await doc.getTablesAndKeys({}, {}, 0, true, false);
    console.log(JSON.stringify(data));
    /*await Promise.all([
      doc.deleteConnection(connId),
      doc.setScript(''),
    ]);*/
    session.close();
}

async function run() {
    try {
      await _run();
    } catch(err) {
      console.log(err);
      process.exit(1);
    }
}

run();
