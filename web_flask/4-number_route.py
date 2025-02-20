#!/usr/bin/python3
'''
Start a basic Flask web app.
'''
from flask import Flask

# Create the application object.
app = Flask(__name__)


# Define endpoints

@app.route('/', strict_slashes=False)  # URL rule
def index():
    ''' Root endpoint.
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' /hbnb endpoint.
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    ''' Displays `C` followed by the value of the
    text variable (replace underscore _ symbols with a space )
    '''
    # Replace any underscores with space char
    text = text.replace('_', ' ')

    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text='is cool'):
    ''' Displays `python` followed by the value of the
    text variable (replace underscore _ symbols with a space )
    '''
    # Replace any underscores with space char
    text = text.replace('_', ' ')

    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    ''' display `n is a number` only if n is an integer.
    '''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    # Run app
    app.run(host='0.0.0.0')
