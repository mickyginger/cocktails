from flask import jsonify
from app import app
from controllers import cocktails, auth, darksky

app.register_blueprint(cocktails.api, url_prefix='/api/cocktails')
app.register_blueprint(auth.api, url_prefix='/api')
app.register_blueprint(darksky.api, url_prefix='/api')

@app.route('/<path:path>')
def catch_all(path):
    return jsonify({ 'message': 'Not found' }), 404
