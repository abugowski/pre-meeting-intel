import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_health_endpoint():
    """Test the /health endpoint to ensure it returns the correct status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_company_endpoint():
    """Test the /company/{name} endpoint to ensure it returns the correct company information."""
    company_name = "TestCompany"
    response = client.get(f"/company/{company_name}")
    assert response.status_code == 200
    assert response.json()["company"] == "TestCompany"
