import pytest
from fastapi.testclient import TestClient

from duke.fast import app


@pytest.fixture
def fastapi_client():
    return TestClient(app)


def test_root(fastapi_client):
    response = fastapi_client.get("/")
    assert response.status_code == 200


def test_troops__valid_endpoint__return_success(fastapi_client):
    response = fastapi_client.get("/troop/assassin")
    assert response.status_code == 200


def test_troops__invalid_endpoint__return_failure(fastapi_client):
    response = fastapi_client.get("/troop/foo")
    assert response.status_code == 422
