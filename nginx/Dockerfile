FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /docker-entrypoint.d/*

RUN apk add bash
RUN apk add --update python3 py3-pip
RUN apk add certbot
RUN pip install certbot-nginx

COPY ./nginx.conf /etc/nginx/conf.d/

RUN mkdir -p /app/staticfiles
RUN mkdir -p /app/media

RUN mkdir -p /usr/local/bin/

COPY ./setup-certbot.sh /usr/local/bin/setup-certbot.sh
RUN chmod +x /usr/local/bin/setup-certbot.sh

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]