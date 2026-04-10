import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from src.intelligence.briefing import generate_briefing


@pytest.mark.asyncio
async def test_generate_briefing():
    """Test that generate_briefing returns a string when given a valid company name."""
    with patch("src.intelligence.briefing.AsyncAnthropic") as mock_anthropic:
        mock_instance = MagicMock()
        mock_anthropic.return_value = mock_instance

        mock_response = MagicMock()
        mock_response.content[0].text = "This is a briefing for the company Orlen."
        mock_instance.messages.create = AsyncMock(return_value=mock_response)

        result = await generate_briefing("Orlen")
        assert result == "This is a briefing for the company Orlen."
