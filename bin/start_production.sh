#!/bin/bash
# start production server

export DEBUG=True
export DATABASE_URL=psql://django:django@db:5432/postgres

export DOCKER_CONFIG_PROD=${DOCKER_CONFIG_PROD:-docker-compose-prod.yml}
./bin/init_db.sh
docker-compose -f $DOCKER_CONFIG_PROD run --rm invoicer_prod python manage.py makemigrations
docker-compose -f $DOCKER_CONFIG_PROD run --rm invoicer_prod python manage.py migrate
docker-compose -f $DOCKER_CONFIG_PROD up -d
echo "started"