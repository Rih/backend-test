FROM python:3.7-buster
MAINTAINER Rodrigo Diaz <rodrigo.ediaz.f@gmail.com>
RUN apt-get update
RUN apt-get install -y software-properties-common apt-utils locales locales-all \
build-essential nginx \
git \
nano \
vim \
curl --no-install-recommends

RUN apt-get clean

WORKDIR /app
COPY ./backend/requirements.txt /app/tmp/
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py
# RUN python3 -m pip install mod_wsgi
RUN python3 -m pip install uwsgi
RUN python3 -m pip install -r /app/tmp/requirements.txt
COPY ./backend/enviame/uwsgi.conf /etc/init.d/uwsgi.conf
COPY ./backend/enviame/uwsgi.ini /uwsgi.ini
COPY ./nginx/app_back /etc/nginx/sites-enabled/app_back
COPY ./entrypoint-back.sh /usr/local/entrypoint-back.sh
RUN chmod +x /etc/init.d/uwsgi.conf
RUN chmod +x /usr/local/entrypoint-back.sh
RUN touch /var/log/uwsgi.log && chown www-data:www-data /var/log/uwsgi.log

# Set the locale
RUN locale-gen es_CL.UTF-8
ENV LANG es_CL.UTF-8
ENV LANGUAGE es_CL
ENV LC_ALL es_CL.UTF-8

EXPOSE 8000 80 8081 9091


CMD ["/usr/local/entrypoint-back.sh"]


