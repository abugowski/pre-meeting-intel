from tavily import AsyncTavilyClient
from src.api.config import settings


async def search_company(company_name):
    client = AsyncTavilyClient(api_key=settings.tavily_api_key)

    results = await client.search(
        query=company_name,
        topic="general",
    )

    return "\n".join([r["content"] for r in results["results"]])
