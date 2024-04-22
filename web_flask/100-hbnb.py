#!/usr/bin/python3
"""
* This script that starts
a Flask web application
* The web application must be listening on 0.0.0.0, port 5000
* use storage for fetching data from the storage engine
Autor : Said LAMGHARI
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def cl_teardowndb(exception):
    """Closes dbase
    again at the end of request."""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def dsply_hbnb():
    """Dsplay a HTML
    like 8-index.html"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)
    return render_template('100-hbnb.html', states=states, cities=cities,
                           amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
