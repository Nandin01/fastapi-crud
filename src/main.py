from datetime import datetime

import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient
from database import TodoService

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
todo_service = TodoService(client)

# Define the routes
@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API!"}

@app.post("/todos")
async def create_todo(todo: dict):
    todo["created_at"] = {"$date": datetime.utcnow()}
    todo["updated_at"] = {"$date": datetime.utcnow()}
    result = await todo_service.create_todo(todo)
    return result

@app.get("/todos")
async def get_todos():
    return await todo_service.get_todos()

@app.get("/todos/{id}")
async def get_todo(id: str):
    return await todo_service.get_todo(id)

@app.put("/todos/{id}")
async def update_todo(id: str, todo: dict):
    return await todo_service.update_todo(id, todo)

@app.delete("/todos/{id}")
async def delete_todo(id: str):
    return await todo_service.delete_todo(id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)