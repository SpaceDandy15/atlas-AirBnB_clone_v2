#!/usr/bin/python3
"""
Flask web application to display a list of states.
The application listens on 0.0.0.0, port 5000, and
retrieves State objects from the storage engine.

Routes:
/states_list: displays an HTML page with a list of states

Usage:
- Ensure the necessary database environment variables are set.
- Run the app with:
    HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd \
    HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db \
    HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays an HTML page with a list of all State objects sorted by name.
    Each state is displayed in an unordered list with its ID and name.
    
    Returns:
        Rendered HTML template (7-states_list.html) with the list of states.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the SQLAlchemy session after each request.
    
    Args:
        exception (Exception): Any exception that occurred during request handling.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
