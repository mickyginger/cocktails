import jwt
import os
import datetime
from functools import wraps
from flask import request, jsonify, g
from models.User import User

def secure_route(func):
    """
    Secure route decorator
    """
    @wraps(func)
    def decorated_secure_route(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return jsonify({ 'message': 'Unauthorized' }), 401

        token = request.headers.get('Authorization').replace('Bearer ', '')
        data = jwt.decode(token, os.getenv('SECRET', 'shh'))
        user = User.query.get(data.get('sub'))

        if not user:
            return jsonify({ 'message': 'Unauthorized' }), 401

        g.current_user = user

        return func(*args, **kwargs)

    return decorated_secure_route
