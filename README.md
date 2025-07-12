📚 genai-poc

🚀 AI-powered support assistant to help support staff analyze tickets, recommend solutions, and build a knowledge base. Includes RPA triggers and extensibility.
✨ Features

✅ Analyze support tickets and recommend solutions based on historical tickets & knowledge base (KB) using embeddings + FAISS
✅ Build & maintain KB articles (manually and import from CSV/JSON)
✅ Use RPA to trigger automated actions
✅ Consume KB from various sources (CSV/JSON for now, extensible)
✅ FastAPI-based backend with a Postman Collection for easy testing
✅ SQLite (in-memory) for persistence, easy to replace with PostgreSQL if needed

🗂 Project Structure

supportiq/
├── api/                 # FastAPI routes & models
├── db/                  # SQLite in-memory DB
├── services/            # Business logic (KB, ticket, recommendation, RPA)
├── vector_store/        # FAISS vector store for similarity search
├── config/              # App settings
├── supportiq.postman_collection.json
├── requirements.txt
└── README.md
⚙️ Setup & Run

📋 Requirements
Python 3.8+
virtualenv (optional)
🔧 Install dependencies
pip install -r requirements.txt
🚀 Run the app
uvicorn api.main:app --reload
Server runs at:
➡️ http://127.0.0.1:8000

📮 API Endpoints

Method	Endpoint	Description
POST	/api/tickets/	Create a support ticket
GET	/api/tickets/	List all tickets
POST	/api/tickets/recommend/	Recommend similar tickets or KB articles
POST	/api/kb/	Add KB article
GET	/api/kb/	List KB articles
POST	/api/kb/import/csv	Import KB from CSV
POST	/api/kb/import/json	Import KB from JSON
POST	/api/rpa/trigger/{action}	Trigger RPA action
🧪 Testing with Postman

Import the provided Postman collection:

supportiq.postman_collection.json
It contains requests for:

Creating & listing tickets
Recommending solutions
Adding & listing KB articles
Importing KB
Triggering RPA
🧹 Notes

Uses in-memory SQLite, so data is reset every restart
Uses FAISS to store vector embeddings of tickets/KB for similarity search
openai package is used for embeddings/completions – configure your API key in services/openai_service.py
