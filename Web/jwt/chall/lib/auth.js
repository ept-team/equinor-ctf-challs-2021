'use strict';

var jwt = require('jsonwebtoken');
var __ = require('underscore');
const { logger } = require('../lib/logger.js');

//Adding auth validator
async function authVerify(request, reply) {

    var tokenArray = [];

    logger.info(
        'Authenticating request for API ' + request.method + ' ' + request.url);

    //Verify if request contains an authorization header
    if (request.headers.authorization) {
        tokenArray = request.headers.authorization.split(' ');
    } else {
        logger.error('No Auth header in request');
        return reply.code(401).send('Unauthorized - missing authentication');
    }

    //Decoding token
    var decodedToken = jwt.decode(tokenArray[1], { complete: true });
    // var token = tokenArray[1];


    logger.debug(decodedToken);

    // We should have a JWT token
    if (__.isNull(decodedToken)) {
        logger.error('Unable to decode token: ' + tokenArray[1]);
        return reply.code(400).send('Unauthorized - bad request');
    }


    // Token should have valid scope
    //hasOwnProperty is case sensitive
    if (
        !((decodedToken.payload.hasOwnProperty('scp')) || 
          (decodedToken.payload.hasOwnProperty('scope'))) ) {
        logger.error('Missing scope in token');
        return reply.code(401).send('Unauthorized - missing scope to in token to read quotes');
    } else {
        if (
            !(decodedToken.payload.scp == 'quotes.read' ||
              decodedToken.payload.scope == 'quotes.read')
        ) {
            logger.error('Wrong scope in token');
            return reply
                .code(401)
                .send('Unauthorized - no quotes.read scope in token');
        }
    }

    // Token should have expire date which not is passed
    if (!decodedToken.payload.hasOwnProperty('exp')) {
        logger.error('Missing expire time in token');
        return reply.code(401).send('Unauthorized - missing expire time in token');
    } else {
              
        var dateNow = new Date();
        if (decodedToken.payload.exp * 1000 < dateNow.getTime()) {
            logger.error('Token has expired');
            return reply.code(401).send('Unauthorized - expired token');
        }
    }


    // Max token lifetime should be less than 5 minutes
    if (!decodedToken.payload.hasOwnProperty('iat')) {
        logger.error('Missing issue at time in token');
        return reply.code(401).send('Unauthorized - missing issued at time in token');
    } else {

        if (!((decodedToken.payload.exp - decodedToken.payload.iat) < (5 * 60))) {
            logger.error('Token max lifetime exceeded');
            return reply
                .code(401)
                .send('Unauthorized - token max lifetime exceeded');
        }
    }

}

module.exports = {authVerify};