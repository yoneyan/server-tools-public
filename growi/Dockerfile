FROM node:18
WORKDIR /opt

RUN apt update && \
    apt install -y curl git python make g++ wget openssl

RUN git clone https://github.com/weseek/growi -b v6.1.8 growi

WORKDIR /opt/growi

RUN npx lerna bootstrap

RUN yarn app:build

RUN apt remove -y curl git python make g++ wget openssl

COPY docker-entrypoint.sh .
RUN chmod 700 docker-entrypoint.sh

EXPOSE 3000

CMD ["yarn", "app:server"]
