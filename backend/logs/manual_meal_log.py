from datetime import date
from backend.database.setup import SessionLocal
from backend.models.sql_models import MealLog

db = SessionLocal()

log = MealLog(
    user_id=1,
    date=str(date.today()),
    meal_type="lunch",
    source="restaurant",
    photo_path="",
    recognized_items="chicken, salad, bread",
    estimated_calories=620
)

db.add(log)
db.commit()
db.close()

print("Manual meal log saved.")
