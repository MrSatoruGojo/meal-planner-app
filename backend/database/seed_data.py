from backend.database.setup import SessionLocal
from backend.models.sql_models import UserProfile, Ingredient, Recipe
from backend.models.sql_models import Recipe
import json
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey


db = SessionLocal()

# Sample user
user = UserProfile(
    name="Alice",
    age=28,
    height_cm=165,
    weight_kg=60,
    dietary_goals="maintenance"
)

# Sample ingredient
ingredient = Ingredient(
    name="beef",
    unit="g",
    calories_per_unit=2.5,
    shelf_life_days=5
)
# Add this to your Recipe class (if not already):
ingredients_json = Column(String)  # store ingredients as JSON list

# Sample recipe
recipe = Recipe(
    name="Beef Stir Fry",
    description="Beef stir fry with onion and rice",
    image_url="https://example.com/stirfry.jpg",
    tags="beef,quick,asian",
    user_uploaded=0,
    ingredients_json=json.dumps([
        {"name": "beef", "quantity": 200},
        {"name": "onion", "quantity": 1},
        {"name": "rice", "quantity": 150}
    ])
)

db.add_all([user, ingredient, recipe])
db.commit()
db.close()

print("Sample data inserted.")
