import pytest
from pydantic import ValidationError
from src.intelligence.models import CompanyProfile


def test_create_company_profile() -> None:
    """Test creating a CompanyProfile instance with valid data."""
    profile = CompanyProfile(
        name="  Acme   Corporation",
        industry="Manufacturing   ",
        country="PL",
        notes="Leading   manufacturer   of widgets.",
    )

    assert profile.name == "Acme Corporation"
    assert profile.industry == "Manufacturing"
    assert profile.country == "PL"
    assert profile.notes == "Leading manufacturer of widgets."


def test_empty_name_raises_error() -> None:
    """Test that creating a CompanyProfile with an empty name raises a ValidationError."""
    with pytest.raises(ValidationError):
        CompanyProfile(
            name="",
            industry="  Technology. ",
            country="USA",
            notes="Innovative tech company.",
        )


def test_to_dict_returns_correct_data() -> None:
    """Test that the to_dict method returns a dictionary with the correct data."""
    profile = CompanyProfile(
        name=" PowerTech",
        industry="Energy",
        country="PL",
        notes="Leading energy company.",
    )
    result = profile.to_dict()
    assert result["name"] == "PowerTech"
    assert result["country"] == "PL"


def test_summary_contains_company_name() -> None:
    """Test that the summary method returns a string containing the company name."""
    profile = CompanyProfile(
        name="Alpha Energy",
        industry="Energy",
        country="PL",
        notes="Leading energy company.",
    )
    summary = profile.summary()
    assert isinstance(summary, str)
    assert "Alpha Energy" in summary


def test_summary_returns_correct_strings() -> None:
    """Test that the summary method returns a string containing all relevant information."""
    profile = CompanyProfile(
        name="Beta Tech",
        industry="Technology",
        country="US",
        notes="AI startup focused on machine learning.",
    )
    assert profile.summary() == (
        "Company: Beta Tech\n"
        "Industry: Technology\n"
        "Country: US\n"
        "Notes: AI startup focused on machine learning.\n"
    )


def test_to_dict_contains_all_fields() -> None:
    """Test that the to_dict method returns a dictionary containing all fields."""
    profile = CompanyProfile(
        name="Gamma Solutions",
        industry="Consulting",
        country="UK",
        notes="Provides business consulting services.",
    )
    result = profile.to_dict()
    assert "name" in result
    assert "industry" in result
    assert "country" in result
    assert "notes" in result
    assert result["name"] == "Gamma Solutions"
    assert result["industry"] == "Consulting"
    assert result["country"] == "UK"
    assert result["notes"] == "Provides business consulting services."
