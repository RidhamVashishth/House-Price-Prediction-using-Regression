{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abdc1853-271d-4e42-9023-6ef86e834f90",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "\n",
    "# Load trained model\n",
    "final_model, elec_dic, garage_dic = joblib.load(\"house_price_model.pkl\")\n",
    "\n",
    "st.title(\"House Price Predictor\")\n",
    "\n",
    "# Feature input widgets\n",
    "OverallQual = st.slider(\"Overall Quality (1-10)\", 1, 10, 5)\n",
    "YearBuilt = st.number_input(\"Year Built\", min_value=1800, max_value=2025, value=2000)\n",
    "TotalBsmtSF = st.number_input(\"Total Basement Area (sqft)\", min_value=0, max_value=10000, value=800)\n",
    "Electrical = st.selectbox(\"Electrical\", [\"SBrkr\", \"FuseA\", \"FuseF\", \"FuseP\", \"Mix\"])\n",
    "GrLivArea = st.number_input(\"Above Ground Living Area (sqft)\", min_value=0, max_value=10000, value=1500)\n",
    "FullBath = st.number_input(\"Full Bathrooms\", min_value=0, max_value=5, value=2)\n",
    "GarageType = st.selectbox(\"Garage Type\", [\"Attchd\", \"Detchd\", \"BuiltIn\", \"CarPort\", \"Basment\", \"2Types\", \"NA\"])\n",
    "GarageCars = st.number_input(\"Garage Cars\", min_value=0, max_value=5, value=2)\n",
    "GarageArea = st.number_input(\"Garage Area (sqft)\", min_value=0, max_value=2000, value=500)\n",
    "Fence = st.selectbox(\"Fence\", ['NotAvailable', 'Available'])\n",
    "MiscFeature = st.selectbox(\"Misc Feature\", [\"Yes\", \"No\"])\n",
    "\n",
    "# Collect inputs into a dataframe\n",
    "input_df = pd.DataFrame([[OverallQual, YearBuilt, TotalBsmtSF, Electrical, GrLivArea,\n",
    "                          FullBath, GarageType, GarageCars, GarageArea, Fence, MiscFeature]],\n",
    "                        columns=['OverallQual', 'YearBuilt', 'TotalBsmtSF', 'Electrical', 'GrLivArea',\n",
    "                                 'FullBath', 'GarageType', 'GarageCars', 'GarageArea', 'Fence',\n",
    "                                 'MiscFeature'])\n",
    "\n",
    "Electrical_encoded = elec_dic.get(Electrical, 0)\n",
    "GarageType_encoded = garage_dic.get(GarageType, 0)\n",
    "Fence_NotAvailable = 1 if Fence == \"NotAvailable\" else 0\n",
    "MiscFeature_Yes = 1 if MiscFeature == \"Yes\" else 0\n",
    "\n",
    "input_data = pd.DataFrame([{\n",
    "    \"OverallQual\": OverallQual,\n",
    "    \"YearBuilt\": YearBuilt,\n",
    "    \"TotalBsmtSF\": TotalBsmtSF,\n",
    "    \"Electrical\": Electrical_encoded,\n",
    "    \"GrLivArea\": GrLivArea,\n",
    "    \"FullBath\": FullBath,\n",
    "    \"GarageType\": GarageType_encoded,\n",
    "    \"GarageCars\": GarageCars,\n",
    "    \"GarageArea\": GarageArea,\n",
    "    \"Fence_NotAvailable\": Fence_NotAvailable,\n",
    "    \"MiscFeature_Yes\": MiscFeature_Yes\n",
    "}])\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"Predict Price\"):\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    st.success(f\"Predicted House Price: ${prediction:,.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "028d6c6d-ff10-4dcb-a995-88c85cfdc29a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00fea70f-eb0f-4932-8075-405a954bc923",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a95a52b9-02fa-4475-a4f8-47cee2dbbb1d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "026d8acd-03a6-4309-a396-b77f41156f49",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1c9daaf-fff8-41a9-9b00-8102973f0ecc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
