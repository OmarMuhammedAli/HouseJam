from flask import Flask

# Local imports
from .api import api


def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(api)
    return app

