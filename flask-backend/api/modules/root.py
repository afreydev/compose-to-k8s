import functools
from decouple import config
from flask import Blueprint, request, jsonify
from flask_cors import CORS

bp = Blueprint('root', __name__, url_prefix='/')
CORS(bp)

@bp.route('/', methods=['GET'])
def root():
    ret = config('MESSAGE', default='hello hello!')
    return jsonify(ret)
