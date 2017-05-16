FROM alpine:3.5

RUN apk --update add apache2 php5-apache2 curl \
    php5-json php5-phar php5-openssl php5-mysql php5-curl php5-mcrypt php5-pdo_mysql php5-ctype php5-gd php5-xml php5-dom php5-iconv \
    && rm -f /var/cache/apk/* \
    && mkdir /run/apache2 \
    && mkdir -p /opt/utils
    
EXPOSE 80

ADD start.sh /opt/utils/

RUN chmod +x /opt/utils/start.sh

COPY app /app

ENTRYPOINT ["/opt/utils/start.sh"]
