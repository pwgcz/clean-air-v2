import os

from flask import Blueprint


send_static = Blueprint("send_static", __name__, static_folder='./build', static_url_path='/static')

from . import url
