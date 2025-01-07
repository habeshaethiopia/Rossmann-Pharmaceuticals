# src/app/test_main.py
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Rossmann Sales Prediction API!"}

def test_prediction():
    response = client.post(
        "/api/predict",
        json={
            "store_id": 1,
            "day_of_week": 5,
            "promo": 1,
            "state_holiday": "0",
            "school_holiday": 1,
            "store_type": "a",
            "assortment": "c",
            "competition_distance": 200.5,
        },
    )
    assert response.status_code == 200
    assert "predicted_sales" in response.json()
