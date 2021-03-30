FROM toska/shibboleth-sp

COPY ./shib_conf/ /etc/shibboleth/
COPY ./apache_conf/SSL/ /etc/pki/tls/

CMD ["bash", "-c", "./etc/shibboleth/shib_start.sh"]