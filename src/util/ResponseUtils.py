import json

from flask import make_response


def custom_response(message, status_code):
    return make_response(json.dumps({'message': message}, ensure_ascii=False).encode('utf-8'), status_code)
