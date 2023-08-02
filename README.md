# FastAPI Todo App

A simple CRUD Todo app built with FastAPI and MongoDB.

## Description

This project is a basic Todo app that allows users to create, read, update, and delete Todo items. It is built using the FastAPI framework for the backend and MongoDB as the database to store the Todo items.

## Features

- Create a new Todo item with a title and description.
- Retrieve a Todo item by its unique ID.
- Update an existing Todo item's title, description, or completion status.
- Delete a Todo item by its ID.
- List all Todo items.

## Requirements

- Python 3.9 or later
- FastAPI
- Uvicorn
- PyMongo

## Installation

1. Clone the repository:

   git clone https://github.com/Nandin01/fastapi-crud.git

2. Install the required dependencies:

   pip install -r requirements.txt

3. Run the FastAPI app using Uvicorn:

   uvicorn app.main:app --host 0.0.0.0 --port 8000

4. The FastAPI app will be accessible at Swagger: http://localhost:8000/docs
5. See the swagger docs http://localhost:8000/redoc

## API Endpoints

- `POST /todos/`: Create a new Todo item.
- `GET /todos/{todo_id}`: Retrieve a Todo item by ID.
- `PUT /todos/{todo_id}`: Update an existing Todo item.
- `DELETE /todos/{todo_id}`: Delete a Todo item by ID.
- `GET /todos/`: List all Todo items.

## Testing

To run the test suite, use the `pytest` command:

   pytest

## Docker Support

To run the app using Docker, follow these steps:

1. Build the Docker image:

   docker build -t todo-app .

2. Run the Docker container:

   docker run -d -p 8000:8000 todo-app

The FastAPI Todo app will be running inside a Docker container at http://localhost:8000.

Feel free to customize the `README.md` file further to add any additional details or make it more suitable for your project.

