import datetime
from marshmallow import fields
from index import db, ma, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import synonym

class User(db.Model):
    """
    User model
    """

    # table name
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    _password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')

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

    def validate_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

class UserSchema(ma.Schema):
    """
    User schema
    """
    class Meta:
        fields = ('id', 'username', 'email', 'password', 'created_at', 'updated_at')
