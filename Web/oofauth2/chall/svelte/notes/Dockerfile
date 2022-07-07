# -- Base node image
#
FROM node:alpine3.14 AS base
WORKDIR /usr/src/app
COPY package.json pnpm-lock.yaml index.html svelte.config.js vite.config.js ./
RUN mkdir -p ./src
COPY src src

# -- Svelte & Node
#
FROM base as dependencies
WORKDIR /usr/src/app
RUN npm i -g pnpm && pnpm i && pnpm build

# Release image
#
FROM dependencies as release
WORKDIR /usr/src/app
COPY --from=dependencies /usr/src/app/dist ./dist
RUN addgroup -S -g 1001 ctf-non-root-group && adduser -S -u 1001 -G ctf-non-root-group ctf-non-root-user
EXPOSE 5000
USER 1001
ENTRYPOINT [ "pnpm", "serve"]
