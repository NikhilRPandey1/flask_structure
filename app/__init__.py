from flask import Flask
from .config import Config
from .extensions import db, migrate
from .auth.routes import auth_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
