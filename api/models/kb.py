from pydantic import BaseModel

class KnowledgeBaseArticle(BaseModel):
    id: int
    question: str
    answer: str