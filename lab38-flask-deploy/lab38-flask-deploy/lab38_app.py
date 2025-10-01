from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "Welcome to the Flask Model Deployment!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prediction = model.predict([data])
    return str(prediction)

@app.route("/predict-form", methods=["GET", "POST"])
def predict_form():
    if request.method == "POST":
        data = request.form["input_data"]
        input_data = np.array([float(x) for x in data.split(",")])
        prediction = model.predict([input_data])
        return f"Prediction: {prediction}"
    return '''
        <form method="post">
            Input Data: <input type="text" name="input_data">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
