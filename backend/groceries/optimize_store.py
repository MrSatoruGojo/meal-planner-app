import json
from backend.database.setup import SessionLocal
from backend.models.sql_models import GroceryList
from backend.groceries.store_prices import tesco_prices, asda_prices, store_delivery_fees

db = SessionLocal()

# Get latest grocery list
grocery = db.query(GroceryList).order_by(GroceryList.id.desc()).first()
needed_ingredients = json.loads(grocery.ingredients_json)

# Calculate basket totals
def calculate_total(prices, delivery_fee):
    total = 0
    for name, qty in needed_ingredients.items():
        price_per_unit = prices.get(name, 0)
        total += price_per_unit * qty
    return total + delivery_fee

tesco_total = calculate_total(tesco_prices, store_delivery_fees["Tesco"])
asda_total = calculate_total(asda_prices, store_delivery_fees["Asda"])

# Choose the cheaper one
if tesco_total <= asda_total:
    selected_store = "Tesco"
    selected_total = tesco_total
    delivery_fee = store_delivery_fees["Tesco"]
else:
    selected_store = "Asda"
    selected_total = asda_total
    delivery_fee = store_delivery_fees["Asda"]

# Update grocery list
grocery.optimized_store = selected_store
grocery.total_cost = round(selected_total, 2)
grocery.delivery_fee = round(delivery_fee, 2)

db.commit()
db.close()

print(f"Best option: {selected_store} → £{selected_total:.2f} (includes delivery)")
