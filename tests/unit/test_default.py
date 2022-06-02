# -*- coding: utf-8 -*-
"""This module tests the default route."""


def test_default(client):
    """Tests that the default route returns ok message on GET request.

    GIVEN we have the / route
    WHEN we send a GET request
    THEN we should get a 200 OK response
    """
    resp = client.get('/')
    assert resp.status_code == 200


def test_home_bad_http_method(client):
    """Tests that the default route returns method not allowed message on POST request.

    GIVEN we have the / route
    WHEN we send a POST request
    THEN we should get a 405 error code in the response
    """
    resp = client.post('/')
    assert resp.status_code == 405
