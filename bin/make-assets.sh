#!/bin/bash
container="app_web_enviame"
case "$(uname -s)" in
    Darwin)
    echo 'Mac OS X'
    docker exec  -it $container python3 manage.py collectstatic
    ;;
    Linux)
    echo 'Linux'
    docker exec  -it $container python3 manage.py collectstatic
    ;;
    CYWGWIN*|MINGW32*|MSYS*|MINGW*)
    echo 'Windows'
    winpty docker exec  -it $container python3 manage.py collectstatic
    ;;
esac
