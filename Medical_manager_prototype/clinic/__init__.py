from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key_for_dev')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:123@localhost/ProjectDB')

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Initialize LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Print statements to verify roles and session states
roles = ["none", "doctor", "patient"]
print(roles)
mysession = {"state": "initializing", "role": "Not assigned", "id": 0, "age": 202212}
print(mysession)

# Import and register blueprints
from clinic.Login.routes import Login
from clinic.Patient.routes import Patient
from clinic.Doctor.routes import Doctor
app.register_blueprint(Login)
app.register_blueprint(Patient)
app.register_blueprint(Doctor)

# Ensure user loader callback is defined
from clinic.models import load_user
