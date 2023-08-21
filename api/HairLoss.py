import numpy as np
from flask import Flask, Blueprint, request, jsonify
import pickle

# Create a Blueprint
hair_bp = Blueprint("hairloss", __name__)


# Load the model using pickle
model_hairLoss = pickle.load(open('./pickle/hairLoss.pkl', 'rb'))

@hair_bp.route("/predict_hair", methods=['POST'])
def predict_hair():
    if request.method == 'POST':
        data = request.json
        print(data)
        Chemotherapy_Regimen = int(data['Chemotherapy_Regimen'])
        Drug_Dosage = int(data['Drug_Dosage(mg)'])
        Age = int(data['Age'])
        Hypertension = int(data['Hypertension'])
        Family_History = int(data['Family_History'])
    
        values = np.array([[Chemotherapy_Regimen, Drug_Dosage, Age, Hypertension, Family_History]])
        predicted_severity = model_hairLoss.predict(values)
    
        return jsonify({'predicted_severity': int(predicted_severity[0])})