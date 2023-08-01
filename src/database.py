from pymongo import MongoClient


class TodoService:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = client["todo"]
        self.collection = self.db["todo.todo"]

    async def create_todo(self, todo: dict):
        return await self.collection.insert_one(todo)

    async def get_todos(self):
        return list(self.collection.find())

    async def get_todo(self, id: str):
        return self.collection.find_one({"_id": id})

    async def update_todo(self, id: str, todo: dict):
        return await self.collection.update_one({"_id": id}, {"$set": todo})

    async def delete_todo(self, id: str):
        return await self.collection.delete_one({"_id": id})


