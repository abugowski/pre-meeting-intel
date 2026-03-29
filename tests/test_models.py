import pytest
from src.intelligence.models import CompanyProfile


def test_create_company_profile():
    profile = CompanyProfile(
        name="  Acme Corporation  ",
        industry="Manufacturing",
        country="USA",
        notes="Leading manufacturer of widgets.",
    )

    assert profile.name == "Acme Corporation"
    assert profile.industry == "Manufacturing"


def empty_name_raises_error():
    with pytest.raises(ValueError):
        CompanyProfile(
            name="",
            industry="Technology",
            country="USA",
            notes="Innovative tech company.",
        )


def test_to_dict_returns_correct_data():
    profile = CompanyProfile(
        "Ignitis", "Energy", "Lithuania", "Leading energy company."
    )
    result = profile.to_dict()
    assert result["name"] == "Ignitis"
    assert result["country"] == "Lithuania"


def test_summary_contains_company_name():
    profile = CompanyProfile(
        "Ignitis", "Energy", "Lithuania", "Leading energy company."
    )
    summary = profile.summary()
    assert isinstance(summary, str)
    assert "Ignitis" in summary
