#!/usr/bin/python3
""" flask app with routes returning hello hbn,
hbnb and c plus the value of text"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    space_text = text.replace('_', ' ')
    return f'C {space_text}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    space_text = text.replace('_', ' ')
    return f'Python {space_text}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
