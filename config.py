import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_na"
#Clone the repo
#setup the DATABASE_URI as statated above
#To create virtual environment $ python3.6 -m venv env
#To activate virtual env $ source env/bin/activate
#Install requirements run $ pip3 install -r requirements.txt
# To start server $ python run.py
# TO test the URL on postman $ http://127.0.0.1:5000/api/Hello
# Run migrations initialization, using the db init command as follows:
#   $ python migrate.py db init
#   $ python migrate.py db migrate
# TO apply migrations to the DB $ python migrate.py db upgrade
