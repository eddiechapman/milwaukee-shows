import logging
from logging.handlers import RotatingFileHandler
import pathlib
from flask import Flask
from config import Production


def create_app(config_class=Production):
    app = Flask(__name__)
    app.config.from_object(config_class)

    if not app.debug and app.testing:
        init_logging()

    return app


def init_logging():
    log_path = pathlib.Path('logs')

    if not log_path.exists():
        log_path.mkdir()

    file_handler = RotatingFileHandler(
        filename='logs/app.log',
        maxBytes=10240,
        backupCount=10
    )

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %Imessage)s '
        '[in %(pathname)s:%(lineno)d]'
    )

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('milwaukee-shows startup')

