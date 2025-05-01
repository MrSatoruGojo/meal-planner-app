import json
from collections import defaultdict

from backend.database.setup import SessionLocal
from backend.models.sql_models import MealPlan, Recipe, GroceryList


import json
from collections import defaultdict

from backend.database.setup import SessionLocal
from backend.models.sql_models import MealPlan, Recipe, GroceryList

# ✅ Step 2: Simulated fridge stock
fridge_stock = {
    "beef": 300,
    "rice": 200,
    "onion": 2
}


db = SessionLocal()

# Settings
user_id = 1
servings = 1
fridge_stock = {"beef": 300, "onion": 2, "rice": 200}

# Get latest meal plan
plan = db.query(MealPlan).order_by(MealPlan.id.desc()).first()
meals = json.loads(plan.meals_json)

# Collect ingredients
total_ingredients = defaultdict(float)

for day, day_meals in meals.items():
    for meal_type, recipe_name in day_meals.items():
        recipe = db.query(Recipe).filter(Recipe.name == recipe_name).first()
        if not recipe or not recipe.ingredients_json:
            continue
        ingredients = json.loads(recipe.ingredients_json)
        for item in ingredients:
            total_ingredients[item["name"]] += item["quantity"] * servings

# Subtract fridge stock
missing_ingredients = {}
for name, total_qty in total_ingredients.items():
    fridge_qty = fridge_stock.get(name, 0)
    required_qty = max(0, total_qty - fridge_qty)
    if required_qty > 0:
        missing_ingredients[name] = required_qty

# Save grocery list
grocery = GroceryList(
    user_id=user_id,
    time_period="weekly",
    ingredients_json=json.dumps(missing_ingredients),
    optimized_store="TBD",
    total_cost=0.0,
    delivery_fee=0.0
)

db.add(grocery)
db.commit()
db.close()

print("Grocery list created:")
for name, qty in missing_ingredients.items():
    print(f"- {name}: {qty}")


