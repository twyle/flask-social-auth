# -*- coding: utf-8 -*-
"""This module contains initialization code for the api package."""
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import github

from api.helpers import set_flask_environment

from .blueprints.auth.views import auth
from .blueprints.default.views import default

app = Flask(__name__)
set_flask_environment(app=app)
app.register_blueprint(default)
app.register_blueprint(auth, url_prefix='/login')


@app.route('/github')
def login():
    """Log in a registered or authenticated user."""
    if not github.authorized:
        return redirect(url_for('github.login'))
    res = github.get('/user')
    return f"You are logged in as {res.json()['login']} on GitHub."
