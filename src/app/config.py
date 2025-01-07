# src/app/config.py
import os

class Config:
    MODEL_PATH = os.getenv("MODEL_PATH", "models/trained_model.pkl")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
