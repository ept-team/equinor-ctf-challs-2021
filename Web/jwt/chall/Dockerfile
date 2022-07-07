# -- Base node image with quote api
#
FROM node:alpine3.14 AS base
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN mkdir -p ./controller ./data ./lib ./routes ./src ./publicnp
COPY controller controller
COPY data data
COPY lib lib
COPY routes routes
COPY src src
COPY public public


#
# -- Dependencies
#
FROM base as dependencies
WORKDIR /usr/src/app
RUN npm install --only=production
RUN cp -R node_modules node_modules_production
RUN npm install

#
# Running test and linting
#
# The Copying of the LICENSE file is just a hack to
# create a dependency between the test and the releasd stage
# and make the build process act like a CI pipeline

FROM dependencies as test
WORKDIR /usr/src/app
#Preparing and runnig tests
COPY test test
COPY LICENSE LICENSE
RUN npm test
#Preparing and running linting
COPY .eslintrc.json .eslintignore ./
RUN npm run lint
#Running vulnerability check for dependencies
RUN npm audit --production --audit-level=high
# #Running Snyk
# ARG SNYK_TOKEN
# RUN npm run snyk

#
# Release image
#
FROM base as release
WORKDIR /usr/src/app
COPY --from=dependencies /usr/src/app/node_modules_production ./node_modules
COPY --from=test /usr/src/app/LICENSE .
RUN addgroup -S -g 1001 ctf-non-root-group
RUN adduser -S -u 1001 -G ctf-non-root-group ctf-non-root-user
EXPOSE 3000
USER 1001
ENTRYPOINT [ "npm", "start"]