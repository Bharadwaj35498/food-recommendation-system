from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

from data_preprocessing import load_and_preprocess_data

X, y, encoders = load_and_preprocess_data()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print("Model Training Completed")
print("Accuracy:", accuracy)

joblib.dump(model, "models/food_model.pkl")
joblib.dump(encoders, "models/encoders.pkl")
