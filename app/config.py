import os
import logging

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')

# ORM settings
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = os.environ.get('FLASK_ENV') == 'development'

LOG_LEVEL = logging.INFO
if os.environ.get('FLASK_ENV') == 'development':
    LOG_LEVEL = logging.DEBUG
