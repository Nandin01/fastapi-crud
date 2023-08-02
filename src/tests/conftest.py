import pytest
from pymongo import MongoClient
from api.db.mongodb import get_database

@pytest.fixture
def test_database():
    # Connect to the test database
    client = MongoClient("mongodb://localhost:27017/")
    db = client["test_todo"]
    yield db

    # Clean up: Drop the test database after tests are finished
    client.drop_database("test_todo")

# Ensure that the `test_database` fixture is used by other test functions
pytestmark = pytest.mark.usefixtures("test_database")
