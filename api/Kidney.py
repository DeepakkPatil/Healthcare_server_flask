from flask import Blueprint, request, jsonify
import numpy as np
import pickle

# Create a Blueprint
kidney_bp = Blueprint("kidney", __name__)

# Load the pre-trained GradientBoostingClassifier model
model_kidney = pickle.load(open('./pickle/Pickle_kidney.pkl', 'rb'))

@kidney_bp.route("/predict_kidney", methods=['POST'])
def predict():
    if request.method == 'POST':
        sg = float(request.json['sg'])
        htn = float(request.json['htn'])
        hemo = float(request.json['hemo'])
        dm = float(request.json['dm'])
        al = float(request.json['al'])
        appet = float(request.json['appet'])
        rc = float(request.json['rc'])
        pc = float(request.json['pc'])

        values = np.array([[sg, htn, hemo, dm, al, appet, rc, pc]])
        prediction = model_kidney.predict(values)

        return jsonify({"prediction": int(prediction[0])})