#!/bin/bash

cat <<EOF > /etc/nginx/conf.d/default.conf
server {
    listen 80;
    server_name $DOMAIN_URL;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://\$host\$request_uri;
    }
}
EOF

nginx -s reload

certbot --nginx -d $DOMAIN_URL --non-interactive --agree-tos --email $DOMAIN_EMAIL

cat <<EOF > /etc/nginx/conf.d/default.conf
server {
    listen 443 ssl;
    server_name $DOMAIN_URL;

    ssl_certificate /etc/letsencrypt/live/$DOMAIN_URL/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$DOMAIN_URL/privkey.pem;

    location / {
        proxy_pass http://django:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }
}

server {
    listen 80;
    server_name $DOMAIN_URL;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://\$host\$request_uri;
    }
}
EOF

nginx -s reload