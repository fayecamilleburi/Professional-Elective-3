# Challenge 1

from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
import numpy as np

# Load data
X, y = load_iris(return_X_y=True)

# Prepare models and hyperparameter grids
models = {
    "RandomForest": (RandomForestClassifier(), {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 5, 10]
    }),
    "SVC": (SVC(), {
        'C': [0.1, 1, 10],
        'kernel': ['linear', 'rbf']
    }),
    "KNN": (KNeighborsClassifier(), {
        'n_neighbors': [3, 5, 7]
    })
}

# Outer CV for unbiased performance estimate
outer_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Store results
results = {}

for name, (model, params) in models.items():
    inner_cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=1)
    clf = GridSearchCV(model, param_grid=params, cv=inner_cv)
    nested_scores = cross_val_score(clf, X, y, cv=outer_cv)
    results[name] = nested_scores
    print(f"{name} Nested CV Accuracy: {nested_scores}")
    print(f"{name} Mean Accuracy: {nested_scores.mean():.4f}, Std: {nested_scores.std():.4f}")
