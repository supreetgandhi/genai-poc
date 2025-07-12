import faiss
import numpy as np

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