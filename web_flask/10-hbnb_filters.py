#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:                    display "Hello HBNB!"
            /hbnb:                display "HBNB"
            /c/<text>:            display "C" + text (replace "_" with " ")
            /python/<text>:       display "Python" + text (default="is cool")
            /number/<n>:          display "n is a number" only if int
            /number_template/<n>: display HTML page only if n is int
            /number_odd_or_even/<n>: display HTML page; display odd/even info
            /states_list & /states:  display HTML and state info from storage
            /cities_by_states:    display HTML and state, city relations
            /states/<id>:         display HTML and state, city given state id
            /hbnb_filters:        display a HTML page like 6-index.html
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """after each request remove current SQLAlchemy session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def static_filters():
    """display html page with working city/state filters & amenities
       runs with web static css files
    """
    state_objs = [s for s in storage.all(cls=State).values()]
    amenity_objs = [a for a in storage.all(cls=Amenity).values()]
    return render_template('10-hbnb_filters.html',
                           state_objs=state_objs, amenity_objs=amenity_objs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
