#!/usr/bin/python3
"""
the script that starts
a Flask web application
The web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of
    the text variable
    (replace underscore _ symbols with a space )
    The option strict_slashes=False is used in route definition
Autor: Said LAMGHARI
    """
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def dsply_hellohbnb():
    """Dsplays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def dsply_hbnb():
    """Dsplays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def dsply_c(text):
    """Dsplays 'C '
    followd by the value
    of the text variable"""
    string = escape(text).replace('_', ' ')
    return 'C {}'.format(string)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
