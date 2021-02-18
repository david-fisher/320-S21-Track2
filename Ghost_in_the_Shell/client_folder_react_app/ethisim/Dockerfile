FROM node:12.18.4-alpine
WORKDIR /app/frontend

COPY package.json ./

RUN npm install

COPY . ./
EXPOSE 3000