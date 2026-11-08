"""
main.py

    FAST API application for IBM telecom churn predictor
"""

from fastapi import FastAPI, HTTPException

from app.schemas import CustomerData
from app.predict import predict_churn

app = FastAPI(
    title = "IBM Telco Customer Churn Predictionn API",
    description= "Predict whether a telecom customer is likely to churn",
    version="1.0.0"
)

@app.get("/")
def root():

    #root endpoint

    return {
        "message": "Welcome to IBM Telco Customer Churn Prediction API"
    }


@app.get("/health")
def health():
        # health check endpoint

    return  {
        "status" : "healthy"
    }


@app.post("/predict")
def predict(customer: CustomerData):

    try:
        result = predict_churn(customer.model_dump())

        return {
            "success" : True,
            "data" : result
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    


