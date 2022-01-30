#!/usr/bin/python3
"""
A script that starts a Flask Web Application
/: Diplays "Hello HBNB!"
/hbnb: Displays "HBNB"
/c/<text>: display “C ” followed by \
    the value of the text variable
/python/(<text>): display “Python ”,
    followed by the value of the text variable
    (replace underscore _ symbols with a space)
"""


from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
def python_magic():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'python' followed by the value of <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
