from flask import Flask
from flask_caching import Cache
from os import environ
from pathlib import Path

from .library import load_library_file

cache = Cache(config={ 'CACHE_TYPE': 'simple',
                       'CACHE_THRESHOLD': 200 }) # 200*5 MB = 1 GB

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config')
    app.config['DEV'] = 'FLASK_ENV' in environ and environ['FLASK_ENV'] == 'development'

    from . import clipper
    app.register_blueprint(clipper.bp)

    from . import explorer
    app.register_blueprint(explorer.bp)

    init_app(app)

    return app

def init_app(app):
    app.library_data = load_library_file(Path(app.config['LIBRARY']))
    cache.init_app(app)

def http_error(code, message):
    return flask.Response(message, status=code, mimetype='text/plain')

