#!/usr/bin/python3
"""Starts a Flask app server that  must listen 0.0.0.0 port 5000.
    routes (/ and /hbnh and /c/<text>)"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbpage():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def varpage(text):
    str_show = str(text).replace("_", " ")
    return "C " + str_show

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
