from flask import Blueprint, request, jsonify
import numpy as np
import pickle

# Create a Blueprint
heart_bp = Blueprint("heart", __name__)

# Load the pre-trained GradientBoostingClassifier model
model_heart = pickle.load(open('./pickle/Pickle_Heart.pkl', 'rb'))

@heart_bp.route("/predict_heart", methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = request.json

        age = int(input_data['age'])
        sex = int(input_data['sex'])
        cp = int(input_data['cp'])
        trestbps = int(input_data['trestbps'])
        chol = int(input_data['chol'])
        fbs = int(input_data['fbs'])
        restecg = int(input_data['restecg'])
        thalach = int(input_data['thalach'])
        exang = int(input_data['exang'])
        oldpeak = float(input_data['oldpeak'])
        slope = int(input_data['slope'])
        ca = int(input_data['ca'])
        thal = int(input_data['thal'])

        values = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        prediction = model_heart.predict(values)

        return jsonify({"prediction": int(prediction[0])})
