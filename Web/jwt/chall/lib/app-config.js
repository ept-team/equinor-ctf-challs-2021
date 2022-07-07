'use strict';

const logger = require('./logger.js').logger;

// Configuration Objects
logger.info('Building configuration');

// const tenantId = process.env.TENANT_ID;
const port = (process.env.PORT || '3000' );

const zwaggerHost = (process.env.ZWAGGER_HOST || ('localhost:' + port));

logger.info('Zwagger host set to ' + zwaggerHost);

const rateLimitAllowList = function () {
    return ['127.0.0.1'];
};

const maxRateLimit = function () {
    return 100;
};

function isConfigOk() {
    
  
    return true;

}

function exitHandler() {
    process.exit(1);
}

//Checking config and exiting app if not ok
//The exit is a bit brutal - but no need for a more controlled exit as this stage
logger.info('Verifying configuration');

if (!isConfigOk()) {
    logger.error('Invalid configuration - exiting in full panic mode');
    exitHandler();
}

module.exports = {
    port,
    rateLimitAllowList,
    maxRateLimit,
    zwaggerHost
};

