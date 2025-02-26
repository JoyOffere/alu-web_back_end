#!/usr/bin/env python3
"""
A Minimal Flask application for testing
"""
from flask import Flask, request, g

app = Flask(__name__)

@app.before_request
def before_request() -> None:
    """
    Set the language for the application
    """
    g.lang = request.accept_languages.best_match(['en', 'fr'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Returns a simple message
    """
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
