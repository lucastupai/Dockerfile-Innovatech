FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build


FROM nginx:alpine

RUN touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid /var/cache/nginx /var/log/nginx /usr/share/nginx/html
USER nginx

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]