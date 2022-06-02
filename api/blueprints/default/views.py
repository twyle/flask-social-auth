# -*- coding: utf-8 -*-
"""This module contains the routes associated with the default Blueprint."""
from flask import Blueprint, jsonify

default = Blueprint('default', __name__, template_folder='templates', static_folder='static')


@default.route('/')
def default_route():
    """Confirm that the application is working."""
    return jsonify({'hello': 'from template api'}), 200
