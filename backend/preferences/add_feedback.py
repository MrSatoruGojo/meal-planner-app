from backend.database.setup import SessionLocal
from backend.models.sql_models import MealFeedback

db = SessionLocal()

feedback = MealFeedback(
    user_id=1,
    recipe_id=1,
    cooked=0,
    liked=0,
    notes="Had ingredients but didn’t feel like cooking."
)

db.add(feedback)
db.commit()
db.close()

print("Feedback saved.")
