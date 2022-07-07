FROM node:16-alpine3.14 as node
WORKDIR /app
COPY . .
WORKDIR /app/svelte/login
RUN npm i -g pnpm && pnpm i && pnpm build
WORKDIR /app/svelte/notes
RUN npm i -g pnpm && pnpm i && pnpm build


FROM denoland/deno:alpine as deno
WORKDIR /app
COPY ./src ./src
COPY .env deps.ts deno.json ./
# Copy compiled svelte js
RUN mkdir -p /app/svelte/dist
COPY --from=node /app/svelte/dist /app/svelte/dist
RUN deno cache -r deps.ts

FROM deno as deploy
WORKDIR /app

EXPOSE 3000

ENTRYPOINT ["deno", "run", "--allow-net", "--allow-env", "--allow-read", "--allow-write", "/app/src/backend.ts"]
