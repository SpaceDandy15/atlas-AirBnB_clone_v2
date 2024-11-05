#!/usr/bin/python3
"""
This module starts a Flask web application that responds to HTTP requests.

The web application listens on all interfaces (0.0.0.0) at port 5000 and
includes the following routes:

Routes:
- /: Displays "Hello HBNB!".
- /hbnb: Displays "HBNB".
- /c/<text>: Displays "C " followed by the value of the text variable,
  replacing underscores (_) with spaces.
"""

from flask import Flask
from markupsafe import escape  # Import escape from markupsafe instead

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Return a greeting message.

    Route: /
    Response: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Return the HBNB message.

    Route: /hbnb
    Response: "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Return 'C ' followed by the value of the text variable.

    Route: /c/<text>
    Parameter:
    - text (str): The text to display after "C ".

    Response: "C <text>", where underscores in <text> are replaced by spaces.
    """
    return "C {}".format(escape(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
