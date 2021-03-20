#!/bin/bash

case "$(uname -s)" in
    Darwin)
    echo 'Mac OS X'
    docker exec -it $(docker-compose ps -q web) bash
    ;;
    Linux)
    echo 'Linux'
    docker exec -it $(docker-compose ps -q web) bash
    ;;
    CYWGWIN*|MINGW32*|MSYS*|MINGW*)
    echo 'Windows'
    winpty docker exec -it $(docker-compose ps -q web) bash
    ;;
esac



