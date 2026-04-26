import chromadb

client = chromadb.PersistentClient(path="./data/chroma_db")


def add_documents(documents: list[str], ids: list[str]) -> None:
    collection = client.get_or_create_collection(name="briefing_knowledge")
    collection.upsert(ids=ids, documents=documents)


def search(query: str, n_results: int = 3, max_distance: float = 1.5) -> list[str]:
    collection = client.get_collection(name="briefing_knowledge")
    results = collection.query(
        query_texts=[query], n_results=n_results, include=["documents", "distances"]
    )

    documents = results["documents"][0]
    distance = results["distances"][0]

    filtered = [doc for doc, dist in zip(documents, distance) if dist < max_distance]
    return filtered
