import json

import pytest
from fastapi.testclient import TestClient

from src.server import app

test_client = TestClient(app)
items_url = "/items"


@pytest.mark.parametrize("item", [0, 1, 2, 3])
def test_items(item):
    response = test_client.get(f"{items_url}/{item}")
    assert response.status_code == 200
    assert json.loads(response.text) == {"item": f"item_{item}"}


@pytest.mark.parametrize("item", [4, 5, 6, 7])
def test_items_with_errors(item):
    response = test_client.get(f"{items_url}/{item}")
    assert response.status_code == 422
    assert json.loads(response.text) == {"message": f"there is no item with such id: '{item}'"}
