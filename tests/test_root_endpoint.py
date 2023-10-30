import json

from fastapi.testclient import TestClient

from src.server import app

test_client = TestClient(app)
root_url = "/"


def test_root():
    response = test_client.get(root_url)
    assert response.status_code == 200
    assert json.loads(response.text) == {"message": "Hello World"}
