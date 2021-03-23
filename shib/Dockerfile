FROM ubuntu:18.04

EXPOSE 80

RUN apt-get update && \
    apt-get -y install sudo
RUN sudo apt-get -y install apache2
RUN sudo service apache2 restart
RUN sudo apt-get -y install libapache2-mod-shib2
RUN sudo a2enmod ssl
RUN sudo a2ensite default-ssl.conf
COPY ./shib_conf/ /etc/shibboleth/
COPY ./apache_conf/ /etc/apache2/
RUN sudo a2enmod auth_basic
RUN sudo a2enmod shib2


CMD ["apachectl", "-D", "FOREGROUND"]