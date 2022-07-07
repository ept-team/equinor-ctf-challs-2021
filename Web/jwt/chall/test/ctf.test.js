'use strict';

//Defining config
process.env.ZWAGGER_HOST = 'A';

const { test } = require('tap');
// var sinon = require('sinon');
var jwt = require('jsonwebtoken');
var __ = require('underscore');
const Crypto = require('crypto');

function generateRandomKey(size) {
    const key = Crypto.randomBytes(size).toString('base64').slice(0, size);
    return key;
}

test('There should be a revealing robots.txt file', async (t) => {
    const app = require('../src/app').build();

    const response = await app.inject({
        method: 'GET',
        url: '/robots.txt',
    });
    t.equal(response.statusCode, 200, 'returns a status code of 200');
    t.equal(
        response.headers['content-type'],
        'text/plain; charset=UTF-8',
        'of content type text/plain and charset UTF-8'
    );
    t.equal(response.body,'User-agent: *\nDisallow: /doc/','disallow for /doc where swagger lives');
    t.end();
});



test('Testing CTF logic to /api/quote', (t) => {
    // t.beforeEach(function (t) {});

    // t.afterEach(function (t) {});

    t.test('fail if no auhtorization header', async (t) => {
        
        const app = require('../src/app').build({
            logger: {
                level: 'debug',
                prettyPrint: {
                    colorize: true,
                    singleLine: true,
                },
                name: 'Test runner',
            }
        });
     
        const response = await app.inject({
            method: 'GET',
            url: '/api/quote',
        });

        t.equal(response.statusCode, 401, 'returns a status code of 401');
        t.equal(
            response.body,
            'Unauthorized - missing authentication',
            'with message - Unauthorized - missing authentication'
        );

    
        t.end();
    });

    t.test('fail if auhtorization header not is a JWT', async (t) => {
        const app = require('../src/app').build({
            logger: {
                level: 'debug',
                prettyPrint: {
                    colorize: true,
                    singleLine: true,
                },
                name: 'Test runner',
            },
        });

        const response = await app.inject({
            method: 'GET',
            url: '/api/quote',
            headers: {
                authorization: 'atoken'
            }
        });

        t.equal(response.statusCode, 400, 'returns a status code of 400');
        t.equal(
            response.body,
            'Unauthorized - bad request',
            'with message - Unauthorized - bad request'
        );

        t.end();
    });

    t.test('fail if JWt token does not contain valid scope', async (t) => {
        const app = require('../src/app').build({
            logger: {
                level: 'debug',
                prettyPrint: {
                    colorize: true,
                    singleLine: true,
                },
                name: 'Test runner',
            },
        });

        var token = jwt.sign(
            {
                exp: Math.floor(Date.now() / 1000) + (60 * 60),
            },
            generateRandomKey(32)
        );


        const response = await app.inject({
            method: 'GET',
            url: '/api/quote',
            headers: {
                authorization: 'Bearer ' + token,
            },
        });

        t.equal(response.statusCode, 401, 'returns a status code of 401');
        t.equal(
            response.body,
            'Unauthorized - missing scope to in token to read quotes',
            'with message - Unauthorized - missing scope to in token to read quotes'
        );

        t.end();
    });

    t.test('fail if JWT token scope is not quotes.read', async (t) => {
        const app = require('../src/app').build({
            logger: {
                level: 'debug',
                prettyPrint: {
                    colorize: true,
                    singleLine: true,
                },
                name: 'Test runner',
            },
        });

        var token = jwt.sign(
            {
                exp: Math.floor(Date.now() / 1000) + 60 * 60,
                scp: 'quotes.write',
                scope: 'quotes.write'
            },
            generateRandomKey(32)
        );

        const response = await app.inject({
            method: 'GET',
            url: '/api/quote',
            headers: {
                authorization: 'Bearer ' + token,
            },
        });

        t.equal(response.statusCode, 401, 'returns a status code of 401');
        t.equal(
            response.body,
            'Unauthorized - no quotes.read scope in token',
            'with message - Unauthorized - no quotes.read scope in token'
        );

        t.end();
    });

    t.test('fail if JWT token has no expire claim in token', async (t) => {
        const app = require('../src/app').build({
            logger: {
                level: 'debug',
                prettyPrint: {
                    colorize: true,
                    singleLine: true,
                },
                name: 'Test runner',
            },
        });

        var token = jwt.sign(
            {
                scp: 'quotes.read',
            },
            generateRandomKey(32)
        );

        const response = await app.inject({
            method: 'GET',
            url: '/api/quote',
            headers: {
                authorization: 'Bearer ' + token,
            },
        });

        t.equal(response.statusCode, 401, 'returns a status code of 401');
        t.equal(
            response.body,
            'Unauthorized - missing expire time in token',
            'with message - Unauthorized - missing expire time in token'
        );

        t.end();
    });

    
    t.test('fail if JWT token has expired', async (t) => {
        const app = require('../src/app').build({
            logger: {
                level: 'debug',
                prettyPrint: {
                    colorize: true,
                    singleLine: true,
                },
                name: 'Test runner',
            },
        });

        var token = jwt.sign(
            {
                scp: 'quotes.read',
                exp: Math.floor(Date.now() / 1000) - 10,
            },
            generateRandomKey(32)
        );

        const response = await app.inject({
            method: 'GET',
            url: '/api/quote',
            headers: {
                authorization: 'Bearer ' + token,
            },
        });

        t.equal(response.statusCode, 401, 'returns a status code of 401');
        t.equal(
            response.body,
            'Unauthorized - expired token',
            'with message - Unauthorized - expired token'
        );

        t.end();
    });

    t.test('fail if JWT token has lifetime more than 5 minutes', async (t) => {
        const app = require('../src/app').build({
            logger: {
                level: 'debug',
                prettyPrint: {
                    colorize: true,
                    singleLine: true,
                },
                name: 'Test runner',
            },
        });

        var token = jwt.sign(
            {
                scp: 'quotes.read',
                exp: Math.floor(Date.now() / 1000) + 5 * 60,
            },
            generateRandomKey(32)
        );

        const response = await app.inject({
            method: 'GET',
            url: '/api/quote',
            headers: {
                authorization: 'Bearer ' + token,
            },
        });

        t.equal(response.statusCode, 401, 'returns a status code of 401');
        t.equal(
            response.body,
            'Unauthorized - token max lifetime exceeded',
            'with message - Unauthorized - token max lifetime exceeded'
        );

        t.end();
    });


    t.test('issue a quote if JWT is validated with correct scp claim', async (t) => {
        const app = require('../src/app').build({
            logger: {
                level: 'debug',
                prettyPrint: {
                    colorize: true,
                    singleLine: true,
                },
                name: 'Test runner',
            },
        });

        var token = jwt.sign(
            {
                scp: 'quotes.read',
                exp: Math.floor(Date.now() / 1000) + 5 * 60 - 1,
            },
            generateRandomKey(32)
        );

        const response = await app.inject({
            method: 'GET',
            url: '/api/quote',
            headers: {
                authorization: 'Bearer ' + token,
            },
        });

        const body = JSON.parse(response.body);
        console.log(body);
        t.equal(response.statusCode, 200, 'returns a status code of 200');
        t.ok(!__.isUndefined(body.title),
            'response body contains a tile'
        );
        t.ok(
            !__.isEmpty(body.title),
            'flag is not empty'
        );

        t.end();
    });

    t.test('issue a quote if JWT is validated with corret scope claim', async (t) => {
        const app = require('../src/app').build({
            logger: {
                level: 'debug',
                prettyPrint: {
                    colorize: true,
                    singleLine: true,
                },
                name: 'Test runner',
            },
        });

        var token = jwt.sign(
            {
                scope: 'quotes.read',
                exp: Math.floor(Date.now() / 1000) + 5 * 60 - 1,
            },
            generateRandomKey(32)
        );

        const response = await app.inject({
            method: 'GET',
            url: '/api/quote',
            headers: {
                authorization: 'Bearer ' + token,
            },
        });

        const body = JSON.parse(response.body);
        console.log(body);
        t.equal(response.statusCode, 200, 'returns a status code of 200');
        t.ok(!__.isUndefined(body.title), 'response body contains a tile');
        t.ok(!__.isEmpty(body.title), 'flag is not empty');

        t.end();
    });



    t.end();
});