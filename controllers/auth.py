import jwt
import datetime
from flask import Blueprint, request, jsonify, g
from models.User import User, UserSchema
from config.environment import secret
from lib.secure_route import secure_route
from lib.error_handler import error_handler

user_schema = UserSchema()
users_schema = UserSchema(many=True)

api = Blueprint('auth', __name__)

@api.route('/register', methods=['POST'])
def register():
    req_data = request.get_json()
    data, errors = user_schema.load(req_data)

    if errors:
        return jsonify({ 'errors': error_handler(errors) }), 422

    user = User(data)
    user.save()

    return user_schema.jsonify(user)

@api.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()
    data, error = user_schema.load(req_data)

    user = User.query.filter_by(email=data.get('email')).first()

    if not user or not user.validate_password(data.get('password', '')):
        return jsonify({ 'message': 'Unauthorized' }), 401

    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': user.id
    }

    token = jwt.encode(
        payload,
        secret,
        'HS256'
    ).decode('utf-8')

    return user_schema.jsonify(user)

@api.route('/profile', methods=['GET'])
@secure_route
def profile():
    return user_schema.jsonify(g.current_user)
