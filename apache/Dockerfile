FROM toska/shibboleth-sp

COPY ./shib_conf/ /etc/shibboleth/
COPY ./apache_conf/ssl/ /etc/pki/tls/certs/
COPY ./build/ /var/www/html/

CMD ["bash", "-c", "chmod +x ./etc/shibboleth/shib_start.sh && ./etc/shibboleth/shib_start.sh"]