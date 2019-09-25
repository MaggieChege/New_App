# New_App
This contains a new Python setup
# Clone the repo

## Create virtual environment 
$ python3.6 -m venv env
## Activate virtual env 
$ source env/bin/activate
## Install requirements run 
$ pip3 install -r requirements.txt
## To start server 
  $ python run.py
# TO test the URL on postman 
http://127.0.0.1:5000/api/Hello
## Run migrations initialization, using the db init command as follows:
  $ python migrate.py db init
 $ python migrate.py db migrate
## Apply migrations to the DB 
$ python migrate.py db upgrade
