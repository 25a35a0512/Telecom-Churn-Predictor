"""
    An User Interface to interact and predict

"""

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"


st.set_page_config(
    page_title="IBM Telco Churn Prediction",
    page_icon="📊",
    layout="wide"
)

with st.sidebar:

    st.title("📊 Churn Predictor")

    st.markdown("---")

    st.markdown("### Model")

    st.info("Gradient Boosting Classifier")

    st.markdown("### Backend")

    st.success("FastAPI")

    st.markdown("### Frontend")

    st.success("Streamlit")

    st.markdown("### Dataset")

    st.write("IBM Telco Customer Churn")

    st.markdown("---")

    st.caption("Built with Knowledge using Python")

st.title("📊 IBM Telco Customer Churn Prediction")

st.caption(
    "Predict whether a telecom customer is likely to leave the telecom service."
)

st.divider()



with st.form("prediction_form"):
    st.subheader("Customer Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender", ["Male", "Female"]
        )

        senior = st.selectbox(
            "Senior Citizen", [0,1]
        )

        partner = st.selectbox(
            "Partner", ["Yes", "No"]
        )

        dependents = st.selectbox(
            "Dependents", ["Yes", "No"]
        )

        tenure = st.number_input(
            "Tenure(Months)", 
            min_value=0,
            max_value=100,
            value=12
        )

    with col2:
        phone = st.selectbox(
            "Phone Service", ["Yes", "No"]
        )

        multiple = st.selectbox(
            "Multiple Lines",
            ["Yes", "No", "No phone service"]
        )

        internet = st.selectbox(
            "Internet Service", ["DSL", "Fiber optic", "No"]
        )

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

        payment = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer( automatic)",
                "Credic card (automatic)"
            ]
        )

    st.subheader("Additional Services")

    col3, col4 = st.columns(2)

    with col3: 
        online_security = st.selectbox(
            "Online Security", ["Yes", "No", "No internet service"]
        )

        online_backup = st.selectbox(
            "Online Backup", ["Yes", "No", "No internet service"]
        )

        device = st.selectbox(
            "Device Protection", ["Yes", "No", "No internet service"]
        )

    with col4: 
        tech = st.selectbox(
            "Tech Support", ["Yes", "No", "No internet service"]
        )

        tv = st.selectbox(
            "Streaming TV", ["Yes", "No", "No internet service"]
        )

        movies = st.selectbox(
            "Streaming Movies", ["Yes", "No", "No internet service"]
        )

    st.subheader("Billing")

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    monthly = st.number_input(
        "Monthly Charges", value=70.0
    )

    total = st.number_input(
        "Total Charges",
        value=1500.0
    )

    predict = st.form_submit_button(
        "Predict Churn"
    )

    if predict:

        customer_data = {
            "gender": gender,
            "SeniorCitizen": senior,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": phone,
            "MultipleLines": multiple,
            "InternetService": internet,
            "OnlineSecurity": online_security,
            "OnlineBackup": online_backup,
            "DeviceProtection": device,
            "TechSupport": tech,
            "StreamingTV": tv,
            "StreamingMovies": movies,
            "Contract": contract,
            "PaperlessBilling": paperless,
            "PaymentMethod": payment,
            "MonthlyCharges": monthly,
            "TotalCharges": total
        }

        try:
            with st.spinner("Predicting..."):
                response = requests.post(
                    API_URL,
                    json = customer_data,
                    timeout=10
                )

            if response.status_code == 200:
                result = response.json()["data"]
                
                prediction = result["prediction"]
                probability = result["probability"]

                st.success("Prediction completed successfully!")
                
                if prediction == "Yes":
                    pred_statement = "Customer is likely to Churn\n\n"

                else: 
                    
                    pred_statement = "Customer is NOT likely to Churn\n\n"
                    
                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Prediction",
                         pred_statement
                    )

                with col2:
                    st.metric(
                        "Probability",
                       
                        f"{probability*100:.2f}%"

                    )


                with st.expander("View Submitted Data"):
                    st.json(customer_data)


            else:
                st.error(response.text)

        except requests.exceptions.ConnectionError:
            st.error("Unable to connect to FastAPI server.")

        except requests.exceptions.Timeout:
            st.error(" Request timed out.")

        except Exception as e:
            st.error(str(e))


        




st.divider()

st.caption(
    "IBM Telco Customer Churn Prediction | "
    "Machine Learning Engineering Capstone"
)