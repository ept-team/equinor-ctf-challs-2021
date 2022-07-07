'use strict';

const { logger } = require('../lib/logger.js');
const port = require('../lib/app-config').port;

const loglevel = require('../lib/logger.js').loglevel().server;

logger.info('Server loglevel: ' + loglevel);

//Instansiating server using fastify, passing the fastify config object as param.
const server = require('../src/app').build({
    logger: {
        level: loglevel,
        prettyPrint: {
            colorize: true,
            singleLine: true,
        },
        name: 'Quote Server',
    },
    port: port,
});

server.listen(port, '0.0.0.0', (err, address) => {
    if (err) {
        server.log.error(err);
        process.exit(1);
    }
    server.log.info(`server listening on ${address}`);
});
