"""
    training and evaluating the ml models
    for IBM telecom churn prediction dataset

"""
import os
import joblib


import numpy as np
import pandas as pd
from preprocess import load_data, prepare_training_data
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report 

try:
    from xgboost import XGBClassifier
    XGB_AVAILABLE = True
except ImportError:
    XGB_AVAILABLE = False

DATA_PATH = "training/data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
MODEL_PATH = "model"


os.makedirs(MODEL_PATH, exist_ok=True)

def evaluate_model(name, model, X_test, y_test):
    #evaluating the models to select the best one among them

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]  # Get probabilities for the positive class

    metrics = {
        "Model" : name,
        "Accuracy": accuracy_score(y_test, predictions),
        "Precision" : precision_score(y_test, predictions),
        "Recall" : recall_score(y_test, predictions),
        "F1_score" : f1_score(y_test, predictions),
        "ROC_AUC" : roc_auc_score(y_test, probabilities)
    }

    return metrics

def print_results(metrics):
    #printing the results of the model evaluation

    print("\n======================")
    print(f"Model: {metrics['Model']}")
    print("======================")

    for key, value in metrics.items():
        if key != "Model":
            print(f"{key:<12}: {value:.4f}")


def main():
    print("=" * 50)
    print("Loading Dataset...")
    print("=" * 50)

    df = load_data(DATA_PATH)

    (X_train, X_test, y_train, y_test, preprocessor) = prepare_training_data(df)
    

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(random_state=42)
    }


    if XGB_AVAILABLE:
        models["XGBoost"] = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)

    results = []

    trained_models= {}

    print("\n Training Models... \n")

    for name, model in models.items():
        print(f"Training {name}...")

        model.fit(X_train, y_train)

        metrics = evaluate_model(name, model, X_test, y_test)

        print_results(metrics)

        results.append(metrics)

        trained_models[name] = model

    best_model_result = max(results, key=lambda x:x["ROC_AUC"])

    best_model_name = best_model_result["Model"]

    best_model = trained_models[best_model_name]

    print("\n")
    print("=" * 60)
    print(f"Best Model : {best_model_name}")
    print("=" * 60)

    predictions = best_model.predict(X_test)

    print("\n Classification Report")

    print(classification_report(y_test, predictions))

    print("\n Confusion Matrix")

    print(confusion_matrix(y_test, predictions))

    model_path = os.path.join(MODEL_PATH, "churn_model.pkl")

    preprocessor_path = os.path.join(MODEL_PATH, "preprocessor.pkl")

    joblib.dump(best_model, model_path)

    joblib.dump(preprocessor, preprocessor_path)

    print("\n Saved Files")

    print(model_path)

    print(preprocessor_path)

if __name__ == "__main__":
    main()
        