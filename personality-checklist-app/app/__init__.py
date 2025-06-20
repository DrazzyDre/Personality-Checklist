from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load secret key from environment variable or fallback
    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'fallback-key')

    # Database configuration (example using SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 'sqlite:///personality.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import and register the Blueprint
    from app.routes import app as app_blueprint
    app.register_blueprint(app_blueprint)

    return app