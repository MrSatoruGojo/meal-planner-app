from backend.database.setup import SessionLocal
from backend.models.sql_models import UserProfile, Ingredient, Recipe

db = SessionLocal()

# Query all users
users = db.query(UserProfile).all()
print("Users:")
for u in users:
    print(f"- {u.name}, {u.age} years old")

# Query ingredients
ingredients = db.query(Ingredient).all()
print("\nIngredients:")
for i in ingredients:
    print(f"- {i.name}: {i.calories_per_unit} cal per {i.unit}")

# Query recipes
recipes = db.query(Recipe).all()
print("\nRecipes:")
for r in recipes:
    print(f"- {r.name}: {r.description}")

db.close()
