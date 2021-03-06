'use strict';

const { logger } = require('../lib/logger.js');
const fastify = require('fastify');
const rateLimitAllowList = require('../lib/app-config').rateLimitAllowList();
const maxRateLimit = require('../lib/app-config').maxRateLimit();
// const port = require('../lib/app-config').port;
const zwaggerHost = require('../lib/app-config').zwaggerHost;
const pkg = require('../package.json');
const path = require('path');

function build(opts= {}) {

    const app = fastify(opts);

    logger.info('Initial api server plumbing');

    //Installing support for CORS headers
    app.register(require('fastify-cors'),{
        origin: '*',
    });

    //Registering a api rate limiter
    app.register(require('fastify-rate-limit'), {
        max: maxRateLimit,
        timeWindow: '1 minute',
        ban: 2,
        allowList: rateLimitAllowList,
        errorResponseBuilder: function (request, context) {
            logger.error('Hitting rate limit');
            return {
                code: 429,
                error: 'Too Many Requests',
                message: `The GOT Api only allow ${context.max} requests per ${context.after}. Try again soon.`,
                date: Date.now(),
                expiresIn: context.ttl,
            };
            // reply.code(429).send('Rate limit');
        },
    });

    //Register static path
    app.register(require('fastify-static'), {
        root: path.join(__dirname, '../public'),
        list: false,
    });

    //Adding swagger documentation
    app.register(require('fastify-swagger'), {
        routePrefix: '/doc',
        swagger: {
            info: {
                title: 'GOT Quotes Api',
                description: 'Serving Gorge RR Quotes from GOT',
                version: pkg.version,
            },
            externalDocs: {
                url: 'https://swagger.io',
                description: 'Find more info here',
            },
            host: zwaggerHost,
            schemes: ['http','https'],
            consumes: ['application/json'],
            produces: ['application/json'],
            tags: [
                { name: 'api/quote', description: 'Get random quote' }
            ],
            securityDefinitions: {
                Bearer: {
                    type: 'apiKey',
                    name: 'Authorization:',
                    in: 'header'
                },
            },
        },
        uiConfig: {
            docExpansion: 'list',
            deepLinking: false,
        },
        staticCSP: true,
        transformStaticCSP: (header) => header,
        exposeRoute: true,
    });



    //Declare a root route
    app.get('/', function (req, reply) {

        const welcomeMessage = 'The Game of Thrones Random Quote Api ('+pkg.version+') \n\n8 hours of guessing, fuzzing and brute force can save you 5 minutes of reading the doc';

        reply.send(welcomeMessage);
    });

    //Register routes
    const quoteRoutes = require('../routes/quotes');
    quoteRoutes.forEach((route) => {
        app.route(route);
    });

    return app;

} //build

module.exports = {build};