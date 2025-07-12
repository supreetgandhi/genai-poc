from fastapi import APIRouter
from api.models.ticket import Ticket
from db.sqlite_db import db
from services import embedding_search

router = APIRouter()

@router.post("/tickets/")
def create_ticket(ticket: Ticket):
    db.execute("INSERT INTO tickets (id, title, description, status) VALUES (?, ?, ?, ?)",
               (ticket.id, ticket.title, ticket.description, ticket.status))
    embedding_search.add_document(ticket.description, {"ticket_id": ticket.id, "title": ticket.title})
    return {"message": "Ticket created", "ticket": ticket}

@router.get("/tickets/")
def list_tickets():
    rows = db.execute("SELECT id, title, description, status FROM tickets", fetch=True)
    return [{"id": r[0], "title": r[1], "description": r[2], "status": r[3]} for r in rows]

@router.post("/tickets/recommend/")
def recommend_solution(query: dict):
    results = embedding_search.search_document(query["query"], k=3)
    return {"recommendations": results}