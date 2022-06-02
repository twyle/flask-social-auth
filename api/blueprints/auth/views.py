# -*- coding: utf-8 -*-
"""This module contains the routes associated with the auth Blueprint."""
import os

from flask import redirect, url_for
from flask_dance.consumer import oauth_authorized
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.contrib.github import github, make_github_blueprint
from flask_login import current_user, login_user
from sqlalchemy.orm.exc import NoResultFound

from ..extensions import db
from ..helpers import get_user_data
from .models import OAuth, User

auth = make_github_blueprint(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    storage=SQLAlchemyStorage(
        OAuth,
        db.session,
        user=current_user,
        user_required=False,
    ),
)


@oauth_authorized.connect_via(auth)
def github_logged_in(blueprint, token):  # pylint: disable=W0613, R1710
    """Automatically log in a user after authentication."""
    info = github.get('/user')
    if info.ok:
        account_info = info.json()
        username = account_info['login']

        query = User.query.filter_by(username=username)
        try:
            user = query.one()
        except NoResultFound:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        login_user(user=user)
        user_data = get_user_data(info.json())
        return redirect(url_for('default.dashboard', user_data=user_data))
