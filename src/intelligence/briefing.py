from anthropic import AsyncAnthropic
from pydantic import BaseModel
from src.intelligence.prompts import BRIEFING_SYSTEM_PROMPT


class BriefingResponse(BaseModel):
    """
    Create a response model for the briefing generation.
    """

    company_overview: str
    strategic_priorities: list[str]
    company_values: list[str]
    cio_profile: str
    current_challenges: list[str]
    industry_context: list[str]
    opportunities: list[str]
    talking_points: list[str]
    risk_flags: list[str]


async def generate_briefing(company_name: str) -> BriefingResponse:
    """
    Generate a briefing for the given company name.

    Args:
        company_name (str): The name of the company to generate a briefing for."""
    client = AsyncAnthropic()
    model = "claude-sonnet-4-6"

    message = await client.messages.parse(
        model=model,
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"Generate a briefing for the company {company_name} in 3 sentences.",
            }
        ],
        system=BRIEFING_SYSTEM_PROMPT,
        output_format=BriefingResponse,
    )

    return message.parsed_output
