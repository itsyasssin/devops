import os
from pathlib import Path

import joblib
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

VERSION = os.getenv("APP_VERSION", "dev")
model = joblib.load(os.getenv("MODEL_PATH", "model.joblib"))
app = FastAPI(title="House price predictor", version=VERSION)


class House(BaseModel):
    size: float = Field(gt=0, description="m2")
    bedrooms: int = Field(ge=1, le=10)
    age: float = Field(ge=0)


@app.get("/")
def ui():
    return FileResponse(Path(__file__).parent / "static" / "index.html")


@app.get("/health")
def health():
    return {"status": "ok", "version": VERSION}


@app.post("/predict")
def predict(h: House):
    price = float(model.predict([[h.size, h.bedrooms, h.age]])[0])
    return {"price": round(price, 2), "version": VERSION}
