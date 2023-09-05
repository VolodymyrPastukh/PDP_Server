from app.extensions import db


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(80), unique=True, nullable=False)
    author_email = db.Column(db.String(120), unique=True, nullable=False)
    author_password = db.Column(db.String, unique=True, nullable=False)
    author_description = db.Column(db.String, unique=True, nullable=True)
    recipes = db.relationship('Recipe', backref='author')

    def json(self):
        return {'id': self.id,'author_name': self.author_name, 'author_email': self.author_email, 'author_password': self.author_password, 'author_description': self.author_description}
