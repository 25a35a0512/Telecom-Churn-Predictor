# 📊 IBM Telco Customer Churn Prediction

An end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn using the **IBM Telco Customer Churn Dataset**.

This project demonstrates the complete Machine Learning deployment lifecycle — from data preprocessing and model training to REST API development, frontend integration, containerization, and cloud deployment.

---

## 🚀 Features

- Data preprocessing and feature engineering
- Comparison of multiple Machine Learning models
- Best model selection using evaluation results
- Model serialization using Joblib
- FastAPI REST API for predictions
- Interactive Streamlit dashboard
- Docker containerization
- Cloud deployment readiness
- Interactive Swagger API documentation

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Machine Learning | Python, Pandas, NumPy, Scikit-learn, Joblib |
| Model | Gradient Boosting Classifier |
| Backend | FastAPI, Pydantic, Uvicorn |
| Frontend | Streamlit, Requests |
| Deployment | Docker, Render, Streamlit Community Cloud |
| Version Control | Git, GitHub |

## 📁 Project Structure

```text
telecom-churn-predictor/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── predict.py
│   └── schemas.py
│
├── frontend/
│   └── app.py
│
├── model/
│   ├── churn_model.pkl
│   └── preprocessor.pkl
│
├── training/
│   ├── data/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   ├── preprocess.py
│   └── train.py
│
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## 📊 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

**Target Variable:** `Churn`

- `Yes` – Customer churned.
- `No` – Customer retained.

The dataset includes features related to:

- Customer demographics
- Account information
- Subscribed services
- Contract details
- Billing information

## 🤖 Machine Learning Pipeline

```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Best Model Selection
   │
   ▼
Model Serialization
   │
   ▼
Prediction
```

**Models evaluated:**

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

**Selected Model:** Gradient Boosting Classifier

## 🌐 System Architecture

```text
             User
               │
               ▼
      Streamlit Frontend
               │
        HTTP POST Request
               │
               ▼
        FastAPI Backend
               │
               ▼
      Gradient Boosting Model
               │
               ▼
       Prediction Result
```

## 🔌 API Endpoints

### 1. Root Endpoint

`GET /`

Returns API information.

### 2. Health Check

`GET /health`

Example response:

```json
{
  "status": "healthy"
}
```

### 3. Customer Churn Prediction

`POST /predict`

**Example Request:**

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 24,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 79.85,
  "TotalCharges": 1862.90
}
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "prediction": "No",
    "probability": 0.12
  }
}
```

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/25a35a0512/telecom-churn-predictor.git

cd telecom-churn-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

### Start the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

`http://127.0.0.1:8000`

Swagger API Documentation:

`http://127.0.0.1:8000/docs`

### Start the Frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t churn-api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 churn-api
```

## 📈 Model Evaluation

| Machine Learning Model | Status |
|---|---|
| Logistic Regression | Evaluated |
| Random Forest | Evaluated |
| Gradient Boosting | Selected |
| XGBoost | Evaluated |

**Final Model:** Gradient Boosting Classifier

*Note: Detailed accuracy, precision, recall, F1-score, and other evaluation metrics can be added here after verifying the actual training results.*

## 📷 Application Preview

### Streamlit Dashboard

<p align="center">
  <img src="assets/dashboard.png" alt="Streamlit Dashboard" width="900">
</p>

### Swagger API Documentation

<p align="center">
  <img src="assets/swagger.png" alt="Swagger API Documentation" width="900">
</p>

### Prediction Result

<p align="center">
  <img src="assets/prediction-result.png" alt="Customer Churn Prediction Result" width="900">
</p>

## 🔮 Future Improvements

- User authentication and authorization
- Batch customer predictions
- Explainable AI using SHAP
- Model performance monitoring
- Automated CI/CD pipeline
- Automated model retraining
- Cloud storage integration

## 👨‍💻 Author

**Bobbili Madhava**

- **GitHub:** [25a35a0512](https://github.com/25a35a0512)
- **LinkedIn:** [Madhava Bobbili](https://www.linkedin.com/in/madhava-bobbili/)
- **LeetCode:** [25a35a0512](https://leetcode.com/u/25a35a0512/)

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you find this project useful, consider giving it a star!
