from flask import Flask
from flask_restful import Api


def create_app(config_filename='config.py'):

    app = Flask(__name__)
    api = Api(app)

    app.config.from_pyfile(config_filename, silent=True)
    app.logger.setLevel(app.config['LOG_LEVEL'])

    api_prefix = '/api'

    from app.db import db

    db.init_app(app)

    from app.tasks.resources import Tasks, Task

    api.add_resource(Tasks, api_prefix + '/tasks')
    api.add_resource(Task, api_prefix + '/tasks/<int:pk>')

    return app
