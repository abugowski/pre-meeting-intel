import pytest
from src.intelligence.exceptions import CompanyNotFoundError, APIConnectionError


def test_company_not_found_error():
    with pytest.raises(CompanyNotFoundError):
        raise CompanyNotFoundError("Company not found")


def test_api_connection_error():
    with pytest.raises(APIConnectionError):
        raise APIConnectionError("API connection error occurred")
