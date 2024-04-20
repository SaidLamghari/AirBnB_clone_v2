#!/usr/bin/python3
"""
The script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” That followed by the value
    of the text variable
    /python/(<text>): display “Python ”
    That followed by the value of the text
    The default text is “is cool”
    /number/<n>: display “n as number” if is an integer
    /number_template/<n>: display a HTML if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
Autor : Said LAMGHARI
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
    """Displays 'C '
    That followed by the value of the text"""
    string1 = text.replace('_', ' ')
    return 'C {}'.format(string1)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def dsply_python(text):
    """Dsplays 'Python '
    that followed by the value of the text"""
    string2 = text.replace('_', ' ')
    return 'Python {}'.format(string2)


@app.route('/number/<int:n>', strict_slashes=False)
def dsply_number(n):
    """Dsplays 'n as number'
    it will display only if it is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def dsply_number_template(n):
    """Displays an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
