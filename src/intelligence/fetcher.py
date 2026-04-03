import httpx
from loguru import logger
from src.intelligence.exceptions import APIConnectionError


async def fetch_url(url: str) -> dict:
    """Fetch data from the given URL and return it as a dictionary."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            logger.error(f"Failed to fetch data from {url}: {response.status_code}")
            raise APIConnectionError(
                f"Failed to fetch data from {url}: {response.status_code}"
            )
        return response.json()
