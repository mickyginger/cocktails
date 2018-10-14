import datetime
from marshmallow import fields
from index import db, ma

class Comment(db.Model):
    """
    Comment model
    """

    # table name
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(20), nullable=False, unique=True)
    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktails.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User')
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

class CommentSchema(ma.Schema):
    """
    Comment schema
    """
    user = fields.Nested('UserSchema', only=('id', 'username'))
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'created_at', 'updated_at')
