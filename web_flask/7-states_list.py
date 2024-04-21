#!/usr/bin/python3
"""
The script to start a Flask web application
The web application be listening on 0.0.0.0, port 5000
Storage use for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
After each request it remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    Routes:
    /states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objectspresent in DBStorage sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
    Import this 7-dump to have some data
Autor : SAID LAMGHARI    
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)



@app.route('/states_list', strict_slashes=False)
def dsply_stateslist():
    """
    Dsplay State objects
    """
    v_stts = storage.all(State).values()
    srtd_stts = sorted(v_stts, key=lambda x: x.name)
    return render_template('7-states_list.html', v_stts=srtd_stts)

@app.teardown_appcontext
def rmv_teardowndb(exception):
    """
    Rmove SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
