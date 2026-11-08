"""
 predict.py
    Here - loads the trained model and preprocesses, performs inference, and prediction results.
"""

import pandas as pd
import joblib
from pathlib import Path

#load model and preprocessor only once

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR/"model"/"churn_model.pkl"
PREPROCESSOR_DIR = BASE_DIR/"model"/"preprocessor.pkl"

model = joblib.load(MODEL_DIR)
preprocessor = joblib.load(PREPROCESSOR_DIR)

#--------------------------------------
# Prediction function
#--------------------------------------

def predict_churn(customer_data: dict):

    input_df = pd.DataFrame([customer_data])

    input_df["SeniorCitizen"] = input_df["SeniorCitizen"].astype(str)

    input_df["TotalCharges"] = pd.to_numeric(input_df["TotalCharges"], errors= "coerce")

    processed_data = preprocessor.transform(input_df)

    print(processed_data.shape)

    prediction = model.predict(processed_data)[0]

    probability = model.predict_proba(processed_data)[0][1]

    return {
        "prediction" : "Yes" if prediction == 1 else "No",
        "probability" : round(float(probability), 4)
    }