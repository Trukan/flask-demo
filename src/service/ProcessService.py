import logging

from flask_restful import abort
from src.util.ResponseUtils import custom_response

logger = logging.getLogger(__name__)


class ProcessService(object):

    def __init__(self):
        pass

    def hi(self, request):
        body = request.data
        if body is None:
            abort(custom_response("request body is not specified", 400))

        response = {}
        response.update({'message': "hi"})

        return response
