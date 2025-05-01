from backend.database.setup import SessionLocal
from backend.models.sql_models import Recipe, UserPreference

db = SessionLocal()
user_id = 1

# Simulate swipe logic
recipes = db.query(Recipe).all()

for i, recipe in enumerate(recipes):
    print(f"Swiping on: {recipe.name}")
    liked = 1 if "beef" in recipe.tags else 0

    pref = UserPreference(
        user_id=user_id,
        recipe_id=recipe.id,
        liked=liked
    )
    db.add(pref)

db.commit()
db.close()

print("Simulated swiping complete.")
