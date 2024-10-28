from flask import Blueprint, request, jsonify
from models import db, Task
from schemas import TaskSchema
from auth import token_required

tasks_bp = Blueprint('tasks', __name__)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@tasks_bp.route('/tasks', methods=['POST'])
@token_required
def create_task(current_user):
    data = request.get_json()
    errors = task_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_task = Task(user_id=current_user, **data)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task), 201

@tasks_bp.route('/tasks', methods=['GET'])
@token_required
def get_tasks(current_user):
    tasks = Task.query.filter_by(user_id=current_user).all()
    return tasks_schema.jsonify(tasks), 200

@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
@token_required
def get_task(current_user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user).first()
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    return task_schema.jsonify(task), 200

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@token_required
def update_task(current_user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user).first()
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    data = request.get_json()
    errors = task_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400
    for key, value in data.items():
        setattr(task, key, value)
    db.session.commit()
    return task_schema.jsonify(task), 200

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user, task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user).first()
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return '', 204
