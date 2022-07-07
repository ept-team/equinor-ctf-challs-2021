//Routine to generate JWT token for testing

var jwt = require('jsonwebtoken');
const Crypto = require('crypto');

function generateRandomKey(size) {
    const key = Crypto.randomBytes(size).toString('base64').slice(0, size);
    return key;
}


var token = jwt.sign({
    exp: Math.floor(Date.now() / 1000) + (60 * 5) - 1,
    // scp: 'quotes.read',
    scope: 'quotes.read'
},
generateRandomKey(32));

var decoded_token = jwt.decode(token, { complete: true });

console.log(token);
console.log(decoded_token);