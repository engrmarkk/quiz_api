from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# instantiate the extensions imported above
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
app = Flask(__name__)
