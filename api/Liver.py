from flask import Blueprint, request, jsonify
import numpy as np
import pickle

# Create a Blueprint
liver_bp = Blueprint("liver", __name__)

# Load the pre-trained GradientBoostingClassifier model
model_liver = pickle.load(open('./pickle/Pickle_Liver.pkl', 'rb'))

# Define a dictionary to map genders to numerical values
gender_mapping = {"Male": 0, "Female": 1}

@liver_bp.route("/predict_liver", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.json['Age'])
        Gender = request.json['Gender']  # Gender as string
        Total_Bilirubin = float(request.json['Total_Bilirubin'])
        Alkaline_Phosphotase = int(request.json['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = int(request.json['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = int(request.json['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.json['Total_Protiens'])
        Albumin = float(request.json['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.json['Albumin_and_Globulin_Ratio'])
        
        # Map the gender to a numerical value using the gender_mapping dictionary
        Gender_numerical = gender_mapping.get(Gender, -1)  # Default to -1 if gender is not recognized
        
        if Gender_numerical == -1:
            return jsonify({"error": "Invalid gender value"})
        
        values = np.array([[Age, Gender_numerical, Total_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
        prediction = model_liver.predict(values)

        return jsonify({"prediction": int(prediction[0])})