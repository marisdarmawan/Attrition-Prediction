import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the model
model = joblib.load("model.pkl")

# Feature list used in the model
feature_names = [
    'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome',
    'Education', 'EducationField', 'EnvironmentSatisfaction', 'Gender',
    'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',
    'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
    'OverTime', 'PercentSalaryHike', 'PerformanceRating',
    'RelationshipSatisfaction', 'StockOptionLevel', 'TotalWorkingYears',
    'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany',
    'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

# Categorical features to encode
categorical_features = [
    'BusinessTravel', 'Department', 'EducationField', 'Gender',
    'JobRole', 'MaritalStatus', 'OverTime'
]

# Simple label encoder using consistent mapping
def simple_label_encode(df, fit_labels={}):
    df_encoded = df.copy()
    encoders = {}
    for col in categorical_features:
        if col in df.columns:
            if col in fit_labels:
                # Use existing label map
                mapping = fit_labels[col]
            else:
                unique = df[col].unique()
                mapping = {k: i for i, k in enumerate(sorted(unique))}
                fit_labels[col] = mapping
            df_encoded[col] = df[col].map(mapping).fillna(-1).astype(int)
            encoders[col] = mapping
    return df_encoded, fit_labels

st.title("🚪 Employee Attrition Prediction App")

mode = st.sidebar.radio("Choose Prediction Mode", ["🔹 Manual Input", "📂 Upload CSV File"])

if mode == "🔹 Manual Input":
    st.header("Enter Employee Details")

    manual_input = {}
    manual_input['Age'] = st.slider("Age", 18, 60, 30)
    manual_input['BusinessTravel'] = st.selectbox("Business Travel", ['Non-Travel', 'Travel_Rarely', 'Travel_Frequently'])
    manual_input['DailyRate'] = st.number_input("Daily Rate", 100, 1500, 800)
    manual_input['Department'] = st.selectbox("Department", ['Sales', 'Research & Development', 'Human Resources'])
    manual_input['DistanceFromHome'] = st.slider("Distance From Home", 1, 50, 10)
    manual_input['Education'] = st.selectbox("Education (1=Below College, 5=Doctor)", list(range(1, 6)))
    manual_input['EducationField'] = st.selectbox("Education Field", ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources', 'Other'])
    manual_input['EnvironmentSatisfaction'] = st.selectbox("Environment Satisfaction", list(range(1, 5)))
    manual_input['Gender'] = st.selectbox("Gender", ['Male', 'Female'])
    manual_input['HourlyRate'] = st.slider("Hourly Rate", 30, 150, 80)
    manual_input['JobInvolvement'] = st.selectbox("Job Involvement", list(range(1, 5)))
    manual_input['JobLevel'] = st.selectbox("Job Level", list(range(1, 6)))
    manual_input['JobRole'] = st.selectbox("Job Role", ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director',
                                                        'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
    manual_input['JobSatisfaction'] = st.selectbox("Job Satisfaction", list(range(1, 5)))
    manual_input['MaritalStatus'] = st.selectbox("Marital Status", ['Single', 'Married', 'Divorced'])
    manual_input['MonthlyIncome'] = st.number_input("Monthly Income", 1000, 20000, 5000)
    manual_input['MonthlyRate'] = st.number_input("Monthly Rate", 2000, 30000, 15000)
    manual_input['NumCompaniesWorked'] = st.slider("Num Companies Worked", 0, 10, 1)
    manual_input['OverTime'] = st.selectbox("OverTime", ['Yes', 'No'])
    manual_input['PercentSalaryHike'] = st.slider("Percent Salary Hike", 10, 25, 15)
    manual_input['PerformanceRating'] = st.selectbox("Performance Rating", [1, 2, 3, 4])
    manual_input['RelationshipSatisfaction'] = st.selectbox("Relationship Satisfaction", list(range(1, 5)))
    manual_input['StockOptionLevel'] = st.selectbox("Stock Option Level", [0, 1, 2, 3])
    manual_input['TotalWorkingYears'] = st.slider("Total Working Years", 0, 40, 10)
    manual_input['TrainingTimesLastYear'] = st.slider("Training Times Last Year", 0, 10, 3)
    manual_input['WorkLifeBalance'] = st.selectbox("Work Life Balance", list(range(1, 5)))
    manual_input['YearsAtCompany'] = st.slider("Years At Company", 0, 40, 5)
    manual_input['YearsInCurrentRole'] = st.slider("Years In Current Role", 0, 20, 3)
    manual_input['YearsSinceLastPromotion'] = st.slider("Years Since Last Promotion", 0, 15, 1)
    manual_input['YearsWithCurrManager'] = st.slider("Years With Current Manager", 0, 17, 2)

    if st.button("Predict"):
        df_input = pd.DataFrame([manual_input])
        df_encoded, _ = simple_label_encode(df_input)
        prediction = model.predict(df_encoded)[0]
        probability = model.predict_proba(df_encoded)[0][1]

        st.subheader("Prediction Result")
        st.write("Prediction:", "🔴 Resign" if prediction == 1 else "🟢 Stay")
        st.write(f"Probability of Resignation: **{probability:.2%}**")

else:
    st.header("Upload CSV for Batch Prediction")

    uploaded_file = st.file_uploader("Upload CSV file with all features", type=["csv"])

    if uploaded_file is not None:
        df_csv = pd.read_csv(uploaded_file)

        # Show preview
        st.write("Data Preview:")
        st.dataframe(df_csv.head())

        if st.button("Predict"):
            df_encoded, _ = simple_label_encode(df_csv)
            predictions = model.predict(df_encoded)
            probabilities = model.predict_proba(df_encoded)[:, 1]

            df_result = df_csv.copy()
            df_result["Prediction"] = ["Resign" if p == 1 else "Stay" for p in predictions]
            df_result["Resignation_Probability"] = probabilities

            st.write("Prediction Results")
            st.dataframe(df_result)

            csv_download = df_result.to_csv(index=False).encode("utf-8")
            st.download_button("Download Predictions as CSV", data=csv_download, file_name="predicted_attrition.csv", mime="text/csv")
