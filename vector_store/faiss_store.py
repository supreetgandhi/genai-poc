import faiss
import numpy as np

class FAISSStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.vectors = []
        self.metadata = []

    def add(self, vector, meta):
        vec = np.array([vector]).astype('float32')
        self.index.add(vec)
        self.vectors.append(vector)
        self.metadata.append(meta)

    def search(self, vector, k=1):
        vec = np.array([vector]).astype('float32')
        distances, indices = self.index.search(vec, k)
        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])
        return results
