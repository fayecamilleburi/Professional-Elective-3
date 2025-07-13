# Task 1: Import libraries & load data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For modeling
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Load the dataset (after uploading to Colab)
df = pd.read_csv("heart.csv")  # replace with your file name if different

# Display structure and summary
print(df.head())
print(df.info())
print(df.describe())

# Task 2: Preprocessing
# Check for missing values
print(df.isnull().sum())

# Identify categorical columns if any (this dataset usually has numeric already)
df = pd.get_dummies(df, columns=['cp', 'thal', 'slope'], drop_first=True)

# Normalize / Scale Features
scaler = StandardScaler()
X = df.drop('target', axis=1)
y = df['target']

X_scaled = scaler.fit_transform(X)

# Task 3: Exploratory Data Visualization
# Distribution of the target variable
sns.countplot(x='target', data=df)
plt.title("Distribution of Target Variable")
plt.show()

# Correlation heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Chest pain type vs Target
sns.countplot(x='cp', hue='target', data=pd.read_csv("heart.csv"))
plt.title("Chest Pain Type vs Target")
plt.xlabel("Chest Pain Type")
plt.ylabel("Count")
plt.legend(title="Heart Disease")
plt.show()

# Task 4: Build Predictive Model
# Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a model: Logistic Regression
logistic_reg = LogisticRegression()
logistic_reg.fit(X_train, y_train)
y_pred_log = logistic_reg.predict(X_test)

# Train a model: Random Forest
random_forest = RandomForestClassifier(random_state=42)
random_forest.fit(X_train, y_train)
y_pred_rf = random_forest.predict(X_test)

# Evaluate both models
def get_metrics(y_true, y_pred):
    return {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred),
        'Recall': recall_score(y_true, y_pred),
        'F1 Score': f1_score(y_true, y_pred)
    }

log_metrics = get_metrics(y_test, y_pred_log)
rf_metrics = get_metrics(y_test, y_pred_rf)

print("Logistic Regression Metrics:")
for k, v in log_metrics.items():
    print(f"{k}: {v:.2f}")

print("\nRandom Forest Metrics:")
for k, v in rf_metrics.items():
    print(f"{k}: {v:.2f}")

# Task 5: Visualize Results
# Confusion Matrices
cm_log = confusion_matrix(y_test, y_pred_log)
cm_rf = confusion_matrix(y_test, y_pred_rf)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

sns.heatmap(cm_log, annot=True, fmt='d', cmap='Blues', ax=axs[0])
axs[0].set_title("Logistic Regression Confusion Matrix")
axs[0].set_xlabel("Predicted")
axs[0].set_ylabel("Actual")

sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Greens', ax=axs[1])
axs[1].set_title("Random Forest Confusion Matrix")
axs[1].set_xlabel("Predicted")
axs[1].set_ylabel("Actual")

plt.tight_layout()
plt.show()
