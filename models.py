from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.String(10), nullable=True)
    priority = db.Column(db.String(10), nullable=True)
    status = db.Column(db.String(10), nullable=False, default="pending")
    user_id = db.Column(db.Integer, nullable=False)  # for user-specific tasks
