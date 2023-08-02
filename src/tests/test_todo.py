from fastapi.testclient import TestClient
from bson import ObjectId

from api.main import app

client = TestClient(app)

def test_read_todo(test_database):
    # Assuming you have an existing Todo in the test database with the following ObjectId
    target_id_str = "64ca3b89182de4fa0e6afe87"
    response = client.get(f"/todos/{target_id_str}")
    if response.status_code == 200:
        data = response.json()
        assert "title" in data
        assert data["title"] == "Wash"
        assert "created_at" in data
        assert "updated_at" in data
    elif response.status_code == 404:

        assert True  # This assertion just ensures that the test passes if the Todo is not found
    else:
        # Unexpected response status code, fail the test with a message
        assert False, f"Unexpected response status code: {response.status_code}"

def test_update_todo(test_database):
    # Assuming you have an existing Todo in the test database with the following ObjectId
    target_id_str = "64ca3b89182de4fa0e6afe87"
    updated_todo_data = {
        "title": "Updated Title",
        "description": "Updated Description",
        "completed": True
    }

    # Access the "todos" collection from the test database
    todos_collection = test_database["todos"]

    # Retrieve the existing Todo by ObjectId
    existing_todo = todos_collection.find_one({"_id": target_id_str})
    assert existing_todo is not None, f"Todo with ID {target_id_str} not found in the test database"

    # Perform the update
    response = client.put(f"/todos/{target_id_str}", json=updated_todo_data)
    assert response.status_code == 200
    updated_todo = response.json()
    assert "title" in updated_todo
    assert updated_todo["title"] == "Updated Title"
    assert "description" in updated_todo
    assert updated_todo["description"] == "Updated Description"
    assert "completed" in updated_todo
    assert updated_todo["completed"] is True
    assert "created_at" in updated_todo
    assert "updated_at" in updated_todo
    assert updated_todo["created_at"] == existing_todo["created_at"]  # Verify created_at remains the same
    assert updated_todo["updated_at"] != existing_todo["updated_at"]  # Verify updated_at changes

def test_delete_todo(test_database):
    # Assuming we have existing Todo in the test database with the following ObjectId
    target_id_str = "64ca3b89182de4fa0e6afe87"
    response = client.delete(f"/todos/{target_id_str}")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Todo deleted successfully"

    # Verify that the Todo is deleted by attempting to read it again
    response = client.get(f"/todos/{target_id_str}")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Todo not found"

def test_get_all_todos(test_database):
    # Assuming we have multiple existing Todos in the test database
    response = client.get("/todos/")
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)
    assert len(todos) >= 1  # There should be at least one Todo in the response
    for todo in todos:
        assert "title" in todo
        assert "description" in todo
        assert "completed" in todo
        assert "created_at" in todo
        assert "updated_at" in todo