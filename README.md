# task1

## Setup

* Create and activate virtual environment.
* Install requirements


    $ pip install -r requirements.txt


* Copy .env_example to .env
* Migrate database

    $ alembic upgrade head


## Run the project

    $ export FLASK_APP=app
    $ flask run
