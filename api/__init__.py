from flask import Flask
from .breastCancer import breast_bp
from .Diabetes import diabetes_bp
from .Heart import heart_bp
from .Kidney import kidney_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(breast_bp, url_prefix="/breast")
app.register_blueprint(diabetes_bp,url_prefix="/diabetes")
app.register_blueprint(heart_bp,url_prefix="/heart")
app.register_blueprint(kidney_bp,url_prefix="/kidney")
