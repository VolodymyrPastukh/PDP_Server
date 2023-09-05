from flask import request, jsonify, make_response
from app.recipes import bp
from app.models.authorization import Authorization
from app.models.recipe import Recipe, RecipeStep
from app.extensions import db
from app.utils.json_utils import success_response, failure_response, error_response

@bp.route('/', methods=['POST'])
def create_recipe():
  try:
    data = request.get_json()
    auth_header = request.headers['Authorization']

    if 'author_id' not in data:
        return make_response(failure_response('there in no author'), 200)

    if not auth_header in list(map(lambda auth: auth.access_key, Authorization.query.filter_by(author_id=data['author_id']))):
        return make_response(failure_response('you have no access'), 200)

    new_recipe = Recipe(author_id=data['author_id'], recipe_title=data['recipe_title'], recipe_country=data['recipe_country'], recipe_description=data['recipe_description'])

    new_recipe_steps = []
    for step in data['steps']:
        new_recipe_steps.append(RecipeStep(recipe=new_recipe, recipe_step_title=step['recipe_step_title'], recipe_step_instruction=step['recipe_step_instruction'],recipe_step_duration_millis=step['recipe_step_duration_millis']))

    db.session.add(new_recipe)
    db.session.add_all(new_recipe_steps)
    db.session.commit()
    return make_response(success_response(result=new_recipe.json(steps=RecipeStep.query.filter_by(recipe_id=new_recipe.id)), message='recipe created'), 200)
  except e:
    return make_response(error_response('error creating recipe'), 500)

@bp.route('/', methods=['GET'])
def get_recipes():
  try:
    recipes = Recipe.query.all()
    return make_response(success_response(result=[recipe.json(steps = RecipeStep.query.filter_by(recipe_id=recipe.id)) for recipe in recipes]), 200)
  except e:
    return make_response(error_response('error getting recipes'), 500)

@bp.route('/<int:id>', methods=['GET'])
def get_recipe(id):
  try:
    recipe = Recipe.query.filter_by(id=id).first()
    if recipe:
      return make_response(success_response(result=recipe.json(RecipeStep.query.filter_by(recipe_id=recipe.id))), 200)
    return make_response(failure_response('recipe not found'), 200)
  except e:
    return make_response(error_response('error getting recipe'), 500)

@bp.route('/<int:id>', methods=['DELETE'])
def delete_recipe(id):
  try:
    recipe = Recipe.query.filter_by(id=id).first()
    if recipe:
        for step in RecipeStep.query.filter_by(recipe_id=recipe.id):
            db.session.delete(step)
        db.session.delete(recipe)
        db.session.commit()
        return make_response(success_response(message='recipe deleted'), 200)
    return make_response(failure_response('author not found'), 200)
  except e:
    return make_response(error_response('error deleting author'), 500)
