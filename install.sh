#!/bin/bash
cp conf.ini src/.env.dev
cd src
sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose exec django python3 manage.py makemigrations
sudo docker-compose exec django python3 manage.py migrate
sudo docker-compose down
cd ..
