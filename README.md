# FastAPI Todo App
A simple CRUD Todo app built with FastAPI and MongoDB.


##Description
This project is a basic Todo app that allows users to create, read, update, and delete Todo items. It is built using the FastAPI framework for the backend and MongoDB as the database to store the Todo items.


##Features
Create a new Todo item with a title and description.
Retrieve a Todo item by its unique ID.
Update an existing Todo item's title, description, or completion status.
Delete a Todo item by its ID.
List all Todo items.

##Requirements
Python 3.9 or later
FastAPI
Uvicorn
PyMongo

##Installation
clone:
git clone https://github.com/Nandin01/fastapi-crud.git


Install the required dependencies:
pip install -r requirements.txt

run:
uvicorn app.main:app --host 0.0.0.0 --port 8000


The FastAPI app will be accessible at swagger http://localhost:8000/docs


API Endpoints
POST /todos/: Create a new Todo item.
GET /todos/{todo_id}: Retrieve a Todo item by ID.
PUT /todos/{todo_id}: Update an existing Todo item.
DELETE /todos/{todo_id}: Delete a Todo item by ID.
GET /todos/: List all Todo items.

##Testing
pytest

##Docker
Build the Docker image:
docker build -t todo-app .


Run the Docker container:
docker run -d -p 8000:8000 todo-app
