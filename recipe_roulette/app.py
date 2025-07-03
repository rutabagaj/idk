from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime, timedelta
from . import recipe_service

app = Flask(__name__)
app.secret_key = 'replace-this-secret'


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
    now = datetime.utcnow()
    last_upvotes = session.get('last_upvotes', {})
    last_time_str = last_upvotes.get(str(recipe_id))
    if last_time_str:
        last_time = datetime.fromisoformat(last_time_str)
        if now - last_time < timedelta(minutes=10):
            flash('You can only upvote this recipe once every 10 minutes.')
            return redirect(url_for('recipes'))

    recipe_service.upvote_recipe(recipe_id)
    last_upvotes[str(recipe_id)] = now.isoformat()
    session['last_upvotes'] = last_upvotes
    return redirect(url_for('recipes'))


if __name__ == '__main__':
    app.run(debug=True)
