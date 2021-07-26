from flask import Flask

# Local imports
from .api.api import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app

