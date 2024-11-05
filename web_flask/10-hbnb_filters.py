#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)

@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display the HBNB filters page."""
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)

    # Sort states, cities, and amenities by name
    states = sorted(states.values(), key=lambda x: x.name)
    cities = sorted(cities.values(), key=lambda x: x.name)
    amenities = sorted(amenities.values(), key=lambda x: x.name)

    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
