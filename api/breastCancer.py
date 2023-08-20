from flask import Blueprint, request, jsonify
import numpy as np
import pickle

# Create a Blueprint
breast_bp = Blueprint("breast", __name__)

# Load the pre-trained RandomForest model
model_breast = pickle.load(open('./pickle/BreastCancerModel.pkl', 'rb'))

@breast_bp.route("/predict_breast", methods=["POST"])
def predict_breast():
    if request.method == "POST":
        # Get input features from JSON data
        input_data = request.json
        input_features = np.array([
            float(input_data["texture_mean"]),
            float(input_data["smoothness_mean"]),
            float(input_data["compactness_mean"]),
            float(input_data["symmetry_mean"]),
            float(input_data["fractal_dimension_mean"]),
            float(input_data["texture_se"]),
            float(input_data["smoothness_se"]),
            float(input_data["symmetry_se"]),
            float(input_data["symmetry_worst"])
        ]).reshape(1, -1)  # Reshape for prediction

        # Predict using the loaded model
        prediction = model_breast.predict(input_features)

        # Convert prediction to integer
        prediction = int(prediction[0])

        return jsonify({"prediction": prediction})
