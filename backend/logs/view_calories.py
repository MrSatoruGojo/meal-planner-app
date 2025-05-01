from backend.database.setup import SessionLocal
from backend.models.sql_models import MealLog

db = SessionLocal()
user_id = 1

logs = db.query(MealLog).filter(MealLog.user_id == user_id).all()

daily_totals = {}
for log in logs:
    calories = log.estimated_calories or 0
    day = log.date
    if day not in daily_totals:
        daily_totals[day] = 0
    daily_totals[day] += calories

db.close()

print("Daily Calorie Summary:")
for day, total in daily_totals.items():
    print(f"{day}: {total} kcal")
