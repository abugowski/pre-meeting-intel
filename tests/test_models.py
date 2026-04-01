import pytest
from pydantic import ValidationError
from src.intelligence.models import CompanyProfile


def test_create_company_profile():
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


def test_empty_name_raises_error():
    with pytest.raises(ValidationError):
        CompanyProfile(
            name="",
            industry="  Technology. ",
            country="USA",
            notes="Innovative tech company.",
        )


def test_to_dict_returns_correct_data():
    profile = CompanyProfile(
        name=" PowerTech",
        industry="Energy",
        country="PL",
        notes="Leading energy company.",
    )
    result = profile.to_dict()
    assert result["name"] == "PowerTech"
    assert result["country"] == "PL"


def test_summary_contains_company_name():
    profile = CompanyProfile(
        name="Alpha Energy",
        industry="Energy",
        country="PL",
        notes="Leading energy company.",
    )
    summary = profile.summary()
    assert isinstance(summary, str)
    assert "Alpha Energy" in summary
