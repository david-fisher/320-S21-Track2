IP=$(hostname -i); echo ip=$IP
sed -i "s/HOST_IP/${IP}/" /etc/shibboleth/shibboleth2.xml

httpd-shibd-foreground