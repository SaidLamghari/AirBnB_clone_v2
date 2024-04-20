#!/usr/bin/python3
"""
The script that starts a Flask web application
The web application will be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, that followed by the value of the text
    /python/(<text>): display “Python ”,
    that followed by the value of the text variable
    The default text is “is cool”
    /number/<n>: display “n is a number”
    /number_template/<n>: display a HTML page :
    H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page:
    H1 tag: “Number: n is even|odd” inside the tag BODY
Autor :  Said LAMGHARI
"""
from flask import Flask, render_template

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
    it will followed by
    the value of the text"""
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
    """Dsplays 'n is a number'
    only if it is integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def dsply_number_template(n):
    """Dsplays an HTML page
    only n is integer"""
    return render_template('6-number_template.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def dsply_number_odd_or_even(n):
    """Dsplays an HTML page
    only if n is an integer
    and if it's odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
