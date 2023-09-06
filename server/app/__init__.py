from flask import Flask, request, jsonify, make_response
from os import environ
from app.extensions import db
from app.storage import bucket

from app.main import bp as main_bp
from app.authors import bp as authors_bp
from app.recipes import bp as recipes_bp
from app.authorization import bp as auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

db.init_app(app)

app.register_blueprint(main_bp)
app.register_blueprint(authors_bp, url_prefix='/authors')
app.register_blueprint(recipes_bp, url_prefix='/recipes')
app.register_blueprint(auth_bp, url_prefix='/auth')

with app.app_context():
    db.create_all()
