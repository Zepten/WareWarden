FROM node:22-alpine3.20 AS development

RUN apk update && apk add --no-cache curl

WORKDIR /src

EXPOSE 5000

CMD ["npm", "run", "dev"]