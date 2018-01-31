#!/bin/bash
# start production server

export DEBUG=False
export DATABASE_URL=psql://django:django@db:5432/postgres
export HIDE_DOCS=True

export DOCKER_CONFIG_PROD=${DOCKER_CONFIG_PROD:-docker-compose-prod.yml}
./bin/init_db.sh
docker-compose -f $DOCKER_CONFIG_PROD run --rm invoicer_prod python3 manage.py makemigrations
docker-compose -f $DOCKER_CONFIG_PROD run --rm invoicer_prod python3 manage.py migrate
docker-compose -f $DOCKER_CONFIG_PROD up -d
echo "started"