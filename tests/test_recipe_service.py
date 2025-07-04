import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import json
from recipe_roulette import recipe_service


def test_filter_recipes_exact_match(tmp_path, monkeypatch):
    data_file = tmp_path / 'recipes.json'
    recipes = [
        {"id": 1, "title": "R1", "ingredients": ["a", "b"], "instructions": "", "votes": 0},
        {"id": 2, "title": "R2", "ingredients": ["b", "c"], "instructions": "", "votes": 0},
    ]
    data_file.write_text(json.dumps(recipes))
    monkeypatch.setattr(recipe_service, 'DATA_FILE', data_file)

    result = recipe_service.filter_recipes(["a", "b"])
    assert len(result) == 1
    assert result[0]['title'] == "R1"


def test_upvote_recipe(tmp_path, monkeypatch):
    data_file = tmp_path / 'recipes.json'
    recipes = [
        {"id": 1, "title": "R1", "ingredients": ["a"], "instructions": "", "votes": 0}
    ]
    data_file.write_text(json.dumps(recipes))
    monkeypatch.setattr(recipe_service, 'DATA_FILE', data_file)

    recipe_service.upvote_recipe(1)
    data = json.loads(data_file.read_text())
    assert data[0]['votes'] == 1



def test_random_recipes_generated(monkeypatch):
    def fake_filter(_):
        return []

    monkeypatch.setattr(recipe_service, 'filter_recipes', fake_filter)

    result = recipe_service.random_recipes(['x'])
    assert result[0]['ingredients'] == ['x']

