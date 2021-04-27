FROM toska/shibboleth-sp

RUN bash -c "yum -y install python3 python3-devel httpd-devel python3-pip"
RUN bash -c "yum -y install httpd-devel httpd24 httpd24-httpd-devel gcc"
RUN python3.6 -m pip install mod_wsgi-standalone
RUN python3.6 -m pip install ptvsd 
COPY requirements.txt ./
RUN python3.6 -m pip install -r requirements.txt
COPY ./www/lead/ /var/www/backend/lead/
COPY ./www/segfault/ /var/www/backend/segfault/
COPY ./shib_conf/ /etc/shibboleth/
COPY ./apache_conf/httpd.conf /etc/httpd/conf/
COPY ./apache_conf/.htaccess /var/www/html/
COPY ./apache_conf/conf.d/segfault.conf /etc/httpd/conf.d/
COPY ./apache_conf/conf.d/backendboys.conf /etc/httpd/conf.d/
COPY ./apache_conf/ssl/ /etc/pki/tls/certs/
COPY ./build/ /var/www/html/
RUN echo "export SERVER_NAME=${SERVER_NAME}" >> /etc/environment
RUN echo "export SERVER_NAME=${SERVER_NAME}" >> /etc/environment
