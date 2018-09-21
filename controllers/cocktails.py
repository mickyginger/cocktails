from flask import request, jsonify
from app import app
from models.Cocktail import CocktailModel, CocktailSchema

cocktail_schema = CocktailSchema()

def index():
    return jsonify({ "message": "Cocktails INDEX" })

def show(id):
    return jsonify({ "message": "Cocktails SHOW" })

def create():
    req_data = request.get_json()
    data, error = cocktail_schema.load(req_data)

    if error:
        return jsonify({ "error": error }), 400

    cocktail = CocktailModel(data)
    cocktail.save()

    return jsonify(cocktail)

def update(id):
    return jsonify({ "message": "Cocktails UPDATE" })

def delete(id):
    return jsonify({ "message": "Cocktails DELETE" })
