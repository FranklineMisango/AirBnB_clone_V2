#!/usr/bin/python3
"""
A script that starts a Flask Web Application
"""


from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
