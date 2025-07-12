from db.sqlite_db import db
from api.models.kb import KnowledgeBaseArticle

def add_kb_article(article: KnowledgeBaseArticle):
    db.execute("INSERT INTO kb_articles (id, question, answer) VALUES (?, ?, ?)",
               (article.id, article.question, article.answer))

def get_kb_articles():
    rows = db.execute("SELECT id, question, answer FROM kb_articles", fetch=True)
    return [KnowledgeBaseArticle(id=r[0], question=r[1], answer=r[2]) for r in rows]