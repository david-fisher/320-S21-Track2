FROM python:3.6

RUN apt-get -qq update
RUN apt-get install --yes apache2 apache2-dev
RUN pip install django
RUN pip install mod_wsgi

RUN mkdir /code
WORKDIR /code

COPY . /code/
COPY ./apache2.conf /etc/apache2/apache2.conf

RUN chown -R www-data:www-data /code
RUN python manage.py migrate

EXPOSE 8000

CMD mod_wsgi-express start-server /code/apache_mod_wsgi/wsgi.py --user www-data --group www-data
