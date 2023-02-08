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
            /hbnb_filters:        disp HTML w/ working state, city filter
            /hbnb:                disp HTML w/ working property, amenity filter
"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """after each request remove current SQLAlchemy session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def all_static_filters():
    """display html page w/ working city/state filters & amenities/properties
       runs with web static css files
    """
    state_objs = [s for s in storage.all(cls=State).values()]
    amenity_objs = [a for a in storage.all(cls=Amenity).values()]
    place_objs = [p for p in storage.all(cls=Place).values()]
    user_objs = [u for u in storage.all(cls=User).values()]
    place_owner_objs = []
    for place in place_objs:
        for user in user_objs:
            if place.user_id == user.id:
                place_owner_objs.append(["{} {}".format(
                    user.first_name, user.last_name), place])
    place_owner_objs.sort(key=lambda p: p[1].name)
    return render_template('100-hbnb.html',
                           state_objs=state_objs,
                           amenity_objs=amenity_objs,
                           place_owner_objs=place_owner_objs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
