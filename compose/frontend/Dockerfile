FROM node:16-alpine

WORKDIR /app

COPY ./frontend/package*.json ./

RUN npm install

COPY ./frontend .

ENTRYPOINT ["npm", "start"]