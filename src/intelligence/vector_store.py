import chromadb

client = chromadb.PersistentClient(path="./data/chroma_db")


def add_documents(documents: list[str], ids: list[str]) -> None:
    collection = client.get_or_create_collection(name="briefing_knowledge")
    collection.upsert(ids=ids, documents=documents)


def search(query: str, n_results: int = 3) -> list[str]:
    collection = client.get_collection(name="briefing_knowledge")
    results = collection.query(query_texts=[query], n_results=n_results)
    return results["documents"][0]
