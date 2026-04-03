import pytest
from pydantic import ValidationError
from src.intelligence.contact import Contact


def test_create_contact() -> None:
    """Test creating a Contact instance with valid data."""
    contact = Contact(
        first_name="Jon", last_name="Doe", role="Software Seller", email="pan@xyz.com"
    )

    assert contact.first_name == "Jon"
    assert contact.last_name == "Doe"
    assert contact.role == "Software Seller"
    assert contact.email == "pan@xyz.com"


def test_invalid_email_raises_error() -> None:
    """Test that creating a Contact with an invalid email raises a ValidationError."""
    with pytest.raises(ValidationError):
        Contact(first_name="Jane", last_name="Smith", role="CTO", email="invalid.org")


def test_full_name_returns_correct_format() -> None:
    """Test that the full_name method returns the correct format."""
    contact = Contact(
        first_name="Jan",
        last_name="Kowalski",
        role="Sales",
        email="jan.kowalski@example.com",
    )

    assert contact.full_name() == "Jan Kowalski"
