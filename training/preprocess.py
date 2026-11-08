""""
preprocessing utilities for the IBM telecom Customer Churn dataset

"""

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split




def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the IBM telecom Customer Churn dataset from a CSV file.

    Args:
        path (str): The file path to the CSV file.
    """

    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # performing dataset-specific cleaning

    df = df.copy()

    if "customerID" in df.columns:
        df.drop(columns="customerID", inplace=True)

    #converting total charges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')

    #Senior citizen into categorical

    df['SeniorCitizen'] = df['SeniorCitizen'].astype(str)

    #Encode targets

    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    return df

def split_features_target(df: pd.DataFrame):

    X = df.drop(["Churn"], axis = 1)
    y = df["Churn"]

    return X, y


def build_preprocessor(X: pd.DataFrame):

   

    numeric_features = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
         ]
    
    categorical_features = [column for column in X.columns if column not in numeric_features]

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer",
             SimpleImputer(strategy="median"))
             ,
             ("scaler",
              StandardScaler()
              )
        ]
    )
    
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                numeric_pipeline,
                numeric_features
            ),
            (
                "cat",
                categorical_pipeline,
                categorical_features
            )
        ]
    )

    return preprocessor

def prepare_training_data(df: pd.DataFrame, test_size = 0.2, random_state= 42):

    df = clean_data(df)

    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state = random_state, stratify=y)

    preprocessor = build_preprocessor(X_train)

    X_train = preprocessor.fit_transform(X_train)

    X_test = preprocessor.transform(X_test)

    return (
        X_train,
        X_test, 
        y_train,
        y_test,
        preprocessor
    )


    