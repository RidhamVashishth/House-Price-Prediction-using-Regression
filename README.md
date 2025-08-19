# House Price Prediction using Regression

## Project Overview

This project focuses on predicting housing prices using machine learning regression models. The dataset contains details of houses such as area, quality, garage type, and electrical system. These features are analyzed to identify their relationship with house prices and build a predictive model.

The final solution is deployed as an interactive **Streamlit web app**, where users can input property details and get a price prediction.

---

## Dataset

* The dataset contains both **numerical features** (e.g., `LotArea`, `OverallQual`, `GrLivArea`, `GarageCars`, `TotalBsmtSF`) and **categorical features** (e.g., `GarageType`, `Electrical`).
* **Target variable:** `SalePrice` (the house price).
* **Size:** The dataset has over 1,400 records.
* **Numerical features** capture areas, counts, and quality scores.
* **Categorical features** capture property characteristics like type of garage and electrical system.

This mix of data required careful **encoding** and **statistical testing** before modeling.

---

## Data Exploration and Cleaning

* **Exploratory Data Analysis (EDA)** included studying distributions of prices and features, detecting missing values, and checking outliers.
* Correlation heatmaps showed strong positive correlation between `GrLivArea`, `OverallQual`, and `SalePrice`.
* Outliers in variables like `GrLivArea` were treated to improve regression results.

---

## Encoding and Feature Engineering

* **Categorical variables** such as `Electrical` and `GarageType` were encoded using mapping/frequency encoding to convert them into numeric form.
* This allowed the models to capture their influence on house prices.
* Example: `Electrical` categories were mapped based on frequency, while garage types were assigned representative codes.

---

## Statistical Tests

* **Correlation Analysis:** Showed that `OverallQual` (overall quality of the house) and `GrLivArea` (above-ground living area) had the highest correlation with `SalePrice`.
* **ANOVA / Hypothesis Testing:** Categorical features like `GarageType` and `Electrical` showed statistically significant differences in mean house prices across their categories.
* These results validated that both **numerical and categorical variables** are essential for modeling.

---

## Model Building

The following regression models were trained and evaluated:

1. **Linear Regression**
2. **Lasso Regression**
3. **Ridge Regression**
4. **Random Forest Regressor**
5. **XGBoost Regressor**

---

## Model Comparison

Models were compared using multiple evaluation metrics:

* **R² Score** – measures how well the model explains variance in prices.
* **Root Mean Squared Error (RMSE)** – penalizes large prediction errors.
* **Mean Absolute Error (MAE)** – gives the average magnitude of errors.

**Focus Metric:**

* While all metrics were reviewed, **R² score** and **RMSE** were given more weight since they best reflect prediction accuracy and error distribution.

**Findings:**

* Linear models (Linear, Ridge, Lasso) gave reasonable baseline results.
* **Random Forest** and **XGBoost** outperformed them with higher R² and lower RMSE.
* After hyperparameter tuning, **XGBoost** achieved the best balance of accuracy and generalization.

---

## Hyperparameter Tuning

* For Random Forest and XGBoost, hyperparameter tuning was carried out using **GridSearchCV/RandomizedSearchCV**.
* Key parameters tuned included `n_estimators`, `max_depth`, and `learning_rate`.
* This step reduced overfitting and improved test-set accuracy.

---

## Final Model

* The **Random Forest model** was selected as the final model due to its strong predictive performance.
* It was saved using **joblib** as `house_price_model.pkl`.
* This model is loaded into the Streamlit app for deployment.

---

## Deployment

* Built an interactive **Streamlit app** for house price prediction.
* Users enter features like living area, garage type, and quality score.
* The app loads the trained model and predicts the house price in real-time.

---

## Tools and Libraries Used

* **Python**: pandas, numpy, matplotlib, seaborn, scikit-learn, joblib
* **Machine Learning Models:** Linear Regression, Ridge, Lasso, Random Forest, XGBoost
* **Streamlit** for deployment

---

## Key Takeaways

* EDA and statistical testing confirmed which features significantly impact house prices.
* Encoding categorical variables properly ensures they contribute to prediction.
* Ensemble models (Random Forest, XGBoost) performed better than linear models.
* Hyperparameter tuning improved accuracy and generalization.
* Streamlit made it easy to deploy the final model into a user-friendly app.

---

Do you want me to **add a short "Results Summary Table"** in the README showing R², RMSE, and MAE for each model (so it’s easy to see why XGBoost was final)?
