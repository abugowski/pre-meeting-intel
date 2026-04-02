import pytest
from src.intelligence.utils import clean_text


def test_clean_text_removes_extra_whitespace():
    assert clean_text("  Hello   World  ") == "Hello World"


def test_clean_text_with_tabs_and_newlines():
    assert clean_text("\tHello\nWorld\t") == "Hello World"


def test_clean_text_with_only_whitespace():
    assert clean_text(" ") == ""
