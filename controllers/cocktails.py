from flask import Blueprint, request, jsonify, g
from models.Cocktail import Cocktail, CocktailSchema
from models.Comment import Comment, CommentSchema
from lib.secure_route import secure_route

cocktail_schema = CocktailSchema()
cocktails_schema = CocktailSchema(many=True)

comment_schema = CommentSchema()

api = Blueprint('cocktails', __name__)

@api.route('')
def index():
    cocktails = Cocktail.query.all()
    return cocktails_schema.jsonify(cocktails)

@api.route('/<int:id>')
def show(id):
    cocktail = Cocktail.query.get(id)
    if not cocktail:
        return jsonify({ 'message': 'Not found' }), 404
    return cocktail_schema.jsonify(cocktail)

@api.route('', methods=['POST'])
@secure_route
def create():
    req_data = request.get_json()
    data, error = cocktail_schema.load(req_data)

    if error:
        return jsonify({ "error": error }), 422

    cocktail = Cocktail(data)
    cocktail.user_id = g.get('current_user').id
    cocktail.save()

    return cocktail_schema.jsonify(cocktail)

@api.route('/<int:id>', methods=['PUT', 'PATCH'])
@secure_route
def update(id):
    req_data = request.get_json()
    data, error = cocktail_schema.load(req_data)

    if error:
        return jsonify({ 'error': error }), 422

    cocktail = Cocktail.query.get(id)
    cocktail.update(data)

    return cocktail_schema.jsonify(cocktail)

@api.route('/<int:id>', methods=['DELETE'])
@secure_route
def delete(id):
    cocktail = Cocktail.query.get(id)

    if not cocktail:
        return jsonify({ 'message': 'Not found' }), 404

    cocktail.delete()
    return '', 204

@api.route('/<int:id>/comments', methods=['POST'])
@secure_route
def create_comment(id):
    req_data = request.get_json()
    data, error = comment_schema.load(req_data)

    if error:
        return jsonify({ "error": error }), 422

    comment = Comment(data)
    comment.cocktail_id = id
    comment.user_id = g.get('user').id
    comment.save()

    return comment_schema.jsonify(comment)

@api.route('/<int:id>/comments/<int:comment_id>', methods=['DELETE'])
@secure_route
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({ 'message': 'Not found' }), 404

    comment.delete()
    return '', 204
