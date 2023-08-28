#!/usr/bin/python3
"""this script start the Flask web application"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    """the route to home page"""
    return "<p>Hello HBNB!<p>"

if __name__ == "__main__":
    app.run(0.0.0.0:5000)
