import faiss
import numpy as np
from langchain_community.vectorstores import FAISS, InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

vector_store: FAISS = None

class FAISSStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add(self, vector, meta):
        vec = np.array([vector]).astype('float32')
        self.index.add(vec)
        self.metadata.append(meta)

    def search(self, vector, k=1):
        vec = np.array([vector]).astype('float32')
        distances, indices = self.index.search(vec, k)
        return [self.metadata[idx] for idx in indices[0] if idx < len(self.metadata)]

    @staticmethod
    def createVectorStore(document_chunks, embeddings):
        vector_store = FAISS.from_documents(document_chunks, embeddings)
        return vector_store

    @staticmethod
    def store_vector_store():
        vector_store.save_local("iAskProdSupport_faiss_index")

    @staticmethod
    def load_vector_store(embeddings):
        loaded_vector_store = FAISS.load_local("iAskProdSupport_faiss_index", embeddings,
                                               allow_dangerous_deserialization=True)
        return loaded_vector_store

    @staticmethod
    def embeddingsAsRetriever(store):
        return store.as_retriever()