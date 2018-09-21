import datetime
from marshmallow import fields, Schema
from . import db

class CocktailModel(db.Model):
    """
    Cocktail model
    """

    # table name
    __tablename__ = "cocktails"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    image = db.Column(db.String(128), nullable=False, unique=True)
    # ingredients = db.Column(db.PickleType(), nullable=False)
    method = db.Column(db.String(500), nullable=False)
    about = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, data):
        for key, item in data.items():
            setattr(self, key, item)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.updated_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class CocktailSchema(Schema):
    """
    Cocktail schema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    image = fields.Str(required=True)
    # ingredients = fields.Dict(required=True)
    method = fields.Str(required=True)
    about = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
