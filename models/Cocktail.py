import datetime
from marshmallow import fields
from sqlalchemy.dialects.postgresql import JSON
from index import db, ma

class Cocktail(db.Model):
    """
    Cocktail model
    """

    # table name
    __tablename__ = "cocktails"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    image = db.Column(db.String(128), nullable=False, unique=True)
    ingredients = db.Column(JSON, nullable=False)
    method = db.Column(db.String(500), nullable=False)
    about = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, data):
        for key, item in data.items():
            setattr(self, key, item)

        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

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

class CocktailSchema(ma.Schema):
    """
    Cocktail schema
    """
    class Meta:
        fields = ('id', 'name', 'image', 'ingredients', 'method', 'about', 'created_at', 'updated_at')
