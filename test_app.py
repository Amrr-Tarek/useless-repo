import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "success", "message": "Hello, CI/CD!"}


def test_health(client):
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
