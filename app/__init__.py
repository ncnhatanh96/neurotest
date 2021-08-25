from flask import Flask
from .api.distance import distance_blueprint

def create_app():

    app = Flask(__name__)
    app.register_blueprint(distance_blueprint)

    return app

