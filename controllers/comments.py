from flask import request, jsonify, g
from index import app
from models.Comment import Comment, CommentSchema
from lib.secure_route import secure_route

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

@secure_route
def create(id):
    req_data = request.get_json()
    data, error = comment_schema.load(req_data)

    if error:
        return jsonify({ "error": error }), 422

    comment = Comment(data)
    comment.cocktail_id = id
    comment.user_id = g.get('user').id
    comment.save()

    return comment_schema.jsonify(comment)

@secure_route
def delete(id, comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({ 'message': 'Not found' }), 404

    comment.delete()
    return '', 204
