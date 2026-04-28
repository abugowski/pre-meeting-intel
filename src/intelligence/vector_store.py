import chromadb


def add_documents(chromadb_client, documents: list[str], ids: list[str]) -> None:
    collection = chromadb_client.get_or_create_collection(name="briefing_knowledge")
    collection.upsert(ids=ids, documents=documents)


def search(
    chromadb_client, query: str, n_results: int = 3, max_distance: float = 1.5
) -> list[str]:
    collection = chromadb_client.get_collection(name="briefing_knowledge")
    results = collection.query(
        query_texts=[query], n_results=n_results, include=["documents", "distances"]
    )

    documents = results["documents"][0]
    distance = results["distances"][0]

    filtered = [doc for doc, dist in zip(documents, distance) if dist < max_distance]
    return filtered
