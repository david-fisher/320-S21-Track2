for i in /var/www/html/simulator/static/js/*; do
    sed -i "s/ethisim2.cs.umass.edu/${ORIGIN_HOST}/" $i;
done

for i in /var/www/html/se/static/js/*; do
    sed -i "s/ethisim2.cs.umass.edu/${ORIGIN_HOST}/" $i
done
