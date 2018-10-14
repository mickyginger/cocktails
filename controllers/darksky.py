import os
import requests
from flask import Blueprint, request, jsonify

api = Blueprint('darksky', __name__)

@api.route('/forecast', methods=['GET'])
def forecast():
    key = os.getenv('DARKSKY_SECRET_KEY')
    query = request.args
    lat = query.get('lat', None)
    lng = query.get('lng', None)

    if not lat or not lng:
        return jsonify({ 'message': 'lat/lng required in query string' }), 422

    endpoint = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)
    response = requests.get(endpoint)

    return jsonify(response.json().get('currently', None))
