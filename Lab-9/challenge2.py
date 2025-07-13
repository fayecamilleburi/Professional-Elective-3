# Challenge 2

# Learning Curve
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve
from sklearn.datasets import load_iris

# Load data
X, y = load_iris(return_X_y=True)

# Model and range of training sizes
model = LogisticRegression(max_iter=200)
train_sizes, train_scores, valid_scores = learning_curve(
    model, X, y, train_sizes=np.linspace(0.1, 1.0, 10), cv=5, scoring='accuracy'
)

# Calculate mean and std
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
valid_mean = np.mean(valid_scores, axis=1)
valid_std = np.std(valid_scores, axis=1)

# Plot learning curve
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, 'o-', label="Training score")
plt.plot(train_sizes, valid_mean, 'o-', label="Cross-validation score")
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1)
plt.fill_between(train_sizes, valid_mean - valid_std, valid_mean + valid_std, alpha=0.1)
plt.xlabel("Training Set Size")
plt.ylabel("Accuracy")
plt.title("Learning Curve (Logistic Regression)")
plt.legend(loc="best")
plt.grid(True)
plt.tight_layout()
plt.show()

# Validation Curve
from sklearn.model_selection import validation_curve
from sklearn.svm import SVC

param_range = np.logspace(-3, 2, 6)
train_scores, valid_scores = validation_curve(
    SVC(), X, y, param_name='C', param_range=param_range, cv=5, scoring='accuracy'
)

train_mean = np.mean(train_scores, axis=1)
valid_mean = np.mean(valid_scores, axis=1)

# Plot validation curve
plt.figure(figsize=(10, 6))
plt.semilogx(param_range, train_mean, 'o-', label='Training score')
plt.semilogx(param_range, valid_mean, 'o-', label='Cross-validation score')
plt.xlabel('Regularization Strength (C)')
plt.ylabel('Accuracy')
plt.title('Validation Curve (SVC)')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()
