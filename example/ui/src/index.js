const picasso = require('picasso.js');
const picassoQ = require('picasso-plugin-q');

picasso.use(picassoQ);

const createSession = require('./session');
const createMemoryChart = require('./memory-chart');
const createSessionChart = require('./sessions-chart');

(async () => {
  const doc = await createSession(`ws://localhost:9076/app/${+new Date()}`);

  const memTitle = document.createElement('h1');
  memTitle.innerHTML = 'Memory (in bytes) per container';
  document.body.appendChild(memTitle);
  createMemoryChart(picasso, doc);

  const sessionTitle = document.createElement('h1');
  sessionTitle.innerHTML = 'Total number of sessions on engines';
  document.body.appendChild(sessionTitle);
  createSessionChart(picasso, doc);
})();
