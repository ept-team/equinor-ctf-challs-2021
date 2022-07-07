
import { DB } from "https://deno.land/x/sqlite/mod.ts";

export class TokenStorage {
  private database: DB;

  constructor(file: string) {
    this.database = new DB(file);
    this.database.query("CREATE TABLE IF NOT EXISTS tokens (token TEXT, scope TEXT, expiry DATETIME)");
  }
  public purgeExpiredTokens = () => {
    this.database.query("DELETE FROM tokens where expiry < datetime('now')");
  };
  public dumpTokens = () => {
    for (const [token, scope, expiry] of this.database.query("SELECT token,scope,expiry FROM tokens")) {
      console.log(`${token} ,${scope}, ${expiry}`);
    }
  };
  public checkToken = (token: string) => {
    const res = this.database.query(
      "SELECT count(token) FROM tokens where token == (?) AND scope == 'protected.read' AND expiry > datetime('now')",
      [token],
    )[0][0] as number;
    console.log(res);
    return res;
  };
  public insertToken = (token: string, scope: string, expiry: string) => {
    this.database.query(
      "INSERT INTO tokens (token,scope,expiry) VALUES (?,?,datetime('now',?))",
      [token, scope, expiry],
    );
  };
}