#!/usr/bin/python3
'''
Start a basic Flask web app.
'''
from flask import Flask

# Create the application object.
app = Flask(__name__)


# Define an endpoint
@app.route('/', strict_slashes=False)  # URL rule
def index():
    ''' Root endpoint.
    '''
    return 'Hello HBNB!'


# Run app
app.run(host='0.0.0.0')
