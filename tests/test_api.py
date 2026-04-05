import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_health_endpoint():
    """Test the /health endpoint to ensure it returns the correct status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_post_company_endpoint():
    """Test the /company/{name} endpoint to ensure it returns the correct company information."""
    company_data = {
        "name": "Test Company",
        "industry": "Technology",
        "country": "US",
    }
    response = client.post("/company", json=company_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Company"
    assert response.json()["country"] == "US"
