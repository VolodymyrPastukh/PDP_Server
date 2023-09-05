from flask import request, jsonify, make_response
from app.main import bp

@bp.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)
