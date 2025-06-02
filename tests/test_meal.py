from models.meal_plan import MealPlan
from models.user import User
from sqlalchemy.orm import Session
import uuid

def test_meal_plan_placeholder():
    assert True

def test_create_meal_plan(test_db: Session):
    unique_email = f"mealuser_{uuid.uuid4()}@example.com"
    user = User(name="Test Meal User", email=unique_email)
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    meal_plan = MealPlan(user_id=user.id, description="Test meal plan")
    test_db.add(meal_plan)
    test_db.commit()
    test_db.refresh(meal_plan)
    assert meal_plan.id is not None
    assert meal_plan.description == "Test meal plan"
    assert meal_plan.user_id == user.id
