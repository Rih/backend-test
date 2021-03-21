#!/bin/bash
container="app_web_enviame"

case "$(uname -s)" in
    Darwin)
    echo 'Mac OS X'
    docker exec  -it $container python3.7 manage.py loaddata continents.json countries.json employees.json
    ;;
    Linux)
    echo 'Linux'
    docker exec  -it $container python3.7 manage.py loaddata continents.json countries.json employees.json
    ;;
    CYWGWIN*|MINGW32*|MSYS*|MINGW*)
    echo 'Windows'
    winpty docker exec  -it $container python3.7 manage.py loaddata continents.json countries.json employees.json
    ;;
esac

echo "done."