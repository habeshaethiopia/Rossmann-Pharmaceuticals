# src/app/main.py
from fastapi import FastAPI
from web_app.api import app as api_router

app = FastAPI()

# Include API routes
app.include_router(api_router, prefix="/api", tags=["predictions"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Rossmann Sales Prediction API!"}
