import logging

from flask import Flask

from src.config.configuration import Config

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['DEBUG'] = True


def create_app(config_class=Config):
    logger.debug("Starting Flask Server")

    from src.app import routes

    app.config.from_object(config_class)
    return app
