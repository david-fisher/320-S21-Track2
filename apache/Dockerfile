FROM toska/shibboleth-sp

COPY ./shib_conf/ /etc/shibboleth/
COPY ./apache_conf/ssl/ /etc/pki/tls/certs/
COPY ./build/ /var/www/html/

CMD ["bash", "-c", "./etc/shibboleth/shib_start.sh"]