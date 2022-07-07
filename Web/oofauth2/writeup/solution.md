# OofAuth2 Writeup

Endpoints for **OAuth2 Authorization Code Grant** has been implemented but not connected.
The steps involved to retrieve the important data behind the protected resource has to be figured out. All info is provided in the notes after logging in as `developer`.


1. Create `/authorize` URL to the authorization server. Correct scope and PKCE parameter **code_challenge** is needed

``` 
https://oofauth2.io.ept.gg/authorize?response_type=code&client_id=backend&redirect_uri=https%3A%2F%2Foofauth2.io.ept.gg%2Fcallback&state=X1GCu7df&scope=protected.read&code_challenge=%2F7Xhgu%2FKCXiIr9wVu6wFx7jbvIC7lqBePRn9wrNMFVU%3D&code_challenge_method=S256
``` 


2. The authorization server will show an approval page, and if approved by the user, it will redirect to the callback API with `code` & `state` as URL parameters. Callback will be dumped.

`-> GET /callback, code : -8.XpXgAohqo, state: X1GCu7df`

3. To use the authorization code to get an accesstoken through the `/token` endpoint, a POST need to be crafted in addition to basic authentication with `client_id:client_secret`. PKCE now need `code_verifier` to be provided.

```
curl 'https://oofauth2.io.ept.gg/token' -X POST -H 'Authorization: Basic YmFja2VuZDpkcm93c3NhcGdub2xkZXNyZXZlcg==' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'grant_type=authorization_code&code=RECEIVED_CODE_GOES_HERE&redirect_uri=https%3A%2F%2Foofauth2.io.ept.gg%2Fcallback&code_verifier=NoSuFCBzJqsciB7YlSkIf6OozKaQL7i49ceFrBCzdciofZTiOkbVtGj7Az8n8rSa&client_id=backend'
```
 
`
-> {"access_token":"3r0fTSzPDk0O23BQhyz3xSc3","token_type":"Bearer","expires_in":600}
`

4. Use the issued accesstoken to get info behind the `/protected` endpoint.

```sh
   curl -H 'Authorization: Bearer 3r0fTSzPDk0O23BQhyz3xSc3' https://oofauth2.io.ept.gg/protected
``` 

5. Use the info to login as admin and get the flag.



## RFCs: (OAuth & PKCE)
[rfc6749 section-4.1 - OAuth2](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1)<br>
[rfc7636 section-4.2 - PKCE](https://datatracker.ietf.org/doc/html/rfc7636#section-4.2)  
[rfc6750 section-2.1 - Bearer token](https://datatracker.ietf.org/doc/html/rfc6750#section-2.1)
