import logging

from src.app import app
from flask import request, jsonify

from src.service.ProcessService import ProcessService

logger = logging.getLogger(__name__)

process_service = ProcessService()


@app.route('/')
@app.route('/index')
def index():
    return "Flask Demo: Hello, comrade!"


@app.route('/hi', methods=['POST'])
def hi():
    response = process_service.hi(request)

    logger.debug('Response: ' + str(response))
    return jsonify(response)
