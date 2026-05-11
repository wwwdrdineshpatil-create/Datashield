from fastapi import FastAPI
from pydantic import BaseModel
from datashield import analyze_data

app = FastAPI()

class InputData(BaseModel):
    value: float

@app.get("/")
def home():
    return {"messaaes": "Datashield API is running"}

@app.post("/predict")
def predict(data: InputData):
    processed = preprocess(data.value)
    result = model.predict(processed)
    return {"result": result}
    
