# **Laboratory 9**

## **Challenge 1**: Nested Cross-Validation for Model Selection and Tuning
Implement nested cross-validation to compare multiple models and tune their hyperparameters simultaneously.

**Goal**: Prevent biased performance estimates when selecting models using tuning.

**Tools**:
* GridSearchCV or RandomizedSearchCV
* cross_val_score
* Different models like RandomForestClassifier, SVC, KNeighborsClassifier

**What to Observe**:
* Compare outer-loop test scores of each algorithm
* Trade-offs between model complexity and performance stability

## **Challenge 2**: Learning Curves and Validation Curves Analysis

Plot learning and validation curves to diagnose whether a model suffers from high bias or variance.

**Goal**: Use visualization to tune training size or hyperparameters like regularization strength.

**Tools**:
* learning_curve, validation_curve from sklearn.model_selection
* Models like Ridge, LogisticRegression, SVC
* matplotlib for visualization

**What to Observe**:
* Curve convergence (bias/variance trade-off)
* Optimal training data size
* Overfitting/underfitting diagnostics
