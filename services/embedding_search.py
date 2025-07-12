from vector_store.faiss_store import FAISSStore
from services.openai_service import generate_embedding

store = FAISSStore(dim=1536)

def add_document(text: str, meta: dict):
    embedding = generate_embedding(text)
    store.add(embedding, meta)

def search_document(query: str, k=3):
    embedding = generate_embedding(query)
    return store.search(embedding, k)