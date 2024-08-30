#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)


@app.route('/')
def index():
    """index file"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
