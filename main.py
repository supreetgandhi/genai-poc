import os

from langchain_community.vectorstores import FAISS

from services import openai_service
from services.embedding_search import getEmbeddings
from services.kb_manager import fetch_kb_documents, splittingDocumentsIntoChunks
from services.openai_service import generate_query_or_response
from tools.agent_tools import retriever_tool
from vector_store.faiss_store import FAISSStore


index_path = "iAskProdSupport_faiss_index"
vector_store: FAISS

if os.path.exists(os.path.join(index_path, "index.faiss")) and \
   os.path.exists(os.path.join(index_path, "index.pkl")):
    vector_store = FAISSStore.load_vector_store()
else:
    fetch_kb_documents()
    docs_splits = splittingDocumentsIntoChunks()
    embeddings = getEmbeddings()
    vector_store = FAISSStore.createVectorStore(docs_splits, embeddings)

retriever = FAISSStore.embeddingsAsRetriever(vector_store)

retrieverTool = retriever_tool(retriever=retriever)
# retrieverTool.invoke({"query": "Why is AI needed in finance"})
response = generate_query_or_response("Demo")
print(response)