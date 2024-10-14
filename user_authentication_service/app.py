#!/usr/bin/env python3
"""
Module with the app's endpoints (routes)
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """return a json pauload with a welcome message"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
