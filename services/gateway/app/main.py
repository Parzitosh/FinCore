from fastapi import FastAPI
from app.database import test_connection

app = FastAPI(title="FinCore Gateway")

@app.get("/")
def health():
    return {"status": "FinCore Gateway Running"}

@app.get("/health/db")
def db_health():
    if test_connection():
        return {"database": "connected"}
    return {"database": "connection failed"}