#!/usr/bin/env python3
"""
Module with the app's endpoints (routes)
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


AUTH = Auth()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """return a json pauload with a welcome message"""
    return jsonify({"message": "Bienvenue"})

@app.route('/', methods=['GET'], strict_slashes=False)
def message():
    """
    Method that returns a JSON welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    Method that registers a new user if it doesnt exist
    or returns a warning message if it does
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400
    
@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    Method that validates login parameters
    and creates a new session for the user
    (logs in)
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password) is False:
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

