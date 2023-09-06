from flask import request, jsonify, make_response
from app.authorization import bp
from app.models.authorization import Authorization
from app.models.author import Author
from app.extensions import db
from app.storage import upload_image
from app.utils.cryptocoder import encrypt, decrypt, access_key
from app.utils.json_utils import success_response, failure_response, error_response

@bp.route('/signIn', methods=['POST'])
def sign_in():
  try:
    data = request.get_json()
    author = Author.query.filter_by(author_email=data['author_email']).first()
    if author:
        if decrypt(author.author_password) == data['author_password']:
            auth = Authorization(author_id=author.id, access_key=access_key())
            db.session.add(auth)
            db.session.commit()
            return make_response(success_response(result=auth.json()), 200)
        return make_response(failure_response('incorrect password'), 200)

    return make_response(failure_response('account has not found'), 201)

  except e:
    return make_response(error_response('error'), 500)

@bp.route('/signUp', methods=['POST'])
def sign_up():
  try:
    data = request.get_json()
    author = Author.query.filter_by(author_email=data['author_email']).first()
    if author:
        return make_response(failure_response('account with such email is already is exist'), 201)

    author_img = upload_image(data['author_img'], image_prefix=data['author_email'])
    new_author = Author(author_name=data['author_name'], author_email=data['author_email'], author_password=encrypt(data['author_password']), author_description=data['author_description'], author_img=author_img)
    db.session.add(new_author)
    db.session.commit()
    return make_response(success_response(message='account created'), 201)
  except e:
    return make_response(failure_response('error creating author'), 200)
