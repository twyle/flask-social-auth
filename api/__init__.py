# -*- coding: utf-8 -*-
"""This module contains initialization code for the api package."""
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import github

from api.helpers import set_flask_environment

from .blueprints.auth.models import User
from .blueprints.auth.views import auth
from .blueprints.default.views import default
from .blueprints.extensions import db
from .blueprints.helpers import get_user_data
from .extensions import login_manager

app = Flask(__name__)
set_flask_environment(app=app)
app.register_blueprint(default)
app.register_blueprint(auth, url_prefix='/login')

db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id: int) -> User:
    """Load the user with the given id."""
    return User.query.get(user_id)


@app.route('/github')
def login():  # pylint: disable=R1710
    """Log in a registered or authenticated user."""
    if not github.authorized:
        return redirect(url_for('github.login'))
    info = github.get('/user')
    if info.ok:
        user_data = get_user_data(info.json())
        return redirect(url_for('default.dashboard', user_data=user_data))
