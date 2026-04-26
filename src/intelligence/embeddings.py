import voyageai
from src.api.config import settings


def embed_text(text: str) -> list[float]:
    client = voyageai.Client(api_key=settings.voyage_api_key)

    results = client.embed([text], model="voyage-4-lite")

    return results.embeddings[0]
