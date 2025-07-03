from flask import Flask, render_template, request, redirect, url_for
from . import recipe_service

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spin', methods=['POST'])
def spin():
    ingredients = request.form.get('ingredients', '')
    ingredient_list = [ing.strip() for ing in ingredients.split(',')]
    recipes = recipe_service.random_recipes(ingredient_list)
    return render_template('results.html', recipes=recipes, ingredients=ingredients)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions']
        recipe_service.add_recipe(title, ingredients, instructions)
        return redirect(url_for('recipes'))
    return render_template('submit.html')


@app.route('/recipes')
def recipes():
    recipes = recipe_service.load_recipes()
    return render_template('recipes.html', recipes=recipes)


@app.route('/upvote/<int:recipe_id>', methods=['POST'])
def upvote(recipe_id):
    recipe_service.upvote_recipe(recipe_id)
    return redirect(url_for('recipes'))


if __name__ == '__main__':
    app.run(debug=True)
