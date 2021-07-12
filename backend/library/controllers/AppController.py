from flask import jsonify

from library import app
from library.DAL import LocationRep


@app.after_request
def after_request_func(response):
    # return response
    pass


@app.before_request
def before_request_func():
    pass


