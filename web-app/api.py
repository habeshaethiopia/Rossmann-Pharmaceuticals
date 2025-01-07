# web-app/api.py
from fastapi import APIRouter
from pydantic import BaseModel
import joblib

# Load model
model_path = "models/trained_model.pkl"
model = joblib.load(model_path)

app = APIRouter()

class PredictionInput(BaseModel):
    store_id: int
    day_of_week: int
    promo: int
    state_holiday: str
    school_holiday: int
    store_type: str
    assortment: str
    competition_distance: float

@app.post("/predict")
async def predict(input_data: PredictionInput):
    input_dict = input_data.dict()
    features = [
        input_dict['store_id'],
        input_dict['day_of_week'],
        input_dict['promo'],
        input_dict['state_holiday'],
        input_dict['school_holiday'],
        input_dict['store_type'],
        input_dict['assortment'],
        input_dict['competition_distance'],
    ]
    prediction = model.predict([features])
    return {"predicted_sales": prediction[0]}
