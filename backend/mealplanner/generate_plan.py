from datetime import date, timedelta
import random
import json

from backend.database.setup import SessionLocal
from backend.models.sql_models import MealPlan, Recipe

db = SessionLocal()

# Config
user_id = 1
start_date = date.today()
end_date = start_date + timedelta(days=6)
office_lunch_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]  # skip lunch

# Get all recipes (filter liked later)
recipes = db.query(Recipe).all()
recipe_names = [r.name for r in recipes]

# Simulate liked recipes
from backend.models.sql_models import UserPreference

prefs = db.query(UserPreference).filter(UserPreference.user_id == user_id, UserPreference.liked == 1).all()
liked_recipe_ids = [p.recipe_id for p in prefs]

liked_recipes = db.query(Recipe).filter(Recipe.id.in_(liked_recipe_ids)).all()

# fallback if no liked recipes
if not liked_recipes:
    liked_recipes = recipes

if not liked_recipes:
    liked_recipes = recipes

# Generate plan
meals = {}

for i in range(7):
    current_date = start_date + timedelta(days=i)
    day_name = current_date.strftime("%A")
    meals[current_date] = {}

    # Always generate dinner
    meals[current_date]["dinner"] = random.choice(liked_recipes).name

    # Optional: skip lunch if user is at office
    if day_name not in office_lunch_days:
        meals[current_date]["lunch"] = random.choice(liked_recipes).name

    # Breakfast (simple repeatable meal for now)
    meals[current_date]["breakfast"] = "Oatmeal"

# Save to DB
plan = MealPlan(
    user_id=user_id,
    start_date=str(start_date),
    end_date=str(end_date),
    servings_per_meal=1,
    meals_json=json.dumps({
        str(k): v for k, v in meals.items()
    })
)

db.add(plan)
db.commit()
db.close()

print("Weekly meal plan generated.")
