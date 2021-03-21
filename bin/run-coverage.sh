#!/bin/bash

container="app_web_enviame"
docker exec  -it $container coverage3 run --source='.' manage.py test
docker exec  -it $container coverage3 report -m
# docker exec  -it $container coverage3 html
