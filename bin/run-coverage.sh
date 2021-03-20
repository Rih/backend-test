#!/bin/bash


docker exec  -it app_web_enviame coverage3 run --source='.' backend/manage.py test
docker exec  -it app_web_enviame coverage3 report -m
#docker exec  -it app_web_enviame coverage3 html
