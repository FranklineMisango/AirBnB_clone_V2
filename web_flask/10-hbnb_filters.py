#!/usr/bin/python3
"""
A script that starts a Flask Web Application

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
