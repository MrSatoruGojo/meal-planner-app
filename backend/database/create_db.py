# backend/database/create_db.py

from backend.database.setup import Base, engine
from backend.models.sql_models import UserProfile
from backend.models.sql_models import MealFeedback
from backend.models.sql_models import MealLog

# Create all tables
Base.metadata.create_all(bind=engine)
print("Database and tables created.")


from backend.models.sql_models import UserProfile, Ingredient, Recipe, MealPlan, GroceryList, MealLog
from backend.models.sql_models import UserPreference
