#!/usr/bin/python3
"""
This module starts a Flask web application that responds to specific
HTTP requests.

It has the following routes:
- /: displays "Hello HBNB!"
- /hbnb: displays "HBNB".
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a greeting message for the root route."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a message for the /hbnb route."""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
