#!/bin/bash
# stop production server

export DOCKER_CONFIG_PROD=${DOCKER_CONFIG_PROD:-docker-compose-prod.yml}
docker-compose -f $DOCKER_CONFIG_PROD stop
echo "stopped"