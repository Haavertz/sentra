from fastapi.testclient import TestClient
from db.client import database
from main import app

client = TestClient(app)

