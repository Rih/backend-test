#!/bin/bash

echo "Stoping containers..."
sh bin/stop-dev-server.sh
echo "Starting containers..."
sh bin/start-dev-server.sh
echo "Done."