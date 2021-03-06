invoicer
=====================================================

There are two options to setup and run the app. You can either choose to setup the Docker environment or run it via `pipenv` (virtualenv like system). In both options you must have the 'stack' installed. 

Stack
=============

* pipenv
* pip
* Python 3.6

Docker setup requirements 
=============================

* Docker CE (lastest) installed
    * Installation    
        * Docker, see [here](https://docs.docker.com/installation/)
    
    * Used Docker images:
        * Python 3.6
        * Postgres

Run the app
===========

1. Git clone this [repo](https://github.com/diogosimao/desafio-programacao-1.git). Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
    
    $ git clone https://github.com/diogosimao/desafio-programacao-1.git && cd desafio-programacao-1

2. Make sure you have `pipenv` installed via `pip`.

3. Use `pipenv` to create a virtualenv, install its dependencies and activate the virtualenv.

    $ pipenv --three && pipenv shell

4. Run `. ./bin/start_development.sh`


#### Note: lookup `./bin` directory  in order to get more options so that you can run the app.  


Hosted on Heroku
================

[Link](https://invoicer-challenge.herokuapp.com)