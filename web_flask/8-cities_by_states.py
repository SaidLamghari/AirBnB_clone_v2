#!/usr/bin/python3
"""
* This is a tarts a Flask web application
* The  web application must be
listening on 0.0.0.0, port 5000
* storage for fetching data from the storage engine
* load all cities of a State
Autor : Said LAMGHARI
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def rm_teardown_db(exception):
    """ Remove the currt
    SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def dsp_cities_by_states():
    """ Dsplay a HTML
    listing all State objects
    Their cities """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
