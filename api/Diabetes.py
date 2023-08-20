from flask import Blueprint, request, jsonify
import numpy as np
import pickle

# Create a Blueprint
diabetes_bp = Blueprint("diabetes", __name__)

# Load the pre-trained GradientBoostingClassifier model
model_diabetes = pickle.load(open('./pickle/Pickle_Diabetes.pkl', 'rb'))


@diabetes_bp.route("/predict_diabetes", methods=["POST"])
def predict_diabetes():
    if request.method == "POST":
        input_data = request.json
        feature_values = np.array([
            float(input_data["Pregnancies"]),
            float(input_data["Glucose"]),
            float(input_data["BloodPressure"]),
            float(input_data["SkinThickness"]),
            float(input_data["Insulin"]),
            float(input_data["BMI"]),
            float(input_data["DiabetesPedigreeFunction"]),
            float(input_data["Age"])
        ]).reshape(1, -1)
        
        prediction = model_diabetes.predict(feature_values)
        
        return jsonify({"prediction": int(prediction[0])})
