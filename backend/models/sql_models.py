# backend/models/sql_models.py

from sqlalchemy import Column, Integer, String
from backend.database.setup import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    height_cm = Column(Integer)
    weight_kg = Column(Integer)
    dietary_goals = Column(String)


from sqlalchemy import Float

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    unit = Column(String)
    calories_per_unit = Column(Float)
    shelf_life_days = Column(Integer)
    # You can normalize store prices into a separate table later

from sqlalchemy import Column, Integer, String

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image_url = Column(String)
    tags = Column(String)  # e.g., "beef,quick"
    user_uploaded = Column(Integer)  # 0 = False, 1 = True
    ingredients_json = Column(String)  # <- NEW LINE to store ingredients

class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    start_date = Column(String)
    end_date = Column(String)
    servings_per_meal = Column(Integer)
    meals_json = Column(String)  # Store meals as JSON string

class GroceryList(Base):
    __tablename__ = "grocery_lists"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    time_period = Column(String)
    ingredients_json = Column(String)
    optimized_store = Column(String)
    total_cost = Column(Float)
    delivery_fee = Column(Float)

class MealLog(Base):
    __tablename__ = "meal_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    date = Column(String)
    meal_type = Column(String)
    source = Column(String)
    photo_path = Column(String)
    recognized_items = Column(String)  # Optional, comma-separated
    estimated_calories = Column(Float)
from sqlalchemy import ForeignKey

class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_profiles.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    liked = Column(Integer)  # 1 = liked, 0 = disliked
from sqlalchemy import Text

class MealFeedback(Base):
    __tablename__ = "meal_feedback"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    recipe_id = Column(Integer)
    cooked = Column(Integer)  # 1 = cooked, 0 = not cooked
    liked = Column(Integer)   # 1 = liked, 0 = disliked
    notes = Column(Text)      # Optional comment (e.g., “Too spicy”, “Didn’t feel like it”)
