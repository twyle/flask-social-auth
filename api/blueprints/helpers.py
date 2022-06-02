# -*- coding: utf-8 -*-
"""This module has methods that are used in the other modules in this package."""
import json


def get_user_data(github_data: dict) -> dict:
    """Obtain the user data from github response.

    Given the response issued out by GitHub, this method should give back the
    user data

    Parameters
    ----------
    github_data: dict
        A json object with all the data from GitHub.

    Throws
    ------
    ValueError:
        if github_data is empty or not a dictionary

    Returns
    -------
    user_data: dict
        A dictionary with the users data:
        {
            "bio": "Founder @oryksrobotics. I design and build robots for the logistics and supply chain industry.",
            "location": "Nairobi, Kenya",
            "login": "lyleokoth",
            "twitter_username": "lylethedesigner",
        }
    """
    if not github_data:
        raise ValueError('The github_data has to be supplied!')
    if not isinstance(github_data, dict):
        raise ValueError('The github_data has to be a dictionary!')

    user_data = dict(
        bio=github_data['bio'],
        location=github_data['location'],
        login=github_data['login'],
        twitter_username=github_data['twitter_username']
    )

    return json.dumps(user_data)
