import pytest
from src.intelligence.utils import clean_text


def test_clean_text_removes_extra_whitespace() -> None:
    """Test that clean_text removes extra whitespace from a string."""
    assert clean_text("  Hello   World  ") == "Hello World"


def test_clean_text_with_tabs_and_newlines() -> None:
    """Test that clean_text handles tabs and newlines correctly."""
    assert clean_text("\tHello\nWorld\t") == "Hello World"


def test_clean_text_with_only_whitespace() -> None:
    """Test that clean_text returns an empty string when given a string with only whitespace."""
    assert clean_text(" ") == ""
