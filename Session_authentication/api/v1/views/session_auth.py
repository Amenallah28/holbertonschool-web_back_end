#!/usr/bin/env python3
"""Module of Session authentication views
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """POST /auth_session/login
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    for u in user:
        if not u.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user[0].id)
    session_name = getenv("SESSION_NAME")
    out = jsonify(user[0].to_json())
    out.set_cookie(session_name, session_id)
    return out


@app_views.route('auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """ Delete /api/v1/auth_session/logout
    """
    from api.v1.app import auth

    delete_session = auth.destroy_session(request)
    if delete_session is False:
        abort(404)
    return jsonify({}), 200