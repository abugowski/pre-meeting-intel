from fastapi.testclient import TestClient
from src.api.main import app
from unittest.mock import patch
from src.intelligence.exceptions import APIConnectionError

client = TestClient(app)


def test_health_endpoint():
    """Test the /health endpoint to ensure it returns the correct status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_post_company_endpoint():
    """Test the POST endpoint /company endpoint to ensure it returns the correct company information."""
    company_data = {
        "name": "Test Company",
        "industry": "Technology",
        "country": "US",
    }
    response = client.post("/company", json=company_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Company"
    assert response.json()["country"] == "US"


def test_post_company_name_empty():
    """Test the POST /company endpoint to ensure it returns the correct error when the company name is empty"""
    company_data = {
        "name": "",
        "industry": "Technology",
        "country": "US",
    }
    response = client.post("/company", json=company_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Company name cannot be empty"


def test_post_company_api_connection_error():
    """Test the POST /company endpoint to ensure it returns the correct error when the external API is unavailable"""
    company_data = {
        "name": "Test Company",
        "industry": "Technology",
        "country": "US",
    }
    with patch("src.api.main.CompanyProfile.create") as mock_create:
        mock_create.side_effect = APIConnectionError("Connection failed")
        response = client.post("/company", json=company_data)
        assert response.status_code == 503
        assert response.json()["detail"] == "External API is unavailable"


def test_post_company_unexpected_error():
    """Test the POST /company endpoint to ensure it returns the correct error when an unexpected error occurs"""
    company_data = {
        "name": "Test Company",
        "industry": "Technology",
        "country": "US",
    }
    with patch("src.api.main.CompanyProfile.create") as mock_create:
        mock_create.side_effect = Exception("Unexpected error")
        response = client.post("/company", json=company_data)
        assert response.status_code == 500
        assert response.json()["detail"] == "Internal Server Error"
