from anthropic import Anthropic
from anthropic import AsyncAnthropic


async def generate_briefing(company_name: str) -> str:
    """
    Generate a briefing for the given company name.

    Args:
        company_name (str): The name of the company to generate a briefing for."""
    client = AsyncAnthropic()
    model = "claude-sonnet-4-6"

    message = await client.messages.create(
        model=model,
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"Generate a briefing for the company {company_name} in 3 sentences.",
            }
        ],
    )

    return message.content[0].text
