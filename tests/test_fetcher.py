import pytest
from src.intelligence.fetcher import fetch_url


@pytest.mark.asyncio
async def test_fetch_url_returns_dict():
    result = await fetch_url("https://api.github.com/users/abugowski")
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_fetch_url_contains_expected_data():
    result = await fetch_url("https://api.github.com/users/abugowski")
    assert result["login"] == "abugowski"
