#!/usr/bin/python3
"""
This module starts a Flask web application that responds to HTTP requests.

The web application listens on all interfaces (0.0.0.0) at port 5000 and includes the following routes:

Routes:
- /: Displays "Hello HBNB!".
- /hbnb: Displays "HBNB".
- /c/<text>: Displays "C " followed by the value of the text variable,
  replacing underscores (_) with spaces.
- /python/<text>: Displays "Python " followed by the value of the text variable,
  replacing underscores (_) with spaces. If no <text> is provided, defaults to "is cool".
- /number/<n>: Displays "<n> is a number" only if <n> is an integer.
"""

from flask import Flask
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
