import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB

# 1. Sample text dataset (spam vs. ham)
messages = [
    "Congratulations! You’ve won a free ticket.",
    "Meeting today at 5pm.",
    "Claim your cash prize now!",
    "Don’t forget the grocery list.",
    "URGENT: Your account has been flagged!",
    "Let’s catch up over coffee tomorrow.",
    "Free access to exclusive content!",
    "Team meeting rescheduled to Monday.",
    "Win cash now. Click the link!",
    "Pick up your prescription at the pharmacy."
]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam

# 2. Vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)
y = labels

# 3. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Define models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "k-NN (k=3)": KNeighborsClassifier(n_neighbors=3),
    "Naïve Bayes": MultinomialNB()
}

# 5. Train, predict, evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\n {name} Results")
    print(classification_report(y_test, y_pred, target_names=["Not Spam", "Spam"]))
