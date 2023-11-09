import pytest

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SERVER_NAME': 'example.com',
        'SQLALCHEMY_DATABASE_URI': 'postgresql://postgres:postgres@localhost:5432/test',
    })

    # TODO: create and migrate database

    yield app

    # TODO: drop database


@pytest.fixture()
def client(app):
    return app.test_client()
