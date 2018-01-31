#!/bin/bash
#start development server on :8000

export DEBUG=True
export DATABASE_URL=sqlite:////tmp/invoicer-tmp-sqlite.db
export HIDE_DOCS=False

read -n1 -p "Run the app on Docker [D] or pipenv [P]: " choice
case $choice in
  d|D) printf "\nRunning on Docker...\n"
    pip install -r requirements_docker.txt
    export DOCKER_CONFIG=${DOCKER_CONFIG:-docker-compose.yml}
    docker-compose -f $DOCKER_CONFIG build
    docker-compose -f $DOCKER_CONFIG run --rm invoicer makemigrations
    docker-compose -f $DOCKER_CONFIG run --rm invoicer migrate
    docker-compose -f $DOCKER_CONFIG up ;;
  p|P) printf "\nRunning on pipenv...\n "
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver ;;
  *) printf "\nChoose [D] for Docker or [P] for pipenv. \n" ;;
esac

