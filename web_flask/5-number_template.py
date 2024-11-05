#!/usr/bin/python3
"""
This module starts a Flask web application that responds to HTTP requests.
"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a greeting message."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return the HBNB message."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Return 'C ' followed by the value of the text variable."""
    return "C {}".format(escape(text.replace('_', ' ')))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Return 'Python ' followed by the value of the text variable."""
    return "Python {}".format(escape(text.replace('_', ' ')))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Return '<n> is a number' only if <n> is an integer."""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render an HTML page displaying 'Number: <n>' only if <n> is an integer."""
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)