#!/usr/bin/python3
"""
our web application must be listening on 0.0.0.0, port 5000
Routes:
/: Hello /hbnb:
/c/<text>: , followed by the value of the text
variable (replace underscore _ symbols with a space)
/python/(<text>): , followed by the value of the text
variable (replace underscore _ symbols with a space)
The default value of text is
a number/<n>: n is a  only if n is an integer
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Display the site index """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C " + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return str(n) + " is a number "


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
