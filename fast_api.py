from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model and encoder
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

# Create FastAPI instance
app = FastAPI()

# Define input format
class HouseInput(BaseModel):
    area: float
    rooms: int
    location: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API 🚀"}

@app.post("/predict")
def predict_price(data: HouseInput):
    # Encode location
    location_encoded = encoder.transform([[data.location]]).toarray()[0]
    features = [data.area, data.rooms] + list(location_encoded)

    # Make prediction
    prediction = model.predict([features])[0]
    return {"predicted_price": round(prediction, 2)}
