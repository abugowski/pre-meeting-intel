import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from src.intelligence.search import search_company


@pytest.mark.asyncio
async def test_search_company():
    """Test that search_company, returns a string when given a valid company"""
    with patch("src.intelligence.search.AsyncTavilyClient") as mock_tavily:
        mock_instance = MagicMock()
        mock_tavily.return_value = mock_instance

        mock_response = MagicMock()
        mock_response = {
            "results": [
                {
                    "content": "Orlen is Polish energy company",
                }
            ]
        }
        mock_instance.search = AsyncMock(return_value=mock_response)

        result = await search_company("Orlen")
        assert result == "Orlen is Polish energy company"
