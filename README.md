
## Task Management API

This project is a simple REST API built with Flask for managing a list of tasks. It provides CRUD (Create, Read, Update, Delete) operations on tasks, allowing users to organize and prioritize their to-do items.

### Features

- Create tasks with details like title, description, due date, priority, and status.
- Retrieve a list of all tasks or a specific task by ID.
- Update tasks to modify details or mark as completed.
- Delete tasks when they are no longer needed.
- Simple file-based storage using JSON for easy setup and use.

### Project Structure

```
task_manager/
├── app.py               # Main application file
├── requirements.txt     # Project dependencies
└── data/
    └── tasks.json       # Simulated database for storing tasks
```

### Requirements

- Python 3.x
- Flask (specified in `requirements.txt`)

### Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/task-manager-api.git
   cd task-manager-api
   ```

2. **Install dependencies**:
   Use the following command to install the required Python packages.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Flask server by running:
   ```bash
   python app.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

### Endpoints

#### 1. Create a Task
- **Endpoint**: `/tasks`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "title": "My first task",
    "description": "This is a sample task",
    "due_date": "2024-11-10",
    "priority": "high",
    "status": "pending"
  }
  ```
- **Response**: Returns the created task object with an `id`.

#### 2. Get All Tasks
- **Endpoint**: `/tasks`
- **Method**: `GET`
- **Response**: List of all tasks.

#### 3. Get a Task by ID
- **Endpoint**: `/tasks/<task_id>`
- **Method**: `GET`
- **Response**: The specific task if found, otherwise a `404` error.

#### 4. Update a Task
- **Endpoint**: `/tasks/<task_id>`
- **Method**: `PUT`
- **Payload**: JSON with fields to update (e.g., `status`, `priority`).
- **Response**: Returns the updated task or `404` if not found.

#### 5. Delete a Task
- **Endpoint**: `/tasks/<task_id>`
- **Method**: `DELETE`
- **Response**: `204` status code on success, `404` if not found.

### Example Usage

1. **Creating a Task**:
   ```bash
   curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": "Test Task", "description": "Test Description", "due_date": "2024-11-10", "priority": "medium", "status": "pending"}'
   ```

2. **Getting All Tasks**:
   ```bash
   curl -X GET http://127.0.0.1:5000/tasks
   ```

3. **Updating a Task**:
   ```bash
   curl -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d '{"status": "completed"}'
   ```

4. **Deleting a Task**:
   ```bash
   curl -X DELETE http://127.0.0.1:5000/tasks/1
   ```

### License

This project is licensed under the MIT License.
# repo
