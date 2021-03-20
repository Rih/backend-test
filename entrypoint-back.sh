#!/bin/sh
set -e

# running nginx + uwsgi
service nginx start

uwsgi --ini /uwsgi.ini

tail -f /var/log/uwsgi.log
