  import { Application, 
  Context, 
  cryptoRandomString, 
  dotEnvConfig, 
  OAuth2ClientOptions, Router , processAuthorizationResponse, Session, send,   parseToken, AuthorizationRequestOptions, processAuthorizeRequest, AuthorizationResponseOptions, URLAuthorizeResponse, processClientAuthentication, processAccessTokenRequest, AccessTokenResponseOptions,} from "../deps.ts";
  import { TokenStorage } from "./tokenstorage.ts";

  const db = new TokenStorage("tokens.db");

  const env = dotEnvConfig();
  console.log(dotEnvConfig({}));

const protectedData = { data: "admin:oauth2inthemaking" };
type AccessTokenItem =  AccessTokenResponseOptions & { scope: string | undefined };

const developer = { username: "developer", password: "repolevedmai" }

  const client: OAuth2ClientOptions = {
    clientId: env.DENO_CLIENT_ID,
    clientSecret: env.DENO_CLIENT_SECRET,
    clientRedirectURIs: [env.DENO_CLIENT_REDIRECT_URL],
    scope: "protected.read",
    state: cryptoRandomString({ length: 8, type: "url-safe" }),
    codeVerifier: "N/A",
    codeChallenge: "N/A",
  };

// Backend for 3 servers.   Client - Authorization Server - Protected resource

  console.log(client);
  const app = new Application();
  const session = new Session(); 
  const port = 3000;
  const router = new Router();

  router.get("/", session.initMiddleware(), async (ctx: Context) => {    
    const sessVal = await ctx.state.session.has("loggedin");
    if (sessVal && await ctx.state.session.get("loggedin")) {
      await ctx.response.redirect("/notes/index.html");
    } else {
      await ctx.response.redirect("/login/index.html");
    }
    
  });
  
  // Just dump searchparams we get in callback URL
  router.get("/callback", async (ctx: Context) => {
    const response = await processAuthorizationResponse(ctx.request.url, client.state);
    if (response) {
      ctx.response.status = 200;
      ctx.response.body = `${ctx.request.url.searchParams}\n`;
      ctx.response.body +=  `-> GET /callback, code : ${response?.code}, state: ${response?.state}`;
    } else {
      ctx.response.status = 400;
      ctx.response.body = `<pre>${ctx.request.url.searchParams}</pre>`;
    }
  });

  router.post("/logon", session.initMiddleware(), async (ctx: Context) => {
    const body = ctx.request.body();
    await body.value;
    if (body.type === "form") {
      const params: URLSearchParams = await body.value;
      const username = params.get("username");
      const password = params.get("password");
      const credsOk = username === developer.username && password === developer.password;
      await ctx.state.session.set("loggedin", credsOk);
      if (credsOk) {
        ctx.response.redirect('/notes/index.html')
      } else {
        ctx.response.status = 401;
      }    
    } else {
      ctx.response.status = 401;
    }
  });

  router.get('/logout', session.initMiddleware(),  async (ctx: Context) => {
    await session.deleteSession(ctx);
    ctx.response.redirect('/')
  });

    // ============ SERVER CODE HERE FOR NOW
  router.get("/protected", (ctx: Context) => {
    db.dumpTokens();
    ctx.response.headers.append("Content-Type", "application/json");
    const authorization = parseToken(ctx);
    if (authorization.scheme === "Bearer" && authorization.token && db.checkToken(authorization.token)) {
      ctx.response.status = 200;
      ctx.response.body = protectedData;
    } else {
      ctx.response.status = 401;
      ctx.response.body = { error: "unauthorized_client" };
    }
  });
  // ============ PROTECTED RESOURCE SERVERs CODE HERE FOR NOW

  // static serve
  router.get("/notes/:path+", session.initMiddleware(), async (ctx: Context) => { 
    if (!await ctx.state.session.has("loggedin") && !await ctx.state.session.get("loggedin")) {
      ctx.response.redirect("/login/index.html");
    } else {
      await send(ctx, ctx.request.url.pathname, { root: `${Deno.cwd()}/svelte/dist` }); 
    }
  });

  router.get("/login/:path+", async (ctx: Context) => { 
    await send(ctx, ctx.request.url.pathname, { root: `${Deno.cwd()}/svelte/dist` }); 
  });


// ============ AUTHORIZATION SERVERs CODE HERE FOR NOW
const codeCache: Map<string, AuthorizationRequestOptions> = new Map();
const requestCache: Map<string, AuthorizationRequestOptions> = new Map();

const basepath = "https://oofauth2.io.ept.gg";



const clients: OAuth2ClientOptions[] = [{
  clientId: env.DENO_CLIENT_ID,
  clientSecret: env.DENO_CLIENT_SECRET,  
  clientRedirectURIs: [ "https://oofauth2.io.ept.gg/callback"],
  scope: "protected.read",
  state: "N/A",
  codeVerifier: "N/A",
  codeChallenge: "N/A", 
}];

//console.log(clients);

router.get("/authorize", (ctx: Context) => {
  const authorizeRequest = processAuthorizeRequest(ctx, clients);
  if (!authorizeRequest) return;

  // Store parsed request until consent OR TTL expires (@todo)
  const requestIdentifier: string = cryptoRandomString({ length: 12, type: "alphanumeric"  });
  requestCache.set( requestIdentifier, authorizeRequest );

    const writeout = `
    <html><body>
        <h1>Authorize this client and scope?</h1>
        <form method="post" action="${basepath}/approve">
          <input type="hidden" name="reqid" value="${requestIdentifier}">
          <p>${ctx.request.url.search}</p>
          <pre>response_type        : ${authorizeRequest.responseType}</pre>
          <pre>client               : ${authorizeRequest.clientId}</pre>
          <pre>scope                : ${authorizeRequest.scope}</pre>
          <pre>state                : ${authorizeRequest.state}</pre>
          <pre>code_challenge       : ${authorizeRequest.codeChallenge}</pre>
          <pre>code_challenge_method: ${authorizeRequest.codeChallengeMethod}</pre>
          <pre>redirect_uri         : ${authorizeRequest.redirectURI}</pre>
          <input type="submit" target="top" value="Sure!"></input>
        </form>
    </body></html>`;

  ctx.response.body = writeout;
});

router.post("/approve", async (ctx) => {
  
  if (!ctx.request.hasBody || ctx.request.body().type !== "form") {
    return;
  } else {
    const body = ctx.request.body();
    const params: URLSearchParams = await body.value;
    const reqid = params.get("reqid") || "N/A";

    // Pull out original request
    const query = requestCache.get( reqid);

    if (query) {
      const code: string = cryptoRandomString({ length: 12, type: "url-safe" });
      const state = query.state;
      const responseOptions: AuthorizationResponseOptions = { code: code, state: state };
      const UrlAuthorize = URLAuthorizeResponse( query.redirectURI, responseOptions);

      codeCache.set(code, query); // Store decision
      requestCache.delete(reqid); // 🔥 burn reqid

      ctx.response.redirect(UrlAuthorize);
    } else {
      ctx.response.status = 400;
      ctx.response.type = "application/json";
      ctx.response.body = { error: "" }
    }
  }
});

router.post("/token", async (ctx: Context) => {
  const clientAuthenticated = await processClientAuthentication(ctx, clients);
  if (!clientAuthenticated || !ctx.request.hasBody) return;

  const requestOptions = await processAccessTokenRequest(ctx, clientAuthenticated, codeCache);
  if (!requestOptions) return;


  // Issue tokens
  const accessToken: AccessTokenItem = {
    access_token: cryptoRandomString({ length: 24, type: "alphanumeric" }),
    token_type: "Bearer",
    expires_in: 600,
    scope: codeCache.get(requestOptions.code)?.scope
  };

  requestOptions ? codeCache.delete(requestOptions.code) : {}; // 🔥 burn used code

  // @todo store token(s) for resource introspection queries, RFC7662
  db.insertToken(accessToken.access_token, accessToken.scope || "", "+10 minute");
  db.purgeExpiredTokens();
  //db.dumpTokens();
  ctx.response.status = 200;
  ctx.response.headers.append("Content-Type", "application/json");
  ctx.response.body = accessToken;
});

  // =====================================
  app.use(router.allowedMethods({ throw: true }));
  app.use(router.routes());
  app.use(async (ctx, next) => {
    await next();
    console.log(`${ctx.request.method} ${ctx.request.url}`);
  });

  
  //app.addEventListener("error", err => { console.log(err); });
  app.listen({ port: port });
    
  console.info(`Client Listening on :${port}`);
