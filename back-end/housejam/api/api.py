from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return "Hello, world!"

@api.route('/hello')
def hello():
    return "<h1>Testing</h1>"