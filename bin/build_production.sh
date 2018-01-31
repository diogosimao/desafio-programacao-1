#!/bin/bash
#build production

export DOCKER_CONFIG_PROD=${DOCKER_CONFIG_PROD:-docker-compose-prod.yml}
docker-compose -f $DOCKER_CONFIG_PROD build
docker-compose -f $DOCKER_CONFIG_PROD run --rm invoicer_prod python3 manage.py collectstatic --noinput