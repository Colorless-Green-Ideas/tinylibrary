FROM node
MAINTAINER Jack Laxson <jack@getpizza.cat>

RUN npm install --global rollup

RUN mkdir -p /usr/src/tinylibrary
WORKDIR /usr/src/tinylibrary