from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

port = int(os.getenv("PORT", 8000))
db_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Finanzas para Freelancers"}

@app.get("/balance")
def get_balance():
    return {
        "status": "success",
        "balance": 1500.50,
        "currency": "MXN",
        "database_used": db_url
    }