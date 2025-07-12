from fastapi import FastAPI
from api.routes import tickets, kb, rpa

app = FastAPI(title="SupportIQ")

app.include_router(tickets.router, prefix="/api")
app.include_router(kb.router, prefix="/api")
app.include_router(rpa.router, prefix="/api")