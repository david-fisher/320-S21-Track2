IP=$(hostname -i); echo ip=$IP
sed -i "s/HOST_IP/${IP}/" /etc/shibboleth/shibboleth2.xml

for i in /var/www/html/simulator/static/js/*; do
    sed -i "s/localhost/${ORIGIN_HOST}/" $i;
done

for i in /var/www/html/se/static/js/*; do
    sed -i "s/localhost/${ORIGIN_HOST}/" $i
done

echo "export SERVER_NAME=${SERVER_NAME}" >> /etc/environment
echo "export SERVER_ADMIN=${SERVER_ADMIN}" >> /etc/environment
echo "\n. /etc/environment" >> /etc/httpd/envvars
httpd-shibd-foreground
