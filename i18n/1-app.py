#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask, request, g
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


@app.before_request
def before_request() -> None:
    """
    Set the language for the application
    """
    g.lang = request.accept_languages.best_match(Config.LANGUAGES)

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
