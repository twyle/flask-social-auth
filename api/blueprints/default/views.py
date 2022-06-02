# -*- coding: utf-8 -*-
"""This module contains the routes associated with the default Blueprint."""
import json
import re

from flask import Blueprint, jsonify, render_template
from flask_login import login_required, logout_user

default = Blueprint('default', __name__, template_folder='templates', static_folder='static')


@default.route('/')
def default_route():
    """Confirm that the application is working."""
    return render_template('home.html'), 200


@default.route('/logout')
@login_required
def logout():
    """Log out a loogged in user."""
    logout_user()
    return jsonify({'hello': 'You are logged out!'}), 200


@default.route('/dashboard/<user_data>')
def dashboard(user_data):
    """Display the user data."""
    user_data = json.loads(user_data)
    return render_template('dashboard.html', user_data=user_data), 200
