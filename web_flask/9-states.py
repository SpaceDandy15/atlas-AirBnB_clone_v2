#!/usr/bin/python3
"""Flask web application to display states and cities"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """Displays a list of all State objects"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Displays cities of a specific State by id"""
    state = storage.all(State).get("State." + id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html', state=None)

@app.teardown_appcontext
def teardown(exception):
    """Closes the storage session after each request"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
