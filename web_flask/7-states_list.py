#!/usr/bin/python3
'''
Start a basic Flask web app.
'''
from flask import Flask, render_template
from models import storage
from models.state import State

# Create the application object.
app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    ''' Close session associated with the app.
    '''
    storage.close()


# Get all State objects
raw_states = storage.all(cls=State)
states = {}
# Replace State objects with name in states dict
states_copy = raw_states.copy()
for key, value in states_copy.items():
    states[value.id] = value.name


@app.route('/states_list', strict_slashes=False)
def hbnb():
    ''' Returns a page that lists state ids with their names.
    '''
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    # Run app
    app.run(host='0.0.0.0')
