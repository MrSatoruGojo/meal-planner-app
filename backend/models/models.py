# backend/models/models.py

from typing import List, Dict, Tuple

class UserProfile:
    def __init__(self, name: str, age: int, height_cm: float, weight_kg: float,
                 dietary_goals: str, preferred_ingredients: List[str], 
                 avoided_ingredients: List[str], ingredient_frequency: Dict[str, int],
                 office_meal_days: List[str], fridge_capacity: str):
        self.name = name
        self.age = age
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.dietary_goals = dietary_goals
        self.preferred_ingredients = preferred_ingredients
        self.avoided_ingredients = avoided_ingredients
        self.ingredient_frequency = ingredient_frequency
        self.office_meal_days = office_meal_days
        self.fridge_capacity = fridge_capacity


class Ingredient:
    def __init__(self, name: str, unit: str, calories_per_unit: float, 
                 shelf_life_days: int, store_prices: Dict[str, float]):
        self.name = name
        self.unit = unit
        self.calories_per_unit = calories_per_unit
        self.shelf_life_days = shelf_life_days
        self.store_prices = store_prices


class Recipe:
    def __init__(self, name: str, description: str, ingredients: List[Tuple[str, float]],
                 tags: List[str], steps: List[str], image_url: str = "", user_uploaded: bool = False):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.tags = tags
        self.steps = steps
        self.image_url = image_url
        self.user_uploaded = user_uploaded
from datetime import date

class MealPlan:
    def __init__(self, user_id: str, date_range: Tuple[date, date],
                 meals: Dict[date, Dict[str, str]], servings_per_meal: int):
        """
        meals = {
            2025-05-01: {"breakfast": "Oatmeal", "lunch": "Grilled Chicken"},
            2025-05-02: {"lunch": "Pasta", "dinner": "Beef Stir Fry"}
        }
        """
        self.user_id = user_id
        self.date_range = date_range
        self.meals = meals
        self.servings_per_meal = servings_per_meal


class GroceryList:
    def __init__(self, user_id: str, time_period: str, ingredients: List[Tuple[str, float]],
                 optimized_store: str, total_cost: float, delivery_fee: float):
        """
        ingredients = [("rice", 500), ("beef", 1000)]
        """
        self.user_id = user_id
        self.time_period = time_period
        self.ingredients = ingredients
        self.optimized_store = optimized_store
        self.total_cost = total_cost
        self.delivery_fee = delivery_fee


class MealLog:
    def __init__(self, user_id: str, date: date, meal_type: str,
                 source: str, photo_path: str = "", recognized_items: List[str] = None,
                 estimated_calories: float = 0.0):
        self.user_id = user_id
        self.date = date
        self.meal_type = meal_type
        self.source = source
        self.photo_path = photo_path
        self.recognized_items = recognized_items if recognized_items else []
        self.estimated_calories = estimated_calories
