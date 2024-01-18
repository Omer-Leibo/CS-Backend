from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_cors import CORS

HOST = "localhost"

app = Flask(__name__)
CORS(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:postgres@{HOST}:5432/postgres"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

from app import routes



# with app.app_context():
#     db.create_all()
