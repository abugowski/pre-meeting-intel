import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from src.intelligence.briefing import (
    generate_briefing,
    generate_persona_briefing,
    stream_briefing,
)


@pytest.mark.asyncio
async def test_generate_briefing():
    """Test that generate_briefing returns a string when given a valid company name."""
    with patch("src.intelligence.briefing.AsyncAnthropic") as mock_anthropic:
        mock_instance = MagicMock()
        mock_anthropic.return_value = mock_instance

        mock_response = MagicMock()
        mock_response.parsed_output.company_overview = (
            "This is a briefing for the company Orlen."
        )
        mock_instance.messages.parse = AsyncMock(return_value=mock_response)

        result = await generate_briefing("Orlen")
        assert result.company_overview == "This is a briefing for the company Orlen."


@pytest.mark.asyncio
async def test_generate_persona_briefing():
    """Test that generate_persona_briefing returns a string when given a valid persona name."""
    with patch("src.intelligence.briefing.AsyncAnthropic") as mock_anthropic:
        mock_instance = MagicMock()
        mock_anthropic.return_value = mock_instance

        mock_response = MagicMock()
        mock_response.parsed_output.persona_overview = (
            "This is a briefing of the persona John Doe."
        )
        mock_instance.messages.parse = AsyncMock(return_value=mock_response)

        persona = await generate_persona_briefing("John Doe")
        assert persona.persona_overview == "This is a briefing of the persona John Doe."


# TODO: Add unit test for stream_briefing()
# Tested manually via curl --no-buffer
# Requires AsyncMock with async context manager support
