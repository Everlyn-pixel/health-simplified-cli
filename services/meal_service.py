from database.setup import SessionLocal
from models.meal_plan import MealPlan
from models.user import User

def add_meal_plan(user_name, week, description=None):
    db = SessionLocal()
    user = db.query(User).filter(User.name == user_name).first()
    if not user:
        print("User not found.")
        db.close()
        return
    if description is None:
        description = f"Meal plan for week {week}"
    meal_plan = MealPlan(user_id=user.id, description=description)
    db.add(meal_plan)
    db.commit()
    print(f"✅ Meal plan created for {user_name} (week {week})")
    db.close()

def update_meal_plan(id, description=None):
    db = SessionLocal()
    meal_plan = db.query(MealPlan).get(id)
    if not meal_plan:
        print("Meal plan not found.")
        db.close()
        return
    if description:
        meal_plan.description = description
    db.commit()
    print(f"✏️ Meal plan {id} updated.")
    db.close()

def list_meal_plans(user_name=None):
    db = SessionLocal()
    query = db.query(MealPlan)
    if user_name:
        user = db.query(User).filter(User.name == user_name).first()
        if not user:
            print("User not found.")
            db.close()
            return
        query = query.filter(MealPlan.user_id == user.id)
    plans = query.all()
    if not plans:
        print("No meal plans found.")
    for plan in plans:
        print(f"ID: {plan.id}, User ID: {plan.user_id}, Description: {plan.description}")
    db.close()
