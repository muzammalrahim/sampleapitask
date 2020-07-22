# Getting Started


### Prerequisite

python 3.8 

SQLite Database

pipenv


# Setup and run in local Machine/Server

clone repo: git clone https://github.com/muzammalrahim/sampleapitask.git

cd sampleapitask

Run pipenv shell

Then 

Run pipenv install



## Run the Server
Run python manage.py migrate and run the server python manage.py runserver (before migrate, pleae create migrations file by python manage.py makemigrations) and we will keep track of each migrations later

and hit the url: http://127.0.0.1:8000/


## Tests

To run tests just run pytest in terminal
