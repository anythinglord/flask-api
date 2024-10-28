from flask import Flask, request, jsonify

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

# temporal db
tasks = []

# Endpoint to create a nek task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    tasks.append(new_task)
    return jsonify(new_task), 201

# Endpoint to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Endpoint to get a specific task using a id
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    return jsonify(task) if task else ("Tarea no encontrada", 404)

# Endpoint to update a Task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        updates = request.get_json()
        task.update(updates)
        return jsonify(task)
    return ("Task not found", 404)

# Endpoint to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return ("", 204)