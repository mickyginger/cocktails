from flask import jsonify
from app import app
from controllers import cocktails, auth, darksky
import os

app.register_blueprint(cocktails.api, url_prefix='/api')
app.register_blueprint(auth.api, url_prefix='/api')
app.register_blueprint(darksky.api, url_prefix='/api')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

    if os.path.isfile('public/' + path):
        return app.send_static_file(path)

    print('here..')
    return app.send_static_file('index.html')
