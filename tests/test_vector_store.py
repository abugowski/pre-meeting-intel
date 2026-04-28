import chromadb
from src.intelligence.vector_store import add_documents, search

client = chromadb.Client()


def test_add_documents_and_search():
    """Test that documents can be added and searched in the vector store."""
    add_documents(
        client,
        documents=[
            "This is a test document about AI.",
            "This is another document about machine learning.",
        ],
        ids=["doc1", "doc2"],
    )
    results = search(client, query="What is AI?", n_results=1, max_distance=0.6)
    assert len(results) > 0
    assert "AI" in results[0]
