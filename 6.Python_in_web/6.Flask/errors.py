from flask import jsonify
from urls import app


class Error(Exception):
    def __init__(self, status_code, error_message):
        self.status_code = status_code
        self.error_message = error_message


@app.errorhandler(Error)
def error_hadler(error):
    response = jsonify({
        'ERROR': f'{error.status_code} {error.error_message}'
    })
    response.status_code = error.status_code
    return response

