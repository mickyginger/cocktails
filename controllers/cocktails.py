from flask import request, jsonify
from config import app
from models.Cocktail import Cocktail, CocktailSchema

cocktail_schema = CocktailSchema()
cocktails_schema = CocktailSchema(many=True)

def index():
    cocktails = Cocktail.query.all()
    return cocktails_schema.jsonify(cocktails)

def show(id):
    cocktail = Cocktail.query.get(id)
    if not cocktail:
        return jsonify({ "message": "Not found" }), 404
    return cocktail_schema.jsonify(cocktail)

def create():
    req_data = request.get_json()
    data, error = cocktail_schema.load(req_data)

    if error:
        return jsonify({ "error": error }), 400

    cocktail = Cocktail(data)
    cocktail.save()

    return cocktail_schema.jsonify(cocktail)

def update(id):
    req_data = request.get_json()
    data, error = cocktail_schema.load(req_data)

    if error:
        return jsonify({ "error": error }), 400

    cocktail = Cocktail.query.get(id)
    cocktail.update(data)

    return cocktail_schema.jsonify(cocktail)

def delete(id):
    cocktail = Cocktail.query.get(id)

    if not cocktail:
        return jsonify({ "message": "Not found" }), 404

    cocktail.delete()
    return '', 204
