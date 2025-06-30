import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data = pd.read_csv("student_data.csv")

# Convert labels to numeric
data['Results'] = data['Results'].map({'Pass': 1, 'Fail': 0})

# Features and target
X = data[['Study_hour', 'sleep_hour', 'Breaks', 'Attendance']]
y = data['Results']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print(f"Accuracy: {acc * 100:.2f}%")

# Save model
joblib.dump(model, 'pass_predictor_model.pkl')
