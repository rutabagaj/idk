import json
import random
from pathlib import Path
from typing import List

DATA_FILE = Path(__file__).resolve().parent.parent / 'data' / 'recipes.json'


def load_recipes():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


def save_recipes(recipes):
    with open(DATA_FILE, 'w') as f:
        json.dump(recipes, f, indent=2)




def filter_recipes(ingredients):
    recipes = load_recipes()
    lower_ingredients = {ing.strip().lower() for ing in ingredients if ing.strip()}
    if not lower_ingredients:
        return recipes
    matches = []
    for recipe in recipes:
        recipe_ings = {i.lower() for i in recipe['ingredients']}
        if lower_ingredients.issubset(recipe_ings):
            matches.append(recipe)
    return matches


def generate_simple_recipe(ingredients: List[str]) -> dict:
    """Create a basic recipe using the provided ingredients."""
    title = "Easy Dish with " + ", ".join(ingredients)
    instructions = (
        "Combine " + ", ".join(ingredients) + " and cook to taste."
    )
    return {
        "id": 0,
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions,
        "votes": 0,
    }


def random_recipes(ingredients, limit=3):
    matches = filter_recipes(ingredients)
    if not matches:
        matches.append(generate_simple_recipe(ingredients))
    random.shuffle(matches)
    return matches[:limit]


def add_recipe(title, ingredients, instructions):
    recipes = load_recipes()
    recipe_id = max((r['id'] for r in recipes), default=0) + 1
    recipe = {
        'id': recipe_id,
        'title': title,
        'ingredients': [ing.strip() for ing in ingredients if ing.strip()],
        'instructions': instructions,
        'votes': 0,
    }
    recipes.append(recipe)
    save_recipes(recipes)
    return recipe


def upvote_recipe(recipe_id):
    recipes = load_recipes()
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            recipe['votes'] += 1
            break
    save_recipes(recipes)

