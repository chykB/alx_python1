#!/usr/bin/python3
"""
This module contains the code for a simple Flask web application.
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    """
    The application has a single route, `/`,
    which calls the `index()` function
    """
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    return "HBNB"

@app.route("/c/<text>")
def text_display(text):
    """
    Display "C " followed by the value of the text variable.
    Replace underscores with spaces
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

