from app.extensions import db


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    recipe_title = db.Column(db.String(80), nullable=False)
    recipe_country = db.Column(db.String(80), nullable=False)
    recipe_description = db.Column(db.String, nullable=True)
    recipe_img = db.Column(db.String, nullable=True)
    steps = db.relationship('RecipeStep', backref='recipe')

    def json(self):
        return {'id': self.id,'author_id':self.author_id,'recipe_title': self.recipe_title, 'recipe_country': self.recipe_country, 'recipe_description': self.recipe_description, 'recipe_img': self.recipe_img}

    def json(self, steps:list):
        _steps = list(map(lambda step: step.json(), steps))
        return {'id': self.id,'author_id':self.author_id, 'recipe_title': self.recipe_title, 'recipe_country': self.recipe_country, 'recipe_description': self.recipe_description,'recipe_img': self.recipe_img, 'steps': _steps}




class RecipeStep(db.Model):
    __tablename__ = 'recipes_steps'

    id = db.Column(db.Integer, primary_key=True)
    recipe_step_id = db.Column(db.Integer, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    recipe_step_title = db.Column(db.String(80), nullable=False)
    recipe_step_instruction = db.Column(db.String, nullable=False)
    recipe_step_duration_millis = db.Column(db.Integer, nullable=False)
    recipe_step_img = db.Column(db.String, nullable=True)

    def json(self):
        return {'id': self.id,'recipe_step_id': self.recipe_step_id, 'recipe_id': self.recipe_id, 'recipe_step_title': self.recipe_step_title,'recipe_step_instruction': self.recipe_step_instruction,'recipe_step_duration_millis': self.recipe_step_duration_millis, 'recipe_step_img': self.recipe_step_img}
