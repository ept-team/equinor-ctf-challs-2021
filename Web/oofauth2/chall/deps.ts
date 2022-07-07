import { Session  } from "https://deno.land/x/oak_sessions@v3.1.2/mod.ts";
import { config as dotEnvConfig } from "https://deno.land/x/dotenv@v3.0.0/mod.ts";
import {
  Application,
  Context,
  Router,
  send 
} from "https://deno.land/x/oak@v9.0.0/mod.ts";
import { createHash } from "https://deno.land/std@0.110.0/hash/mod.ts";
import { cryptoRandomString } from "https://deno.land/x/crypto_random_string@1.1.0/mod.ts";

import {
  parseToken,
  processAccessTokenRequest,
  processAuthorizeRequest,
  processClientAuthentication,
  processAuthorizationResponse,
  URLAuthorizeResponse,
} from "https://raw.githubusercontent.com/steinsiv/oauth2-dance/main/mod.ts";

import type {
  OAuth2ClientOptions,
  AccessTokenResponseOptions,
  AuthorizationRequestOptions,
  AuthorizationResponseOptions,
} from "https://raw.githubusercontent.com/steinsiv/oauth2-dance/main/mod.ts";

export {
  Session,
  parseToken,
  dotEnvConfig,
  Application,
  Context,
  Router,
  send,
  createHash,
  cryptoRandomString,
  processAccessTokenRequest,
  processAuthorizeRequest,
  processAuthorizationResponse,
  processClientAuthentication,
  URLAuthorizeResponse,
};
export type {
  OAuth2ClientOptions,
  AccessTokenResponseOptions,
  AuthorizationRequestOptions,
  AuthorizationResponseOptions,      
};