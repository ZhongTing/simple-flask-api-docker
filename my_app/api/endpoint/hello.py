from flask import (
    Blueprint, request
)
from flask import jsonify

from my_app.api.util import try_get

bp = Blueprint('hello', __name__, url_prefix='/api/endpoint')


@bp.route('hello', methods=['GET'])
def hello():
    return jsonify({'result': 'hello'})


@bp.route('world', methods=['POST'])
def world():
    post_data = request.get_json()
    content = try_get(post_data, 'content')
    return jsonify({'result': content})
