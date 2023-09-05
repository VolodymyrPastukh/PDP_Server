from flask import request, jsonify, make_response
from app.authors import bp
from app.models.author import Author
from app.extensions import db
from app.utils.json_utils import success_response, failure_response, error_response

@bp.route('/', methods=['GET'])
def get_authors():
  try:
    authors = Author.query.all()
    return make_response(success_response(result=[author.json() for author in authors]), 200)
  except e:
    return make_response(error_response('error getting authors'), 500)

@bp.route('/<int:id>', methods=['GET'])
def get_author(id):
  try:
    author = Author.query.filter_by(id=id).first()
    if author:
      return make_response(success_response(result=author.json()), 200)
    return make_response(failure_response('author not found'), 200)
  except e:
    return make_response(error_response('error getting author'), 500)

@bp.route('/<int:id>', methods=['PUT'])
def update_author(id):
  try:
    author = Author.query.filter_by(id=id).first()
    if author:
      data = request.get_json()
      author.author_name = data['author_name']
      author.author_email = data['author_email']
      db.session.commit()
      return make_response(success_response(message='author updated'), 200)
    return make_response(failure_response('author not found'), 201)
  except e:
    return make_response(error_response('error updating author'), 500)
