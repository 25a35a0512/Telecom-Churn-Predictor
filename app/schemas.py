"""
    schemas.py

    Using Pydantic - schemas for validating incomiing prediction requests
"""

from pydantic import BaseModel, Field

class CustomerData(BaseModel):

    #Defining the prediction request fields as column : datatype = field(..., example = "value")

    gender: str = Field(..., example="Male")
    SeniorCitizen: int = Field(..., example=0)
    Partner: str = Field(..., example="Yes")
    Dependents: str = Field(..., example="No")
    tenure: int = Field(..., example=24)

    PhoneService: str = Field(..., example="Yes")
    MultipleLines: str = Field(..., example="No")

    InternetService: str = Field(..., example="Fiber optic")

    OnlineSecurity: str = Field(..., example="No")
    OnlineBackup: str = Field(..., example="Yes")
    DeviceProtection: str = Field(..., example="No")
    TechSupport: str = Field(..., example="No")

    StreamingTV: str = Field(..., example="Yes")
    StreamingMovies: str = Field(..., example="No")

    Contract: str = Field(..., example="Month-to-month")

    PaperlessBilling: str = Field(..., example="Yes")

    PaymentMethod: str = Field(..., example="Electronic check")

    MonthlyCharges: float = Field(..., example=79.85)
    TotalCharges: float = Field(..., example=1862.90)


    class Config: 
        json_schema_extra = {
            "example": {
                "gender" : "Female" ,
                "SeniorCitizen" : 0,
                "Partner" : "Yes",
                "Dependents" : "No",
                "tenure" : 24,
                "PhoneService" : "Yes",
                "MultipleLines" : "No",
                "InternetService" : "Fiber optic",
                "OnlineSecurity" : "No",
                "OnlineBackup" : "Yes",
                "DeviceProtection" : "No",
                "TechSupport" : "No",
                "StreamingTV" : "Yes",
                "StreamingMovies" : "No",
                "Contract" : "Month-to-month",
                "PaperlessBilling" : "Yes",
                "PaymentMethod" : "Electronic check",
                "MonthlyCharges" : 79.85,
                "TotalCharges" : 1862.90
            }
        }