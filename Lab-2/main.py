import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Set file name for saving dataset
DATA_FILE = 'data.csv'

# 1. Create a Messy Customer Dataset
print("1. Generating a new messy customer dataset")

np.random.seed(42)  # For reproducibility

data = {
    'CustomerID': range(101, 151),
    'Age': np.random.randint(18, 70, 50).astype(float), # Keep as float initially to allow NaN
    'MonthlySpend': np.random.uniform(20, 200, 50),
    'ContractType': np.random.choice(['Monthly', 'Yearly', 'Two Year'], 50),
    'Churn': np.random.choice([0, 1], 50, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Messing it up intentionally
df.loc[[5, 12, 28], 'Age'] = np.nan
df.loc[[10, 35], 'MonthlySpend'] = np.nan
df.loc[[20, 45], 'MonthlySpend'] = [500.0, 750.0]
df.loc[3, 'ContractType'] = ' monthly '
df.loc[15, 'ContractType'] = 'YEARLY'
df.loc[25, 'ContractType'] = 'Two Year '
df.loc[40, 'MonthlySpend'] = 'abc'

# Save messy dataset
df.to_csv(DATA_FILE, index=False)

print("\nMessy Dataset Preview:")
print(df.head())
print("\nData Types and Null Values:")
print(df.info())


# 2. Clean and Transform the Data
print("\n2. Cleaning and transforming the data")

df_cleaned = df.copy()

# Clean ContractType: strip spaces & standardize casing
df_cleaned['ContractType'] = df_cleaned['ContractType'].astype(str).str.strip().str.capitalize()

# Convert MonthlySpend to numeric (coerce errors like 'abc' to NaN)
df_cleaned['MonthlySpend'] = pd.to_numeric(df_cleaned['MonthlySpend'], errors='coerce')

# Handle missing Age: Fill with rounded mean, then convert to integer
mean_age = df_cleaned['Age'].mean()
df_cleaned['Age'].fillna(round(mean_age), inplace=True) # Round the mean before filling
df_cleaned['Age'] = df_cleaned['Age'].astype(int) # Convert to integer after filling

# Fill MonthlySpend using forward fill
df_cleaned['MonthlySpend'].fillna(method='ffill', inplace=True)

print("\nCleaned Dataset Preview:")
print(df_cleaned)
print("\nUpdated Info After Cleaning:")
print(df_cleaned.info())


# 3. Visualize the Data
print("\n3. Visualizing the data")

plt.figure(figsize=(15, 10))

# Plot 1: Age vs MonthlySpend
plt.subplot(2, 2, 1)
sns.scatterplot(x='Age', y='MonthlySpend', data=df_cleaned)
plt.title('Age vs MonthlySpend')
plt.grid(True)

# Plot 2: ContractType counts
plt.subplot(2, 2, 2)
sns.countplot(x='ContractType', data=df_cleaned, palette='Set2')
plt.title('Customer Count by Contract Type')

# Plot 3: MonthlySpend histogram with KDE
plt.subplot(2, 2, 3)
sns.histplot(df_cleaned['MonthlySpend'], bins=15, kde=True)
plt.title('MonthlySpend Distribution')

# Plot 4: Boxplot to show outliers
plt.subplot(2, 2, 4)
sns.boxplot(y='MonthlySpend', data=df_cleaned)
plt.title('Boxplot of MonthlySpend')

plt.tight_layout()
plt.show()

# 4. Build a Predictive Model
print("\n4. Building a predictive model")

# Prepare data
X = df_cleaned[['Age', 'MonthlySpend', 'ContractType']]
y = df_cleaned['Churn']

# One-hot encode categorical ContractType (drop_first to avoid multicollinearity)
X = pd.get_dummies(X, columns=['ContractType'], drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Model: Logistic Regression
model = LogisticRegression(solver='liblinear', random_state=42)
model.fit(X_train, y_train)

# Predictions & Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(report)
