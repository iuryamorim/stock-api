"""
Provide implementation of application's server configurations.
"""
from flask import Flask
from flask_cors import CORS
from src.endpoints import blueprint

def create_app() -> Flask:
    """
    Create the configured Flask app.

    Returns created app instance (flask.Flask).
    """
    app = Flask(import_name=__name__)

    CORS(app, resources={r"*": {"origins": "*"}})

    app.register_blueprint(blueprint=blueprint)

    return app


app = create_app()
