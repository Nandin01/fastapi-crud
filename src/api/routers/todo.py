from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from api.models.todo import Todo
from api.db.mongodb import get_database, get_todos_collection

router = APIRouter()

@router.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, db=Depends(get_database)):
    return db["todos"].insert_one(todo.dict())

@router.get("/todos/", response_model=List[Todo])
def read_todos(skip: int = 0, limit: int = 10, db=Depends(get_database)):
    todos = db["todos"].find().skip(skip).limit(limit)
    return [Todo(**todo) for todo in todos]

# @router.get("/todos/{todo_id}", response_model=Todo)
# def read_todo(todo_id: str, db=Depends(get_database)):
#     todo = db["todos"].find_one({"_id": todo_id})
#     if todo is None:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return Todo(**todo)
@router.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: str, db=Depends(get_database)):
    target_id = ObjectId(todo_id)
    todo = db["todos"].find_one({"_id": target_id})
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return Todo(**todo)

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: str, todo: Todo, db=Depends(get_database)):
    target_id = ObjectId(todo_id)
    updated_todo = db["todos"].find_one_and_update(
        {"_id": target_id}, {"$set": todo.dict()}, return_document=True
    )
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return Todo(**updated_todo)

@router.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: str, db=Depends(get_database)):
    target_id = ObjectId(todo_id)
    result = db["todos"].delete_one({"_id": target_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}

