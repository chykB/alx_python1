#!/usr/bin/python3
"""
This module contains the code for a simple Flask web application.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """
    The application has a single route, `/`,
    which calls the `index()` function
    """
    return "<p>Hello HBNB!<p>"

if __name__ == "__main__":
    app.run(0.0.0.0:5000)
