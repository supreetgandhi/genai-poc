import os
from db.sqlite_db import db
from api.models.kb import KnowledgeBaseArticle
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

docs = []

def add_kb_article(article: KnowledgeBaseArticle):
    db.execute("INSERT INTO kb_articles (id, question, answer) VALUES (?, ?, ?)",
               (article.id, article.question, article.answer))

def get_kb_articles():
    rows = db.execute("SELECT id, question, answer FROM kb_articles", fetch=True)
    return [KnowledgeBaseArticle(id=r[0], question=r[1], answer=r[2]) for r in rows]

def fetch_kb_documents():
    paths = [
        "./docs/Artificial_Intelligence_in_Financial_Services_2025.pdf",
        "./docs/FinancialLiteracyArroundWorld.pdf"
    ]
    absolute_paths = [os.path.abspath(path) for path in paths]
    [docs.extend(PyMuPDFLoader(path).load()) for path in absolute_paths]
    # print(docs)
def splittingDocumentsIntoChunks():
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=100,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    docs_splits = text_splitter.split_documents(docs)
    # docs_splits[0].page_content.strip()
    return docs_splits