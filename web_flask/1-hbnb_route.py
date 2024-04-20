#!/usr/bin/python3
"""
the script that starts a Flask web application
hte web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    the option strict_slashes=False is used
Autor: Said LAMGHARI
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def dsply_hellohbnb():
    """Dsplays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def dsply_hbnb():
    """Dsplays 'HBNB'"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
