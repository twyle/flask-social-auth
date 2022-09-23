# -*- coding: utf-8 -*-
"""This package contains all the application code."""
from flask import Flask, jsonify


def create_app():
    """Create the flask app object."""
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def health_check():
        """Check if the application is running."""
        return jsonify({"Hello": "from flask-social-auth"}), 200

    return app
