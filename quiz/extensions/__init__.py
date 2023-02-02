from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restx import Api


# instantiate the extensions imported above
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
app = Flask(__name__)
api = Api()

