export FLASK_APP=app

run:
	flask run

migrate:
	alembic upgrade head
