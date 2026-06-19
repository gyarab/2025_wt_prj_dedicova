FROM node:22-slim AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:1.27-alpine

RUN mkdir -p /usr/share/nginx/vue

COPY --from=build /app/dist/ /usr/share/nginx/vue/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]