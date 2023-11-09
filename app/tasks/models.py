from datetime import datetime

from app.db import db


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    starts_at = db.Column(db.DateTime(), nullable=True)
    expires = db.Column(db.DateTime(), nullable=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def delete(task_id):
        Task.query.filter(Task.id == task_id).delete()
        db.session.commit()

    @staticmethod
    def update(task_id, data):
        Task.query.filter(Task.id == task_id).update(data)
        db.session.commit()

    def __repr__(self):
        return f'<Task  {self.name}>'
