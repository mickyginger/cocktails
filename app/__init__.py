from flask import Flask
from models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://localhost:5432/cocktails"
db.init_app(app)
