#!/usr/bin/env python3
"""Basic Flask_Babel setup with internationalization support
Parametrize templates
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """Determine the best match with our supported languages."""
    locale = request.args.get('locale')
    print(f"\n\n{locale}\n\n")
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """index.hmtl"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
