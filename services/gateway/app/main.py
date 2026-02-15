from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine

app = FastAPI(title="FinCore Gateway")

@app.get("/")
def health():
    return {"status": "FinCore Gateway Running"}

@app.get("/health/db")
def db_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"database": "connected"}
    except Exception as e:
        return {"database": "connection failed", "error": str(e)}