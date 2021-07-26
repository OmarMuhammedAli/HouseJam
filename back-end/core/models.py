from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.engine.url import URL
from flask_sqlalchemy import SQLAlchemy

from dotenv import dotenv_values

config = dotenv_values(dotenv_path='.env')

# URI for the database
# All values are taken from the .env file
DB_INFO = {
    'drivername': config['DB_DRIVER'],
    'host': config['DB_HOST'],
    'port': config['DB_PORT'],
    'username': config['DB_USER'],
    'password': config['DB_PASS'],
    'database': config['DB_NAME']
}

# Create DB path
DATABASE_URI = URL(**DB_INFO)

# Instantiate the db
db = SQLAlchemy()

def setup_db(app, database_uri=DATABASE_URI):
    """
    Sets up the database by binding a flask application and a SQLAlchemy service
    :param app: Flask application
    :param database_uri: SQLAlchemy database URI
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

