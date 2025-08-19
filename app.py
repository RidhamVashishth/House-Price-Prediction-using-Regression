# -*- coding: utf-8 -*-
import streamlit as st
import joblib
import pandas as pd

# Load trained model
final_model = joblib.load("house_price_model.pkl")

st.title("House Price Predictor")

# Feature input widgets
OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)
TotalBsmtSF = st.number_input("Total Basement Area (sqft)", min_value=0, max_value=10000, value=800)
Electrical = st.selectbox("Electrical", ["SBrkr", "FuseA", "FuseF", "FuseP", "Mix"])
GrLivArea = st.number_input("Above Ground Living Area (sqft)", min_value=0, max_value=10000, value=1500)
FullBath = st.number_input("Full Bathrooms", min_value=0, max_value=5, value=2)
GarageType = st.selectbox("Garage Type", ["Attchd", "Detchd", "BuiltIn", "CarPort", "Basment", "2Types", "NA"])
GarageCars = st.number_input("Garage Cars", min_value=0, max_value=5, value=2)
GarageArea = st.number_input("Garage Area (sqft)", min_value=0, max_value=2000, value=500)
Fence = st.selectbox("Fence", ['NotAvailable', 'Available'])
MiscFeature = st.selectbox("Misc Feature", ["Yes", "No"])

# Encoding dictionaries
elec_dic = {
    'SBrkr': 0.9227,
    'FuseA': 0.0590,
    'FuseF': 0.0154,
    'FuseP': 0.0018,
    'Mix': 0.0009
}

garage_dic = {
    'Attchd': 0.5727,
    'Detchd': 0.2863,
    'BuiltIn': 0.0636,
    'CarPort': 0.0527,
    'Basment': 0.0136,
    '2Types': 0.0063,
    'NA': 0.0045
}

# Encode categorical inputs
Electrical_encoded = elec_dic.get(Electrical, 0)
GarageType_encoded = garage_dic.get(GarageType, 0)
Fence_NotAvailable = 1 if Fence == "NotAvailable" else 0
MiscFeature_Yes = 1 if MiscFeature == "Yes" else 0

# Final input dataframe
input_data = pd.DataFrame([{
    "OverallQual": OverallQual,
    "YearBuilt": YearBuilt,
    "TotalBsmtSF": TotalBsmtSF,
    "Electrical": Electrical_encoded,
    "GrLivArea": GrLivArea,
    "FullBath": FullBath,
    "GarageType": GarageType_encoded,
    "GarageCars": GarageCars,
    "GarageArea": GarageArea,
    "Fence_NotAvailable": Fence_NotAvailable,
    "MiscFeature_Yes": MiscFeature_Yes
}])

# Predict button
if st.button("Predict Price"):
    prediction = final_model.predict(input_data)[0]  
    st.success(f"Predicted House Price: ${prediction:,.2f}")
