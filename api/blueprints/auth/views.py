# -*- coding: utf-8 -*-
"""This module contains the routes associated with the auth Blueprint."""
import os

from flask_dance.contrib.github import make_github_blueprint

auth = make_github_blueprint(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
)
