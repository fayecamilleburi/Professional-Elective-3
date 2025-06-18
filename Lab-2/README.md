# Messy Customer Dataset

1. **Create a Messy Customer Dataset**
* **Generate Data**: Create a DataFrame using pandas that includes columns such as:
  * CustomerID (unique IDs)
  * Age (numeric data with a few missing values)
  * MonthlySpend (numeric data with some outliers)
  * ContractType (categorical text, e.g., "Monthly", "Yearly")
  * Churn (binary response: 1 for churn, 0 for no churn)
* **Mess It Up**: Manually insert a few missing values (NaN) and inconsistent data entries (e.g., some wrong data types or extra spaces).

2. **Clean and Transform the Data**:
* **Handle Missing Values**: Use techniques like forward fill or filling with the mean.
* **Fix Inconsistencies**: Trim spaces and ensure all text is in a consistent format.

3. **Visualize the Data**:
* **Trend Analysis**: Create plots such as a line plot of Age vs. MonthlySpend and bar charts of ContractType counts.
* **Comparative Visualizations**: Use seaborn to create histograms or boxplots to identify outliers.

4. **Build a Predictive Model**:
* **Prepare the Data**: Split the cleaned dataset into features (e.g., Age, MonthlySpend, ContractType) and labels (Churn). Convert categorical data appropriately (e.g., using dummy variables).
* **Train/Test Split**: Use scikit-learn to split the data.
* **Model Building**: Build a simple model (like logistic regression) to predict Churn
