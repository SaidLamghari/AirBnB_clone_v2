#!/usr/bin/python3
"""
Script that starts a Flask web application
he web application that must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”,
    it will followed by the value of the text
    /python/(<text>): display “Python ”
    it will followed by the value of the text variable
    The default text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
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


@app.route('/c/<text>', strict_slashes=False)
def dsply_c(text):
    """Dsplays 'C '
    it will followed by the value
    of the text variable"""
    string1 = text.replace('_', ' ')
    return 'C {}'.format(string1)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def dsply_python(text):
    """Dsplays 'Python '
    it will followed by the value
    of the text"""
    string2 = text.replace('_', ' ')
    return 'Python {}'.format(string2)


@app.route('/number/<int:n>', strict_slashes=False)
def dsply_number(n):
    """Dsplays 'n as number'
    it wll be display only is an integer"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
