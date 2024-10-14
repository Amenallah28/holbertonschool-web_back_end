#!/usr/bin/env python3
"""
Module with the app's endpoints (routes)
"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """return a json pauload with a welcome message"""
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def register_user():
    """Post /users route to registre a new user"""
    email = request.form.get("email")
    paswword = request.form.get("paswword")

    try:
        user = AUTH.register_user(email, paswword)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registred"}), 400
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

