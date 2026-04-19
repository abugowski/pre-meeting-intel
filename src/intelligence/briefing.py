from anthropic import AsyncAnthropic
from pydantic import BaseModel
from src.intelligence.prompts import BRIEFING_SYSTEM_PROMPT, BRIEFING_USER_PROMPT


class BriefingResponse(BaseModel):
    """
    Create a response model for the briefing generation.
    """

    company_overview: str
    strategic_priorities: list[str]
    company_values: list[str]
    person_profile: str
    current_challenges: list[str]
    industry_context: list[str]
    opportunities: list[str]
    talking_points: list[str]
    risk_flags: list[str]


async def generate_briefing(
    company_name: str,
    person_name: str,
    person_bio: str | None = None,
    industry: str | None = None,
    technology_focus: str | None = None,
) -> BriefingResponse:
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
                "content": BRIEFING_USER_PROMPT.format(company_name=company_name),
            }
        ],
        system=BRIEFING_SYSTEM_PROMPT,
        output_format=BriefingResponse,
    )

    return message.parsed_output
