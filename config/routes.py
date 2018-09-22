from flask import abort, jsonify
from . import app
from controllers import cocktails

app.add_url_rule("/cocktails", "cocktails_index", cocktails.index, methods=["GET"])
app.add_url_rule("/cocktails", "cocktails_create", cocktails.create, methods=["POST"])
app.add_url_rule("/cocktails/<int:id>", "cocktails_show", cocktails.show, methods=["GET"])
app.add_url_rule("/cocktails/<int:id>", "cocktails_update", cocktails.update, methods=["PUT", "PATCH"])
app.add_url_rule("/cocktails/<int:id>", "cocktails_delete", cocktails.delete, methods=["DELETE"])

@app.route("/<path:path>")
def catch_all(path):
    return jsonify({ "message": "Not found" }), 404
