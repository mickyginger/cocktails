from flask import request, jsonify, g
from index import app
from models.Cocktail import Cocktail, CocktailSchema
from lib.secure_route import secure_route

cocktail_schema = CocktailSchema()
cocktails_schema = CocktailSchema(many=True)

@secure_route
def index():
    cocktails = Cocktail.query.all()
    return cocktails_schema.jsonify(cocktails)

@secure_route
def show(id):
    cocktail = Cocktail.query.get(id)
    if not cocktail:
        return jsonify({ 'message': 'Not found' }), 404
    return cocktail_schema.jsonify(cocktail)

@secure_route
def create():
    req_data = request.get_json()
    data, error = cocktail_schema.load(req_data)

    if error:
        return jsonify({ "error": error }), 422

    cocktail = Cocktail(data)
    cocktail.save()

    return cocktail_schema.jsonify(cocktail)

@secure_route
def update(id):
    req_data = request.get_json()
    data, error = cocktail_schema.load(req_data)

    if error:
        return jsonify({ 'error': error }), 422

    cocktail = Cocktail.query.get(id)
    cocktail.update(data)

    return cocktail_schema.jsonify(cocktail)

@secure_route
def delete(id):
    cocktail = Cocktail.query.get(id)

    if not cocktail:
        return jsonify({ 'message': 'Not found' }), 404

    cocktail.delete()
    return '', 204
