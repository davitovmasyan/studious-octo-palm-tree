from datetime import datetime

from flask import request
from flask_restful import Resource

from .models import Task as TaskModel


class TaskBase(Resource):
    def _validate(self, data):
        errors = {}

        task = TaskModel()
        task.name = data.get('name')

        if task.name == "":
            errors["name"] = "invalid"

        try:
            task.starts_at = datetime.strptime(
                data.get('starts_at'),
                "%Y-%m-%d %H:%M:%S",
            )
        except Exception:
            errors["starts_at"] = "invalid"

        try:
            task.expires = datetime.strptime(
                data.get('expires'),
                "%Y-%m-%d %H:%M:%S",
            )
        except Exception:
            errors["expires"] = "invalid"

        return task, errors


class Tasks(TaskBase):
    def get(self):
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per-page", 10, type=int)
        tasks = TaskModel.query.paginate(page=page, per_page=per_page)

        response = []

        for a in tasks.items:
            starts_at = None
            expires = None
            if a.starts_at:
                starts_at = a.starts_at.strftime('%Y-%m-%d %H:%M:%S')
            if a.expires:
                expires = a.expires.strftime('%Y-%m-%d %H:%M:%S')

            item = {
                'id': a.id,
                'name': a.name,
                'expires': expires,
                'starts_at': starts_at,
            }
            response.append(item)

        return response

    def post(self):
        data = request.get_json()
        task, errors = self._validate(data)
        if len(errors) > 0:
            return errors, 400

        if TaskModel.query.filter_by(name=task.name).count() > 0:
            return {"name": "must be unique"}, 400

        task.save()

        return None, 201


class Task(TaskBase):
    def get(self, pk):
        task = TaskModel.query.filter(TaskModel.id == pk).first()
        if task is None:
            return None, 404

        starts_at = None
        expires = None
        if task.starts_at:
            starts_at = task.starts_at.strftime('%Y-%m-%d %H:%M:%S')
        if task.expires:
            expires = task.expires.strftime('%Y-%m-%d %H:%M:%S')

        return {
            'id': task.id,
            'name': task.name,
            'expires': expires,
            'starts_at': starts_at,
        }

    def put(self, pk):
        data = request.get_json()
        task, errors = self._validate(data)
        if len(errors) > 0:
            return errors, 400

        existingTask = TaskModel.query.filter(
            TaskModel.id != pk,
            TaskModel.name == task.name,
        ).first()
        if existingTask is not None:
            return {"name": "must be unique"}, 400

        TaskModel.update(
            pk,
            {
                'name': task.name,
                'starts_at': task.starts_at,
                'expires': task.expires,
            },
        )
        return None, 200

    def delete(self, pk):
        TaskModel.delete(pk)
        return None, 200
