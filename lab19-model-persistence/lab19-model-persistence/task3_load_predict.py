import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load saved model
loaded_model = joblib.load('random_forest_model.joblib')

# Make a prediction
sample_data = [X_test[0]]
predicted_class = loaded_model.predict(sample_data)
print(f"Predicted class: {predicted_class}")