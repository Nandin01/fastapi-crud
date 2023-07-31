from typing import Optional

import uvicorn

from models import Todo
from fastapi import FastAPI
from mongoengine import connect
import json

app = FastAPI()
connect(db="todo", host="localhost", port=27017)


# Get all data
@app.get("/")
def index():
    return {"message": "Welcome to the todo app!"}


# Get all todos
@app.get("/todos")
def get_all_todos():
    todos = Todo.objects().all()
    todo_list = []
    for todo in todos:
        todo_list.append(todo.to_dict())
    return {"todos": todo_list}


# Get a todo by ID
@app.get("/todos/{id}")
def get_todo_by_id(id: str):
    todo = Todo.objects.get(id=id)
    if todo is None:
        return {"message": "Todo not found."}
    return {"todo": todo.to_dict()}


# Create a new todo
@app.post("/todos")
def create_todo(title: str, description: Optional[str] = None):
    todo = Todo(title=title, description=description)
    todo.save()
    return {"todo": todo.to_dict()}


# Update a todo
@app.put("/todos/{id}")
def update_todo(id: str, title: Optional[str] = None, description: Optional[str] = None):
    todo = Todo.objects.get(id=id)
    if todo is None:
        return {"message": "Todo not found."}
    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    todo.save()
    return {"todo": todo.to_dict()}


# Delete a todo
@app.delete("/todos/{id}")
def delete_todo(id: str):
    todo = Todo.objects.get(id=id)
    if todo is None:
        return {"message": "Todo not found."}
    todo.delete()
    return {"message": "Todo deleted."}


if __name__ == "__main__":
     uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)