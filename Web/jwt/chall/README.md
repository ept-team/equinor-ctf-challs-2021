# jwt ctf challenge

A few puzzles to solve, a few security issues to discuss

## The system

There is an API which uses a JWT token to authenticate. To get the flag you need to create a valid JWT, iterating over error messages to figure out token claims.

The Zwagger endpoint could be used to iterate (/doc) where the essence is to input "Bearer" + JWT token in the authorization header. The /robots.txt files contains a reference to /doc.

### Flaws that are explored

- No signature validation - any jwt token will be parsed
- No audience validation
- No issuer validation
- No nbf (not before validation)
- Too much revealing information in error messages
- Not using framework for validation
- And most likely a few more :)

### Capturing the flag

The flag and GOT Quotes are exposed if the api is called with a valid JWT token

Token is validated ok if it:
- is a JWT token
- contains scp = "quotes.read" or scope = "quotes.read" i payload claim (case sensitive)
- expired dated for token not has passed (payload "exp" claim)
- max token lifetime is less than 5 minutes (payload "iat" - "exp" claim)

API has ratelimiting activated (expect for localhost)

## The code

The procect is coded in NodeJs. 

Commands:
* **npm start** (run application)
* **npm test** (run tests)
* **npm run dev** (run application in dev mode - nodemon with restart)
* **npm run wtest** (run application in test dev mode - watch with re-runs)
* **npm run lint** (lint the code)
* **npm run docker:build** (build a docker image called ctf - includes testing)
* **npm run docker:run** (run the build docker container)
* **npm run docker:save** (export the docker image to a tar.gz file)
  
## Run the code


```shell
npm start
```
or
```shell
npm run docker:run
```

### Config

The following environment variables are used:

* **PORT** (defines the port where the app listen, default 3000)
* **NODE_ENV** (nodejs environment - development or production )
* **ZWAGGER_HOST** (Defines the url for zwagger queries, default is localhost:3000)


## Requirements

* Docker &| NodeJs
