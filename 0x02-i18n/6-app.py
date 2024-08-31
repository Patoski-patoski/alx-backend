#!/usr/bin/env python3
"""Basic Flask_Babel setup with internationalization support
   Parametrize templates
   Force locale with URL parameter
   Use user locale
"""

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Return a user dictionary or None
    """
    user_id = request.args.get("login_as")
    if user_id is not None:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """Set a user as a global on flask.g.user
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """ return the best match """
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang
    if g.user:
        lang = g.user.get("locale")
        if lang and lang in app.config["LANGUAGES"]:
            return lang
    lang = request.headers.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """render_template: 6-index.html
    """
    return render_template("6-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
