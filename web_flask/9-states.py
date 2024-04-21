#!/usr/bin/python3
"""
* This script to start a Flask web application
* The web application must be
listening on 0.0.0.0, port 5000
* This use storage for fetching
data from the storage engine
Autor : Said LAMGHARI
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def cl_teardowndb(exception):
    """Closes database again at
    the end of request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def dsply_stateslist():
    """Dsplay a HTML with
    the list of State objects"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def dsply_statescities(id):
    """Dsplay a HTML with the list
    of City objects linked to State"""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', not_found=True)
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
