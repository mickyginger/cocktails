from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config.environment import db_uri

app = Flask(__name__, static_folder='public')

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

from config import routes
