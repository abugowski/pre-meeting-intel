from anthropic import AsyncAnthropic
from pydantic import BaseModel
from src.api.config import settings

class BriefingResponse(BaseModel):
    """
    Create a response model for the briefing generation.
    """

    company_overview: str
    strategic_priorities: list[str]
    company_values: list[str]
    target_personas: str = ""
    current_challenges: list[str]
    industry_context: list[str]
    opportunities: list[str]

class PersonaBriefingResponse(BaseModel):
    """
    Create a response model for the person briefing generation.
    """
    persona_overview: str
    strategic_priorities: list[str]
    talking_points: list[str]
    risk_flags: list[str]

async def generate_briefing(
    company_name: str,
    industry: str | None = None,
    technology_focus: str | None = None,
) -> BriefingResponse:
    """
    Generate a briefing for the given company name.

    Args:
        company_name (str): The name of the company to generate a briefing for."""

    client = AsyncAnthropic()
    # model = "claude-sonnet-4-6"
    model = "claude-haiku-4-5"

    prompt = settings.briefing_user_prompt.format(company_name=company_name)
    if industry:
        prompt += settings.briefing_user_industry_prompt.format(industry=industry)
    if technology_focus:
        prompt += settings.briefing_user_technology_prompt.format(technology_focus=technology_focus, company_name=company_name)
    

    message = await client.messages.parse(
        model=model,
        max_tokens=4000,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        system=settings.briefing_system_prompt,
        output_format=BriefingResponse,
    )

    return message.parsed_output

async def generate_persona_briefing(
    name: str,
    position: str | None = None,
    bio: str | None = None,
) -> PersonaBriefingResponse:
    """
    Generate a persona-based briefing for the given persona.
    Args:
        name (str): The name of the persona.
        position (str, optional): The position of the persona. Defaults to None.
        bio (str, optional): The bio of the persona. Defaults to None.
    Returns:
        PersonaBreifingResponse: The generated persona-based briefing.
    """
    client = AsyncAnthropic()
    # model = "claude-sonnet-4-6"
    model = "claude-haiku-4-5"

    prompt = settings.briefing_user_person_prompt.format(name=name)
    if bio:
        prompt += settings.briefing_user_bio_prompt.format(bio=bio)

    message = await client.messages.parse(
        model=model,
        max_tokens=4000,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        system=settings.briefing_system_prompt,
        output_format=PersonaBriefingResponse,
    )
    return message.parsed_output
