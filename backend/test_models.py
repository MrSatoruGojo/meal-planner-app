# backend/test_models.py

from models.models import UserProfile, Ingredient, Recipe

user = UserProfile(
    name="John",
    age=30,
    height_cm=175,
    weight_kg=70,
    dietary_goals="muscle gain",
    preferred_ingredients=["beef", "rice"],
    avoided_ingredients=["shrimp", "pork"],
    ingredient_frequency={"beef": 20, "chicken": 5},
    office_meal_days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    fridge_capacity="medium"
)

print(user.__dict__)
