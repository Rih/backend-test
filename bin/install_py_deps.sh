#!/bin/bash
echo "install pip..."
container="app_web_enviame"
case "$(uname -s)" in
    Darwin)
    echo 'Mac OS X'
    docker exec  -it $container pip install -r requirements.txt
    ;;
    Linux)
    echo 'Linux'
    docker exec  -it $container pip install -r requirements.txt
    ;;
    CYWGWIN*|MINGW32*|MSYS*|MINGW*)
    echo 'Windows'
    winpty docker exec  -it $container pip install -r requirements.txt
    ;;
esac

echo "done."


