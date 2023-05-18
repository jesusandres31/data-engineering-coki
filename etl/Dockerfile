FROM node:14-alpine

RUN apk add --no-cache mdbtools unixodbc unixodbc-dev && \
    mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . . 
  
CMD ["npm", "start"]