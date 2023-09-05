from app.extensions import db

class Authorization(db.Model):
    __tablename__ = 'authotrization'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    access_key = db.Column(db.String, unique=True, nullable=False)

    def json(self):
        return {'id': self.id,'author_id': self.author_id, 'access_key': self.access_key}
