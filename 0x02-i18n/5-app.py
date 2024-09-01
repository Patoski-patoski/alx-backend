#!/usr/bin/env python3
"""Basic Flask_Babel setup with internationalization support
   Parametrize templates
   Force locale with URL parameter
"""

from flask import Flask, g, render_template, request
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """Config settings"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """get user_name"""
    login_as = request.args.get('login_as', None)
    if login_as:
        login_as = int(login_as)
        return users.get(login_as)

    return None


@app.before_request
def before_request():
    """get global user"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match with our supported languages.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.jinja_env.globals['get_locale'] = get_locale


@app.route("/")
def index():
    """render_template: 5-index.html"""
    return render_template("5-index.html", get_locale=get_locale)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
