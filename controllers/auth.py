import jwt
import os
import datetime
from flask import request, jsonify, json
from index import app
from models.User import User, UserSchema
from config.environment import secret

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def register():
    req_data = request.get_json()
    data, error = user_schema.load(req_data)

    if error:
        return jsonify({ 'error': error }), 422

    user = User(data)
    user.save()

    return user_schema.jsonify(user)

def login():
    req_data = request.get_json()
    data, error = user_schema.load(req_data, partial=True)

    if error:
        return jsonify({ 'error': error }), 422

    user = User.query.filter_by(email=data.get('email')).first()

    if not user.validate_password(data.get('password')):
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

    return jsonify({ 'message': 'Welcome back {}!'.format(user.username), 'token': token })
