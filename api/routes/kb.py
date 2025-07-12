from fastapi import APIRouter, UploadFile
from api.models.kb import KnowledgeBaseArticle
from services import kb_manager

import csv
import json

router = APIRouter()

@router.post("/kb/")
def add_kb_article(article: KnowledgeBaseArticle):
    kb_manager.add_kb_article(article)
    return {"message": "KB Article added", "article": article}

@router.get("/kb/")
def list_kb_articles():
    articles = kb_manager.get_kb_articles()
    return articles

@router.post("/kb/import/csv")
async def import_kb_csv(file: UploadFile):
    contents = await file.read()
    reader = csv.DictReader(contents.decode().splitlines())
    for row in reader:
        article = KnowledgeBaseArticle(id=int(row["id"]), question=row["question"], answer=row["answer"])
        kb_manager.add_kb_article(article)
    return {"message": "KB imported from CSV"}

@router.post("/kb/import/json")
async def import_kb_json(file: UploadFile):
    contents = await file.read()
    data = json.loads(contents)
    for row in data:
        article = KnowledgeBaseArticle(id=int(row["id"]), question=row["question"], answer=row["answer"])
        kb_manager.add_kb_article(article)
    return {"message": "KB imported from JSON"}