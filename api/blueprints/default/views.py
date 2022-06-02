# -*- coding: utf-8 -*-
"""This module contains the routes associated with the default Blueprint."""
from flask import Blueprint, jsonify
from flask_login import login_required, logout_user

default = Blueprint('default', __name__, template_folder='templates', static_folder='static')


@default.route('/')
def default_route():
    """Confirm that the application is working."""
    return jsonify({'hello': 'from template api'}), 200


@default.route('/logout')
@login_required
def logout():
    """Log out a logged in user."""
    logout_user()
    return jsonify({'hello': 'You are logged out!'}), 200


@default.route('/dashboard')
def dashboard():
    """Display the user data."""
    return jsonify({'hello': 'You are at the dashboard!'}), 200
