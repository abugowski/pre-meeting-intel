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


async def fetch_country_data(country_code: str) -> str:
    """Fetch country data from the REST Countries API."""
    logger.info(f"Fetching data for country code {country_code}")
    response = await fetch_url(f"https://restcountries.com/v3.1/alpha/{country_code}")
    logger.info(f"Successfully fetched data for country code {country_code}")
    return f"Capital: {response[0].get('capital', ['N/A'])[0]}, Population: {response[0].get('population', ['N/A'])}, Languages: {list(response[0].get('languages', ['N/A']).values())[0]}"
