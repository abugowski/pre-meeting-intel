import pytest
from src.intelligence.exceptions import CompanyNotFoundError, APIConnectionError


def test_company_not_found_error() -> None:
    """Test that raising a CompanyNotFoundError works as expected."""
    with pytest.raises(CompanyNotFoundError):
        raise CompanyNotFoundError("Company not found")


def test_api_connection_error() -> None:
    """Test that raising an APIConnectionError works as expected."""
    with pytest.raises(APIConnectionError):
        raise APIConnectionError("API connection error occurred")
