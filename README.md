# Recipe Roulette

Recipe Roulette is a simple web application that suggests recipes based on the ingredients you have at home. If no stored recipe matches, the app creates a simple recipe using whatever ingredients you entered. You can also contribute your own recipes and vote on others.

## Features

- Enter ingredients and get random recipe suggestions. When none of the built-in recipes match, the app generates an easy recipe using your ingredients.
- Submit new recipes with ingredients and instructions.
- View all recipes and upvote your favorites. Upvotes are limited to one every 10 minutes per user.

## Requirements

- Python 3.8+
- Packages listed in `requirements.txt`

## Running the app

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the application:
   ```bash
   python -m recipe_roulette.app
   ```
3. Open `http://localhost:5000` in your browser.

## Running tests

```
pytest -q
```
