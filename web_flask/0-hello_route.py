#!/usr/bin/python3
"""
A script that starts a Flask web application:

The web application must be listening on 0.0.0.0, port 5000
Routes: /: display “Hello HBNB!”
it must use the option strict_slashes=False in your route definition
Autor: Said LAMGHARI
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Route for the root URL.

    Returns: The message "Hello HBNB!".
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
