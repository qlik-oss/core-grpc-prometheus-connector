const enigma = require('enigma.js');
const schema = require('enigma.js/schemas/12.20.0.json');

async function reloadLoop(global, doc) {
  const reload = doc.doReload();
  await reload;
  const progress = await global.getProgress(reload.requestId);
  console.log(JSON.stringify(progress));
  setTimeout(() => reloadLoop(global, doc), 10000);
}

async function createSession(url) {
  const session = enigma.create({ url, schema });
  // session.on('traffic:*', console.log);
  const global = await session.open();
  const doc = await global.createSessionApp();

  await Promise.all([
    doc.createConnection({
      qType: 'prometheus-connector',
      qName: 'prom',
      qConnectionString: 'CUSTOM CONNECT TO "provider=prometheus-connector;hostname=prom-connector"',
      qUserName: 'test',
      qPassword: 'test',
    }),
    doc.createConnection({
      qType: 'folder',
      qName: 'tmp',
      qConnectionString: '/tmp/',
    }),
  ]);

  const script = `
Prometheus_Data:
LIB CONNECT TO "prom";
SQL *;
CONCATENATE LOAD * FROM [lib://tmp/promdata.qvd](qvd);

STORE Prometheus_Data INTO [lib://tmp/promdata.qvd](qvd);
  `;

  await doc.setScript(script);
  reloadLoop(global, doc);
  return doc;
}


module.exports = createSession;
