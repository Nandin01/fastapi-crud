import uvicorn
from fastapi import FastAPI
from api.routers import todo

app = FastAPI()

app.include_router(todo.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
